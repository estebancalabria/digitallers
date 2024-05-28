import { configureStore } from "@reduxjs/toolkit";
import axios from "axios";
import { ACT_INIT_STORE, ACT_ADD } from "../actions/action-types";


const store = configureStore({
    reducer : (state,action) => {
        let newState = {...state};

        (action.type===ACT_INIT_STORE) && (newState.ia = action.payload);
        (action.type===ACT_ADD) && (newState.ia = [...state.ia, action.payload]);

        return newState;
    },
    preloadedState : {
        ia : []
    }
});



axios.get("http://localhost:3001/ia").then((resp)=>{
    store.dispatch({
        type : ACT_INIT_STORE,
        payload : resp.data
    });
})


export default store;