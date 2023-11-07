import { ACT_ADD_LIBRO } from "./action-types"

const crearAccion = {
    agregarLibro : (libro) => ({
        type : ACT_ADD_LIBRO,
        payload : libro
    })
}

export default crearAccion;