import math
BLUE="#0033cc"; RED="#cc0000"; GREEN="#007a1f"; SH="#f7c5c5"; SH2="#d9d9d9"; GSH="#cfe9d6"; LB="#dbe4ff"; GRAY="#555"

def T(x,y,s,size=9,color="#000",anchor="middle",bold=False,italic=False):
    w=' font-weight="bold"' if bold else ''
    it=' font-style="italic"' if italic else ''
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{color}" text-anchor="{anchor}"{w}{it}>{s}</text>'

def _zx(z,x0,x1,zlo,zhi): return x0+(x1-x0)*(z-zlo)/(zhi-zlo)
def _bellpath(x0,x1,base,peak,zlo,zhi,n=64):
    pts=[(x0+(x1-x0)*i/n, base-peak*math.exp(-((zlo+(zhi-zlo)*i/n)**2)/2)) for i in range(n+1)]
    return "M"+" L".join(f"{x:.1f} {y:.1f}" for x,y in pts)
def _shade(x0,x1,base,peak,za,zb,zlo,zhi,fill=SH):
    n=40; pts=[(_zx(za,x0,x1,zlo,zhi),base)]
    for i in range(n+1):
        z=za+(zb-za)*i/n; pts.append((_zx(z,x0,x1,zlo,zhi), base-peak*math.exp(-z*z/2)))
    pts.append((_zx(zb,x0,x1,zlo,zhi),base))
    return '<polygon points="'+" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)+f'" fill="{fill}" stroke="none"/>'

def panel(ox,w,title,kw,shades,cuts,rules,mu=True,inside=(),zlo=-3.2,zhi=3.2,base=58,peak=34):
    """one mini bell. shades: [(za,zb,fill)], cuts: [(z,label)], rules: [str], inside: [(z,yoff,text,color)]"""
    x0,x1=ox+4,ox+w-4; s=[]
    s.append(T(ox+w/2,9,title,10,"#000",bold=True))
    s.append(T(ox+w/2,18,kw,7.8,BLUE))
    for za,zb,fill in shades: s.append(_shade(x0,x1,base,peak,za,zb,zlo,zhi,fill))
    s.append(f'<path d="{_bellpath(x0,x1,base,peak,zlo,zhi)}" fill="none" stroke="#000" stroke-width="1.1"/>')
    s.append(f'<line x1="{x0}" y1="{base}" x2="{x1}" y2="{base}" stroke="#000" stroke-width="0.8"/>')
    if mu:
        xm=_zx(0,x0,x1,zlo,zhi)
        s.append(f'<line x1="{xm:.1f}" y1="{base-peak}" x2="{xm:.1f}" y2="{base+3}" stroke="{GRAY}" stroke-width="0.6" stroke-dasharray="2,1.5"/>')
        s.append(T(xm,base+10,"μ",9,"#000"))
    for z,lab in cuts:
        xc=_zx(z,x0,x1,zlo,zhi); yc=base-peak*math.exp(-z*z/2)
        s.append(f'<line x1="{xc:.1f}" y1="{yc:.1f}" x2="{xc:.1f}" y2="{base+3}" stroke="{RED}" stroke-width="0.9"/>')
        s.append(T(xc,base+10,lab,9,RED,bold=True))
    for z,yoff,txt,col in inside:
        s.append(T(_zx(z,x0,x1,zlo,zhi),base-yoff,txt,8,col,bold=True))
    y=base+21
    for r in rules:
        s.append(T(ox+w/2,y,r,8.6,RED,bold=True)); y+=9.5
    return "".join(s)

def svg(w,h,body,cap=None):
    out=f'<div class="fig"><svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">{body}</svg>'
    if cap: out+=f'<div class="cap">{cap}</div>'
    return out+'</div>'

def fig_bells():
    b=[]
    b.append(panel(0,100,"LEFT","less than · below · at most",[(-3.2,0.8,SH)],[(0.8,"x")],["shaded = table value"]))
    b.append(panel(100,100,"RIGHT","more than · above · at least",[(0.8,3.2,SH)],[(0.8,"x")],["shaded = 1 − table"]))
    b.append(panel(200,100,"BETWEEN","from x₁ to x₂",[(-1.3,1.4,SH)],[(-1.3,"x₁"),(1.4,"x₂")],["left of x₂ − left of x₁"],mu=False))
    for k in (100,200): b.append(f'<line x1="{k}" y1="4" x2="{k}" y2="86" stroke="#bbb" stroke-width="0.5"/>')
    return svg(300,90,"".join(b))

