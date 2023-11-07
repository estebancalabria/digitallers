import { configureStore } from "@reduxjs/toolkit";

const ACT_ADD_LIBRO = 'ACT_ADD_LIBRO';

function reducer(state, action) {
    let newState = {...state};

    switch (action.type) {
        case ACT_ADD_LIBRO:
            newState.libros = [
                ...newState.libros,
                action.payload
            ]
            break;
    
        default:
            break;
    }

    return newState;
}


export default configureStore({
    reducer : reducer,
    preloadedState : {
        libros : [
            {id:1 , nombre: "The Witcher", autor: "Andrzej Sapkowski"},
            {id:2 , nombre: "Los Juegos del Hambre", autor: "Suzana Collins"},
            {id:3 , nombre: "Moby Dick", autor: "Herman Melville"},
        ]
    }
})