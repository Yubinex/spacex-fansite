

function startTime() {

  const today = new Date();
  
  let hour = today.getHours();
  let min = today.getMinutes();
  let sec = today.getSeconds();

  min = checkTime(min);
  sec = checkTime(sec);

  document.getElementById('clock').innerHTML =  hour + ":" + min + ":" + sec;
  setTimeout(startTime, 1000);

}

function checkTime(i) {

  if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
  return i;

}