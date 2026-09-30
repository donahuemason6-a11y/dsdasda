/* =====================================================================
   TouchGrass Music Fest · schedule data

   This is the only file you need to touch to update the schedule.
   - Times are 24-hour "HH:MM" in the festival's local time zone.
   - Add, remove or reorder sets freely; the page sorts them itself.
   - Stage colors and names live in the "stages" list.
   - "photo" is optional: put the image in img/ and reference it here.
   ===================================================================== */
window.FESTIVAL = {
  name: "TouchGrass Music Fest",
  dateLabel: "Saturday, October 3, 2026",
  dateShort: "Sat Oct 3, 2026",
  date: "2026-10-03",             // YYYY-MM-DD. On this day the page shows the live "Right now" bar.
  timeZone: "America/New_York",   // IANA time zone the festival runs in
  venue: "Orlando Amphitheater",
  city: "Orlando, FL",
  startTime: "12:00",             // music starts; the countdown runs to this moment on "date"
  dayStart: "12:00",              // first hour shown on the timeline
  dayEnd: "23:00",                // last hour shown on the timeline
  note: "Set times subject to change.",

  /* Artist photos: drop a JPG/PNG into the img/ folder and point "photo" at it below.
     Square-ish crops look best. If the file is missing the page shows a monogram tile instead. */

  stages: [
    { id: "touch-grass", name: "Touch Grass Stage", short: "Touch Grass", color: "#c9ff3f" },
    { id: "meadows",     name: "Meadows Stage",     short: "Meadows",     color: "#6cf2bb" }
  ],

  sets: [
    /* ---------- Touch Grass Stage ---------- */
    { stage: "touch-grass", artist: "Zay of the Zoo",  start: "12:20", end: "12:30", photo: "img/zay-of-the-zoo.jpg" },
    { stage: "touch-grass", artist: "DJ PeeWee",       start: "12:35", end: "13:35", photo: "img/dj-peewee.jpg" },
    { stage: "touch-grass", artist: "Bizzy Crook",     start: "13:40", end: "14:00", photo: "img/bizzy-crook.jpg" },
    { stage: "touch-grass", artist: "TiaCorine",       start: "14:05", end: "14:35", photo: "img/tiacorine.jpg" },
    { stage: "touch-grass", artist: "Cochise",         start: "14:40", end: "15:10", photo: "img/cochise.jpg" },
    { stage: "touch-grass", artist: "DDG",             start: "15:15", end: "15:45", photo: "img/ddg.jpg" },
    { stage: "touch-grass", artist: "Chris Patrick",   start: "16:00", end: "16:35", photo: "img/chris-patrick.jpg" },
    { stage: "touch-grass", artist: "Flo Milli",       start: "17:05", end: "17:35", photo: "img/flo-milli.jpg" },
    { stage: "touch-grass", artist: "Monaleo",         start: "18:05", end: "18:40", photo: "img/monaleo.jpg" },
    { stage: "touch-grass", artist: "Aminé",           start: "19:10", end: "19:45", photo: "img/amine.jpg" },
    { stage: "touch-grass", artist: "JID",             start: "20:00", end: "20:45", photo: "img/jid.jpg" },
    { stage: "touch-grass", artist: "PARTYNEXTDOOR",   start: "21:45", end: "22:45", photo: "img/partynextdoor.jpg" },

    /* ---------- Meadows Stage ---------- */
    { stage: "meadows", artist: "DJ Jynn",                        start: "12:45", end: "13:15", photo: "img/dj-jynn.jpg" },
    { stage: "meadows", artist: "Cherele",                        start: "13:20", end: "13:40", photo: "img/cherele.jpg" },
    { stage: "meadows", artist: "Trap Sushi",                     start: "13:45", end: "14:15", photo: "img/trap-sushi.jpg" },
    { stage: "meadows", artist: "Lizzy Ashleigh",                 start: "14:20", end: "14:45", photo: "img/lizzy-ashleigh.jpg" },
    { stage: "meadows", artist: "Bae Brigade Battle",             start: "14:50", end: "15:50", photo: "img/bae-brigade-battle.jpg" },
    { stage: "meadows", artist: "Adamn Killa & Fiji_Slayed_May",  start: "15:55", end: "16:15", photo: "img/adamn-killa-fiji-slayed-may.jpg" },
    { stage: "meadows", artist: "Trim",                           start: "16:20", end: "16:40", photo: "img/trim.jpg" },
    { stage: "meadows", artist: "Girls Love Karaoke",             start: "16:45", end: "17:45", photo: "img/girls-love-karaoke.jpg" },
    { stage: "meadows", artist: "Sosocamo",                       start: "17:55", end: "18:20", photo: "img/sosocamo.jpg" },
    { stage: "meadows", artist: "Wynne",                          start: "18:30", end: "19:05", photo: "img/wynne.jpg" },
    { stage: "meadows", artist: "Jenevieve",                      start: "19:15", end: "19:55", photo: "img/jenevieve.jpg" },
    { stage: "meadows", artist: "Armani White",                   start: "20:15", end: "20:55", photo: "img/armani-white.jpg" },
    { stage: "meadows", artist: "Slayr",                          start: "21:10", end: "21:45", photo: "img/slayr.jpg" }
  ]
};