def fig_back():
    b=[]
    b.append(panel(0,100,"NEGATIVE z","mirror image → same area",[(-3.2,-1.0,SH),(1.0,3.2,SH2)],[(-1.0,"−z"),(1.0,"+z")],["area left of −z","= 1 − (left of +z)"]))
    b.append(panel(100,100,"k-th PERCENTILE","k% of values sit below x",[(-3.2,-0.9,SH)],[(-0.9,"x = ?")],["left area k/100 → z","(find it INSIDE the table)","x = μ + z·σ"],mu=False,inside=[(-2.65,1,"k/100",RED)]))
    b.append(panel(200,100,"TOP 10% cutoff","top 10% → left area 0.90",[(-3.2,1.28,SH)],[(1.28,"x = ?")],["left 0.90 → z = 1.28","x = μ + 1.28σ"],inside=[(-0.3,12,"0.90",RED),(2.15,9,"0.10",GRAY)]))
    for k in (100,200): b.append(f'<line x1="{k}" y1="4" x2="{k}" y2="106" stroke="#bbb" stroke-width="0.5"/>')
    return svg(300,108,"".join(b))

def fig_emp():
    x0,x1=18,282; zlo,zhi=-3.6,3.6; base=62; peak=44; s=[]
    s.append(T(150,9,"The normal curve · Empirical Rule (68 – 95 – 99.7)",10,"#000",bold=True))
    bands=[(0,1,"34%"),(1,2,"13.5%"),(2,3,"2.35%"),(3,3.6,"0.15%")]
    for i,(a,c,lab) in enumerate(bands):
        fill=["#f7c5c5","#fbdede","#fdeeee","#ffffff"][i]
        s.append(_shade(x0,x1,base,peak,a,c,zlo,zhi,fill)); s.append(_shade(x0,x1,base,peak,-c,-a,zlo,zhi,fill))
    s.append(f'<path d="{_bellpath(x0,x1,base,peak,zlo,zhi)}" fill="none" stroke="#000" stroke-width="1.1"/>')
    s.append(f'<line x1="{x0}" y1="{base}" x2="{x1}" y2="{base}" stroke="#000" stroke-width="0.8"/>')
    for z in range(-3,4):
        xz=_zx(z,x0,x1,zlo,zhi); yz=base-peak*math.exp(-z*z/2)
        s.append(f'<line x1="{xz:.1f}" y1="{yz:.1f}" x2="{xz:.1f}" y2="{base+3}" stroke="{GRAY}" stroke-width="0.7"/>')
        lab={-3:"μ−3σ",-2:"μ−2σ",-1:"μ−σ",0:"μ",1:"μ+σ",2:"μ+2σ",3:"μ+3σ"}[z]
        s.append(T(xz,base+11,lab,8.2,"#000"))
    for sign in (1,-1):
        s.append(T(_zx(0.5*sign,x0,x1,zlo,zhi),base-13,"34%",9,RED,bold=True))
        s.append(T(_zx(1.4*sign,x0,x1,zlo,zhi),base-3,"13.5%",6.8,RED,bold=True))
        s.append(T(_zx(2.5*sign,x0,x1,zlo,zhi),base-10,"2.35%",7.2,RED,bold=True))
        s.append(T(_zx(3.3*sign,x0,x1,zlo,zhi),base-10,"0.15%",7.2,GRAY,bold=True))
    y=base+21
    for zz,lab in ((1,"68%"),(2,"95%"),(3,"99.7%")):
        xa,xb=_zx(-zz,x0,x1,zlo,zhi),_zx(zz,x0,x1,zlo,zhi)
        s.append(f'<line x1="{xa:.1f}" y1="{y}" x2="{xb:.1f}" y2="{y}" stroke="{RED}" stroke-width="0.8"/>')
        for xx in (xa,xb): s.append(f'<line x1="{xx:.1f}" y1="{y-3}" x2="{xx:.1f}" y2="{y+3}" stroke="{RED}" stroke-width="0.8"/>')
        s.append(f'<rect x="{150-15}" y="{y-5}" width="30" height="9" fill="#fff"/>')
        s.append(T(150,y+3,lab,8,RED,bold=True)); y+=10
    s.append(T(150,y+1,"68% within 1 SD · 95% within 2 SD · 99.7% within 3 SD · pieces: 34 | 13.5 | 2.35 | 0.15",6.8,BLUE))
    return svg(300,y+4,"".join(s))

