var select = document.querySelector("select");
var html = document.querySelector("html");
document.body.style.padding = '10px';

function update(bgColor, txtColor) {
    html.style.backgroundColor = bgColor;
    html.style.color = txtColor;
}

//function setTheme() {
//    (localStorage.getItem("selectedChoice") === 'black') ? update("black", "white") : update("white", "black");
//}

select.onchange = function () {
 localStorage.setItem("selectedChoice", select.value);
 (localStorage.getItem("selectedChoice") === 'black') ? update("black", "white") : update("white", "black");
}

console.log(localStorage.getItem("selectedChoice"));

//if (localStorage.getItem("selectedChoice") === "black") {
//  update("black", "white");
//} else {
//  update("white", "black");
//}

function setUserTheme() {
if (localStorage.getItem("selectedChoice") === "black") {
     select.value = "black";
     update("black", "white");
   } else {
     select.value = "white";
     update("white", "black");
   }
 }

setUserTheme();
console.log(localStorage.getItem("selectedChoice"));
