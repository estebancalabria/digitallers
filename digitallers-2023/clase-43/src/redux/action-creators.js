import { ACT_ADD_LIBRO, ACT_ELI_LIBRO } from "./action-types"

const crearAccion = {
    agregarLibro : (libro) => ({
        type : ACT_ADD_LIBRO,
        payload : libro
    }),
    eliminarLibro : (id) =>({
        type : ACT_ELI_LIBRO,
        payload : id
    })
}

export default crearAccion;