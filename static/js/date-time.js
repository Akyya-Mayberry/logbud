/* Controls the date and time clock displayed */

'use strict';
function startTime() {
  var today = new Date();

  // The date
  var date = today.toDateString();
  document.getElementById('date').innerHTML = date

  // The time
  var h = today.getHours()
  var amPm = h > 11 ? 'pm' : 'am';

  // Convert time to non-military
  h = (h + 24) % 12 || 12;

  var m = today.getMinutes();
  var s = today.getSeconds();
  m = checkTime(m);
  s = checkTime(s);

  document.getElementById('txt').innerHTML =
  h + ":" + m + ":" + s + amPm;

  // Keep time and date updated
  var t = setTimeout(startTime, 500);
}

function checkTime(i) {
  if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
  return i;
}
