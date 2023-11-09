import { configureStore } from "@reduxjs/toolkit";
import { ACT_ADD_LIBRO, ACT_ELI_LIBRO, ACT_MOD_LIBRO } from "./action-types";


function reducer(state, action) {
    let newState = { ...state };

    switch (action.type) {
        case ACT_ADD_LIBRO:
            newState.libros = [
                ...newState.libros,
                {
                    id :  Math.max(...newState.libros.map(l=>l.id),0) + 1,
                    ...action.payload
                }
            ]
            break;
        case ACT_ELI_LIBRO:
            newState.libros =
                newState.libros
                    .filter(libro => libro.id !== action.payload);
            break
        default:
            break;
    }

    return newState;
}


export default configureStore({
    reducer: reducer,
    preloadedState: {
        libros: [
            { id: 1, nombre: "The Witcher", autor: "Andrzej Sapkowski" },
            { id: 2, nombre: "Los Juegos del Hambre", autor: "Suzana Collins" },
            { id: 3, nombre: "Moby Dick", autor: "Herman Melville" },
        ]
    }
})