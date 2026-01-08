const mensaje = document.getElementById("mensaje");
const button1 = document.getElementById("bt1");
const button2 = document.getElementById("bt2");


button1.addEventListener("click",function(){
mensaje.textContent = "Bienvenido a mi primera paguina web";
})

button2.addEventListener("click",function(){
mensaje.textContent = "Welcome to my frist web page";
})