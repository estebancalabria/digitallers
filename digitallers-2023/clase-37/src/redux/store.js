import { configureStore } from "@reduxjs/toolkit";

export default configureStore({
    reducer : (s,a) => (s),
    preloadedState : { noticias : [
        {"id":1, "titulo":"El desafio de redux", "contenido": "Veremos esta libreria de react para implementar el patron de arquitectura FLUX"},
        {"id":2, "titulo":"Redux vs ContextAPI", "contenido": "Cual me conviene usar y cuando?"},
        {"id":3, "titulo":"Props Drilling", "contenido": "Las soluciones clasicas son muchas veces desestimadas pero son buenas"},
        {"id":4, "titulo":"Experto en React", "contenido": "Conviertase en experto en React con esas librerias mas react-router-dom"}
    ]}
});