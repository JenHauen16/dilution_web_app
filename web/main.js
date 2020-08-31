function calculate(){
  var array = document.getElementById('array').value;
  var startdil = document.getElementById('startdil').value;
  if (array === "Oncoscan") {
    eel.oshigh(startdil)(callBack);
  } else {
    eel.cshigh(startdil)(callBack);
  }
}


function callBack (result){
  document.getElementById('buffer').value=result
}
