import { configureStore } from "@reduxjs/toolkit";
import reducer from "../reducer/reducer";

export default configureStore({
    reducer : reducer,
    preloadedState : {
        tareas :[
            {
              id: 1,
              accion: "Dominio del mundo",
              done: false,
            },
            {
              id: 2,
              accion: "Cardio",
              done: false,
            },
            {
              id: 3,
              accion: "Golpear a lenny en la nuca xD",
              done: false,
            },
          ],
    }
})