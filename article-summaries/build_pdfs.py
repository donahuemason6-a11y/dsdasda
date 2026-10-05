"""Render each article summary .txt in this folder to a PDF.

Source format: "Key: value" header lines, then "## Summary" and "## Opinion"
sections of plain paragraphs separated by blank lines. The word count is
computed from the section bodies only and inserted into the header.

Usage: python3 build_pdfs.py
"""
import re
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib import colors

HERE = Path(__file__).parent


def parse(path: Path):
    header, sections, current = {}, {}, None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if line.startswith("## "):
            current = line[3:].strip()
            sections[current] = []
        elif current is None:
            if line.strip():
                key, _, value = line.partition(":")
                header[key.strip()] = value.strip()
        else:
            if line.strip():
                if sections[current] and sections[current][-1] is not None:
                    sections[current][-1] += " " + line.strip()
                else:
                    sections[current].append(line.strip())
            else:
                sections[current].append(None)
    for name, paras in sections.items():
        sections[name] = [p for p in paras if p]
    return header, sections


def word_count(paragraphs):
    return sum(len(re.findall(r"\S+", p)) for p in paragraphs)


def build(path: Path):
    header, sections = parse(path)
    counts = {name: word_count(paras) for name, paras in sections.items()}
    total = sum(counts.values())
    breakdown = ", ".join(f"{name} {n}" for name, n in counts.items())
    header["Word Count"] = f"{total} ({breakdown})"

    body = ParagraphStyle(
        "body", fontName="Times-Roman", fontSize=12, leading=18,
        alignment=TA_JUSTIFY, spaceAfter=10, firstLineIndent=0.4 * inch,
    )
    heading = ParagraphStyle(
        "heading", fontName="Times-Bold", fontSize=13, leading=18,
        spaceBefore=10, spaceAfter=6,
    )
    title = ParagraphStyle(
        "title", fontName="Times-Bold", fontSize=15, leading=20, spaceAfter=12,
    )
    cell_key = ParagraphStyle("k", fontName="Times-Bold", fontSize=11, leading=14)
    cell_val = ParagraphStyle("v", fontName="Times-Roman", fontSize=11, leading=14)

    story = [Paragraph("Article Summary and Opinion", title)]
    rows = [[Paragraph(escape(k), cell_key), Paragraph(escape(v), cell_val)]
            for k, v in header.items()]
    table = Table(rows, colWidths=[1.45 * inch, 5.05 * inch])
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ]))
    story += [table, Spacer(1, 14)]

    for name, paras in sections.items():
        story.append(Paragraph(escape(name), heading))
        story += [Paragraph(escape(p), body) for p in paras]

    out = path.with_suffix(".pdf")

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("Times-Roman", 10)
        canvas.drawCentredString(letter[0] / 2, 0.55 * inch, str(doc.page))
        canvas.restoreState()

    doc = SimpleDocTemplate(
        str(out), pagesize=letter, leftMargin=1 * inch, rightMargin=1 * inch,
        topMargin=1 * inch, bottomMargin=1 * inch,
        title=header.get("Name of Article", out.stem),
        author=header.get("Student Name", ""),
    )
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f"{out.name}: {header['Word Count']}")


if __name__ == "__main__":
    for src in sorted(HERE.glob("*.txt")):
        build(src)
