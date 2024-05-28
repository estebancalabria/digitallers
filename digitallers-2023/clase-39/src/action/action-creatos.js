import * as types from "./action-types";

const creadorAcciones = {

    agregarTarea : (nombre) => ({type : types.ACT_AGREGAR , nombre : nombre}),
    eliminarTarea : (id) =>({type : types.ACT_ELIMINAR , id : id}),
    realizarTarea :  (id) => ({ type: types.ACT_REALIZAR, id: id })

}

export default creadorAcciones;