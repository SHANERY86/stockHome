
  // Your web app's Firebase configuration
  var firebaseConfig = {
    apiKey: "AIzaSyAp3AZ-qdiCMxAYqeDMplNviTJhdB4k1M4",
    authDomain: "sensepi-c7a8f.firebaseapp.com",
    databaseURL: "https://sensepi-c7a8f.firebaseio.com",
    projectId: "sensepi-c7a8f",
    storageBucket: "sensepi-c7a8f.appspot.com",
    messagingSenderId: "621385355482",
    appId: "1:621385355482:web:926e3d473a6cbca63755e3"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);

var potatoesRef = firebase.database().ref("potatoes");
var coffeeRef = firebase.database().ref("coffee");
var sugarRef = firebase.database().ref("sugar");

var potatoFullStock = 3000;
var coffeeFullStock = 300;
var sugarFullStock = 600;

var potatoesWeight = potatoesRef.once("value").then(function(snapshot) {
    var potatoesData = snapshot.val();
var potatoesPercentLeft = Math.round((potatoesData.weight/potatoFullStock)*100*10)/10;
var Time = new Date();
var dateandtime = Time.toLocaleString();
 document.getElementById("potatoesWeight").innerHTML=potatoesData.weight;
  document.getElementById("potatoTime").innerHTML=dateandtime;
  document.getElementById("potatoPercent").innerHTML=potatoesPercentLeft;
}); 

var coffeeWeight = coffeeRef.once("value").then(function(snapshot) {
    var coffeeData = snapshot.val();
var coffeePercentLeft = Math.round((coffeeData.weight/coffeeFullStock)*100*10)/10;
var time = new Date();
var dateandtime = time.toLocaleString();
 document.getElementById("coffeeWeight").innerHTML=coffeeData.weight;
  document.getElementById("coffeeTime").innerHTML=dateandtime;
  document.getElementById("coffeePercent").innerHTML=coffeePercentLeft;
}); 

var sugarWeight = sugarRef.once("value").then(function(snapshot) {
    var sugarData = snapshot.val();
var sugarPercentLeft = Math.round((sugarData.weight/sugarFullStock)*100*10)/10;
var time = new Date();
var dateandtime = time.toLocaleString();
 document.getElementById("sugarWeight").innerHTML=sugarData.weight;
  document.getElementById("sugarTime").innerHTML=dateandtime;
  document.getElementById("sugarPercent").innerHTML=sugarPercentLeft;
}); 