def fig_uniform():
    a,b=70,100; L,R=62,272; top,base=26,58; s=[]
    def X(v): return L+(R-L)*(v-a)/(b-a)
    s.append(T(150,9,"Uniform on [a, b] = a flat rectangle (Q5: 70°F to 100°F)",10,"#000",bold=True))
    s.append(f'<rect x="{L}" y="{top}" width="{R-L}" height="{base-top}" fill="#fff" stroke="#000" stroke-width="1"/>')
    s.append(f'<rect x="{X(75):.1f}" y="{top}" width="{X(85)-X(75):.1f}" height="{base-top}" fill="{SH}" stroke="{RED}" stroke-width="0.8"/>')
    s.append(f'<line x1="{L-6}" y1="{base}" x2="{R+10}" y2="{base}" stroke="#000" stroke-width="0.8"/>')
    for v in (70,75,85,100):
        s.append(f'<line x1="{X(v):.1f}" y1="{base}" x2="{X(v):.1f}" y2="{base+3}" stroke="#000" stroke-width="0.8"/>')
        s.append(T(X(v),base+11,str(v),8.6,"#000",bold=v in (75,85)))
    s.append(T(L-5,top+8,"height =",8,RED,anchor="end",bold=True)); s.append(T(L-5,top+17,"1/(b − a)",8,RED,anchor="end",bold=True)); s.append(T(L-5,top+26,"= 1/30",8,RED,anchor="end",bold=True))
    xm=(X(75)+X(85))/2
    s.append(T(xm,top+12,"10/30",8.2,RED,bold=True)); s.append(T(xm,top+21,"= 0.3333",8.2,RED,bold=True)); s.append(T(xm,top+30,"(85−75)/30",7,RED))
    s.append(T((X(85)+R)/2,top+13,"total area",8,BLUE)); s.append(T((X(85)+R)/2,top+22,"= 30 × 1/30 = 1",8,BLUE))
    s.append(T(150,base+21,"P(c ≤ X ≤ d) = (d − c)/(b − a) = the strip's width ÷ the whole width",7.4,BLUE))
    s.append(T(150,base+30,"P(X < 80) = (80 − 70)/30 = 0.3333 · never use z for a uniform · P(X = 80) = 0",7.4,BLUE))
    return svg(300,base+34,"".join(s))

def fig_discrete():
    xs=[4,5,6,7]; ps=[0.2410,0.2410,0.3133,0.2048]; base=72; top=18; ax=40; s=[]
    s.append(T(150,9,"Q3(b) graph of the distribution: a bar above each x, height = P(x)",9.6,"#000",bold=True))
    sc=(base-top)/0.35
    s.append(f'<line x1="{ax}" y1="{top-2}" x2="{ax}" y2="{base}" stroke="#000" stroke-width="0.8"/>')
    s.append(f'<line x1="{ax}" y1="{base}" x2="285" y2="{base}" stroke="#000" stroke-width="0.8"/>')
    for t in (0,0.1,0.2,0.3):
        y=base-t*sc; s.append(f'<line x1="{ax-3}" y1="{y:.1f}" x2="{ax}" y2="{y:.1f}" stroke="#000" stroke-width="0.8"/>'); s.append(T(ax-5,y+3,f"{t:.1f}",7.6,"#000",anchor="end"))
    s.append(T(ax+4,top+3,"P(x)",8,"#000",anchor="start",bold=True))
    for i,(x,p) in enumerate(zip(xs,ps)):
        cx=75+i*54; h=p*sc
        s.append(f'<rect x="{cx-16}" y="{base-h:.1f}" width="32" height="{h:.1f}" fill="{GSH}" stroke="{GREEN}" stroke-width="0.9"/>')
        s.append(T(cx,base-h-3,f"{p:.4f}",7.8,GREEN,bold=True)); s.append(T(cx,base+10,str(x),9,"#000",bold=True))
    s.append(T(288,base+10,"(x = games)",7.6,"#000",anchor="end"))
    s.append(T(150,base+21,"Label both axes (x across, P(x) up). Heights = the P(x) values from (a); tallest bar = most likely x.",7.6,BLUE))
    return svg(300,base+25,"".join(s))

