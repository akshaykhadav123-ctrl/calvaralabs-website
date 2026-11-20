// Calvara website enquiry log.
// Paste into the Google Sheet "Calvara website enquiries": Extensions > Apps Script, replace everything, Save,
// then Deploy > New deployment > type "Web app" > Execute as: Me > Who has access: Anyone > Deploy.
// Copy the Web app URL and give it to Claude (it goes into LOG_URL in source/build.py).

function doPost(e) {
  var p = (e && e.parameter) || {};
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
  var clean = function (v) { v = String(v || ''); return /^[=+\-@]/.test(v) ? "'" + v : v.slice(0, 2000); };
  sheet.appendRow([
    new Date(), clean(p.source), clean(p.name), clean(p.company), clean(p.phone), clean(p.email),
    clean(p.product), clean(p.grade), clean(p.request), clean(p.quantity), clean(p.application),
    clean(p.delivery), clean(p.packing), clean(p.message), clean(p.page), clean(p.lang)
  ]);
  return ContentService.createTextOutput('ok');
}
