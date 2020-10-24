document.getElementById("btn__log-in").addEventListener("click", login);
document.getElementById("btn__register").addEventListener("click", register);
window.addEventListener("resize", widthPage);


//Declare variables
var container_login_register = document.querySelector(".container__login-register");
var formulario_login = document.querySelector(".form__login");
var formulario_register = document.querySelector(".form__register");
var back_box_login = document.querySelector(".back__box-login");
var back__box_register = document.querySelector(".back__box-register");

function widthPage(){
    if(window.innerWidth > 850){
        back_box_login.style.display="block";
        back__box_register.style.display = "block";
    }else{
        back__box_register.style.display = "block";
        back__box_register.style.opacity = "1";
        back_box_login.style.display = "none";
        formulario_login.style.display = "block";
        formulario_register.style.display = "none";
        container_login_register.style.left = "0px";
    }
}

widthPage();

function login(){
    if(window.innerWidth > 850){
        formulario_register.style.display = "none";
        container_login_register.style.left = "10px";
        formulario_login.style.display = "block";
        back__box_register.style.opacity = "1";
        back_box_login.style.opacity = "0";
    }else{
        formulario_register.style.display = "none";
        container_login_register.style.left = "0px";
        formulario_login.style.display = "block";
        back__box_register.style.display = "block";
        back_box_login.style.display = "none";
    }
}

function register(){
    if(window.innerWidth > 850){
    formulario_register.style.display = "block";
    container_login_register.style.left = "410px";
    formulario_login.style.display = "none";
    back__box_register.style.opacity = "0";
    back_box_login.style.opacity = "1";
    }else{
    formulario_register.style.display = "block";
    container_login_register.style.left = "0px";
    formulario_login.style.display = "none";
    back__box_register.style.display = "none";
    back_box_login.style.display = "block";
    back_box_login.style.opacity = "1";
    }

}