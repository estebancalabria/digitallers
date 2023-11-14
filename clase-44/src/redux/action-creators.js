import axios from "axios"
import { ACT_ADD_LIBRO, ACT_ELI_LIBRO, ACT_MOD_LIBRO } from "./action-types"


/*const crearAccion = {
    agregarLibro : (libro) => ({
        type : ACT_ADD_LIBRO,
        payload : libro
    }),
    eliminarLibro : (id) =>({
        type : ACT_ELI_LIBRO,
        payload : id
    }),
    modificarLibro : (libro) => ({
        type : ACT_MOD_LIBRO,
        payload : libro
    })

}*/

//Reescribo los action creators para que funcionen con llamadas asyn
const crearAccion = {
    agregarLibro: (libro) => (dispatch) => {
        axios.post("http://localhost:3001/libros", libro).then((resp) => {
            dispatch({
                type: ACT_ADD_LIBRO,
                payload: resp.data
            });
        })
    },
    eliminarLibro: (id) => (dispatch) => {
        axios.delete("http://localhost:3001/libros/" + id).then((resp) => {
            dispatch({
                type: ACT_ELI_LIBRO,
                payload: id
            })
        })
    },
    modificarLibro: (libro) => (dispatch) => {
        axios.put("http://localhost:3001/libros/" + libro.id, libro).then((resp) => {
            dispatch({
                type: ACT_MOD_LIBRO,
                payload: libro
            });

        })
    }
}

export default crearAccion;