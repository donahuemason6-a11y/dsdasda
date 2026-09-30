/* =====================================================================
   TouchGrass Music Fest · schedule data

   This is the only file you need to touch to update the schedule.
   - Times are 24-hour "HH:MM" in the festival's local time zone.
   - Add, remove or reorder sets freely; the page sorts them itself.
   - Stage colors and names live in the "stages" list.
   ===================================================================== */
window.FESTIVAL = {
  name: "TouchGrass Music Fest",
  dateLabel: "Saturday, October 3, 2026",
  date: "2026-10-03",             // YYYY-MM-DD. On this day the page shows the live "Right now" bar.
  timeZone: "America/New_York",   // IANA time zone the festival runs in
  venue: "Orlando Amphitheater",
  city: "Orlando, FL",
  dayStart: "12:00",              // first hour shown on the timeline
  dayEnd: "23:00",                // last hour shown on the timeline
  note: "Set times subject to change.",

  stages: [
    { id: "touch-grass", name: "Touch Grass Stage", short: "Touch Grass", color: "#c9ff3f" },
    { id: "meadows",     name: "Meadows Stage",     short: "Meadows",     color: "#6cf2bb" }
  ],

  sets: [
    /* ---------- Touch Grass Stage ---------- */
    { stage: "touch-grass", artist: "Zay of the Zoo",  start: "12:20", end: "12:30" },
    { stage: "touch-grass", artist: "DJ PeeWee",       start: "12:35", end: "13:35" },
    { stage: "touch-grass", artist: "Bizzy Crook",     start: "13:40", end: "14:00" },
    { stage: "touch-grass", artist: "TiaCorine",       start: "14:05", end: "14:35" },
    { stage: "touch-grass", artist: "Cochise",         start: "14:40", end: "15:10" },
    { stage: "touch-grass", artist: "DDG",             start: "15:15", end: "15:45" },
    { stage: "touch-grass", artist: "Chris Patrick",   start: "16:00", end: "16:35" },
    { stage: "touch-grass", artist: "Flo Milli",       start: "17:05", end: "17:35" },
    { stage: "touch-grass", artist: "Monaleo",         start: "18:05", end: "18:40" },
    { stage: "touch-grass", artist: "Aminé",           start: "19:10", end: "19:45" },
    { stage: "touch-grass", artist: "JID",             start: "20:00", end: "20:45" },
    { stage: "touch-grass", artist: "PARTYNEXTDOOR",   start: "21:45", end: "22:45" },

    /* ---------- Meadows Stage ---------- */
    { stage: "meadows", artist: "DJ Jynn",                        start: "12:45", end: "13:15" },
    { stage: "meadows", artist: "Cherele",                        start: "13:20", end: "13:40" },
    { stage: "meadows", artist: "Trap Sushi",                     start: "13:45", end: "14:15" },
    { stage: "meadows", artist: "Lizzy Ashleigh",                 start: "14:20", end: "14:45" },
    { stage: "meadows", artist: "Bae Brigade Battle",             start: "14:50", end: "15:50" },
    { stage: "meadows", artist: "Adamn Killa & Fiji_Slayed_May",  start: "15:55", end: "16:15" },
    { stage: "meadows", artist: "Trim",                           start: "16:20", end: "16:40" },
    { stage: "meadows", artist: "Girls Love Karaoke",             start: "16:45", end: "17:45" },
    { stage: "meadows", artist: "Sosocamo",                       start: "17:55", end: "18:20" },
    { stage: "meadows", artist: "Wynne",                          start: "18:30", end: "19:05" },
    { stage: "meadows", artist: "Jenevieve",                      start: "19:15", end: "19:55" },
    { stage: "meadows", artist: "Armani White",                   start: "20:15", end: "20:55" },
    { stage: "meadows", artist: "Slayr",                          start: "21:10", end: "21:45" }
  ]
};
