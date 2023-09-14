

/*
var contador = 0;

function incrementar() {
    contador++;
}

function decrementar() {
    contador--;
}

function mostrarContador() {
    document.getElementById("veces").innerHTML = contador;
}  */

//IIFE :  Inmediatly Invoked Function Expression
(function (){
    "use strict";
    let contador = 0;

    function incrementar() {
        contador++;
    }

    function decrementar() {
        contador--;
    }

    function mostrarContador(elem) {
        //document.getElementById("veces").innerHTML = contador;
        elem.innerHTML = contador;
    }  

    //Exportacion del modulo
    window.counter = {
        inc : incrementar,
        dec : decrementar,
        showIn : mostrarContador
    }
})();