def fig_venn():
    s=[]; r=15; cy=38
    def circ(cx,cy,fill,stroke="#000",sw=0.9,extra=""): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'
    # OR
    s.append(T(50,9,"OR",10,"#000",bold=True)); s.append(T(50,18,"take the overlap out once",7.2,BLUE))
    s.append('<clipPath id="vcE"><circle cx="40" cy="38" r="15"/></clipPath>')
    s.append(circ(40,cy,"#fff")); s.append(circ(60,cy,"#fff")); s.append(f'<circle cx="60" cy="{cy}" r="{r}" fill="{SH}" clip-path="url(#vcE)"/>'); s.append(circ(40,cy,"none")); s.append(circ(60,cy,"none"))
    s.append(T(31,cy+3,"E",9,"#000",bold=True)); s.append(T(69,cy+3,"F",9,"#000",bold=True)); s.append(T(50,cy+22,"overlap = E and F",7.4,RED))
    s.append(T(50,cy+32,"P(E) + P(F) − P(E and F)",8.4,RED,bold=True))
    # DISJOINT
    s.append(T(150,9,"DISJOINT",10,"#000",bold=True)); s.append(T(150,18,"can't both happen",7.2,BLUE))
    s.append(circ(132,cy,"#fff")); s.append(circ(168,cy,"#fff")); s.append(T(132,cy+3,"E",9,"#000",bold=True)); s.append(T(168,cy+3,"F",9,"#000",bold=True))
    s.append(T(150,cy+22,"P(E and F) = 0",7.4,RED)); s.append(T(150,cy+32,"OR: just P(E) + P(F)",8.4,RED,bold=True))
    # GIVEN
    s.append(T(250,9,"GIVEN E",10,"#000",bold=True)); s.append(T(250,18,"the world shrinks to E",7.2,BLUE))
    s.append('<clipPath id="vcE2"><circle cx="240" cy="38" r="15"/></clipPath>')
    s.append(circ(240,cy,LB)); s.append(circ(260,cy,"#fff",extra='fill-opacity="0"')); s.append(f'<circle cx="260" cy="{cy}" r="{r}" fill="{SH}" clip-path="url(#vcE2)"/>'); s.append(circ(240,cy,"none",RED,1.6)); s.append(circ(260,cy,"none"))
    s.append(T(231,cy+3,"E",9,"#000",bold=True)); s.append(T(269,cy+3,"F",9,"#000",bold=True)); s.append(T(250,cy+22,"divide by E's total, not N",7.4,RED))
    s.append(T(250,cy+32,"P(F | E) = overlap ÷ E",8.4,RED,bold=True))
    for k in (100,200): s.append(f'<line x1="{k}" y1="4" x2="{k}" y2="72" stroke="#bbb" stroke-width="0.5"/>')
    return svg(300,74,"".join(s))

def fig_binom():
    s=[]; n=10; xs=[104+i*18.6 for i in range(n+1)]
    s.append(T(96,8,"n = 10 · the phrase →",7.6,BLUE,anchor="end",italic=True)); s.append(T(200,8,"filled dots = the x values you add up",7.6,BLUE))
    rows=[("fewer than 3 (< 3)",lambda x:x<3),("at most 3 (≤ 3)",lambda x:x<=3),("more than 3 (> 3)",lambda x:x>3),("at least 3 (≥ 3)",lambda x:x>=3)]
    y=24
    for lab,f in rows:
        s.append(T(96,y+3,lab,8.4,"#000",anchor="end",bold=True))
        s.append(f'<line x1="{xs[0]}" y1="{y}" x2="{xs[-1]}" y2="{y}" stroke="#999" stroke-width="0.6"/>')
        for i,x in enumerate(xs):
            if f(i): s.append(f'<circle cx="{x:.1f}" cy="{y}" r="3.4" fill="{RED}" stroke="{RED}"/>')
            else: s.append(f'<circle cx="{x:.1f}" cy="{y}" r="3.0" fill="#fff" stroke="#999" stroke-width="0.7"/>')
            if y==24: s.append(T(x,y-7,str(i),7.4,"#000"))
        y+=13
    s.append(T(150,y+1,"fewer than / more than → the number itself is OUT",7.4,RED,bold=True))
    s.append(T(150,y+10,"at most / at least → the number is IN · many dots filled → 1 − P(the empty dots)",7.4,RED,bold=True))
    return svg(300,y+14,"".join(s))

ALL={"bells":fig_bells,"back":fig_back,"emp":fig_emp,"uniform":fig_uniform,"discrete":fig_discrete,"venn":fig_venn,"binom":fig_binom}
if __name__=="__main__":
    body="".join(f"<h4>{k}</h4>{f()}" for k,f in ALL.items())
    open("figs_preview2.html","w").write(f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
body{{font-family:Helvetica,Arial,sans-serif;font-size:7.1pt;margin:10px;width:189pt}} h4{{margin:6px 0 2px 0;font-size:8pt;color:#999}}
.fig{{break-inside:avoid;margin:1.5pt 0 2.5pt 0;border:0.3pt dotted #ccc}} .fig svg{{width:100%;height:auto;display:block}}
</style></head><body>{body}</body></html>""")
    print("ok")
