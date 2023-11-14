import { configureStore } from "@reduxjs/toolkit";
import { ACT_ADD_LIBRO, ACT_ELI_LIBRO, ACT_INIT_LIBRO, ACT_MOD_LIBRO } from "./action-types";
import axios from "axios";


function reducer(state, action) {
    let newState = { ...state };

    switch (action.type) {
        case ACT_INIT_LIBRO:
            newState.libros = action.payload
            break;
        case ACT_ADD_LIBRO:
            newState.libros = [
                ...newState.libros,
                {
                    //id :  Math.max(...newState.libros.map(l=>l.id),0) + 1,
                    ...action.payload
                }
            ]
            break;
        case ACT_ELI_LIBRO:
            newState.libros =
                newState.libros
                    .filter(libro => libro.id !== action.payload);
            break
        case ACT_MOD_LIBRO :
            newState.libros = newState.libros
                .map(libro => ( (libro.id === action.payload.id) ? action.payload : libro )); 
            break;
        default:
            break;
    }

    return newState;
}


const store = configureStore({
    reducer: reducer,
    preloadedState: {
        libros: [
            /*{ id: 1, nombre: "The Witcher", autor: "Andrzej Sapkowski" },
            { id: 2, nombre: "Los Juegos del Hambre", autor: "Suzana Collins" },
            { id: 3, nombre: "Moby Dick", autor: "Herman Melville" },*/
        ]
    }
});

axios.get("http://localhost:3001/libros").then((resp)=>{
    store.dispatch({
        type : ACT_INIT_LIBRO,
        payload : resp.data
    })
});

export default store;