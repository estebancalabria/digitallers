
/*var contador = 0;
let timerId = 0;

function iniciar(){
    if (timerId===0){
        timerId = setInterval(()=>{ 
            contador++; 
            mostarTimer();
        }, 1000)
    }
}

function detener(){
    clearInterval(timerId);
    timerId = 0;
}

function mostarTimer(){
    document.getElementById("segundos").innerHTML = contador;
}*/

(function(){
    "use strict";
    let contador = 0;
    let timerId = 0;
    let showInElem = null;
    
    function iniciar(){
        if (timerId===0){
            timerId = setInterval(()=>{ 
                contador++; 
                //En breve lo mejoramos
                /*if (showInElem){
                    showInElem.innerHTML = contador;
                }*/

                //Una manera mejor con un "one liner" para mandarnos la parte de javascript
                showInElem && (showInElem.innerHTML = contador);

                //Otro one liner mejor ===> No me funciono! Tiene que estar del otro lado del igual
                //showInElem?.innerHTML = contador;
            }, 1000)
        }
    }
    
    function detener(){
        clearInterval(timerId);
        timerId = 0;
    }
    
    function showIn(elem){
        //elem.innerHTML = contador;
        showInElem = elem;
    }

    window.timer = {
        init : iniciar,
        stop : detener,
        showIn : showIn
    }
})();