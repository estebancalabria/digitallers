import { configureStore } from "@reduxjs/toolkit";


export default configureStore({
    reducer : (s,a) => s,
    preloadedState : {
        libros : [
            {id:1 , nombre: "The Witcher", autor: "Andrzej Sapkowski"},
            {id:2 , nombre: "Los Juegos del Hambre", autor: "Suzana Collins"},
            {id:3 , nombre: "Moby Dick", autor: "Herman Melville"},
        ]
    }
})