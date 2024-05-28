import * as types from "../action/action-types";

function reducer(state, action) {
    let newState = { ...state };

    switch (action.type) {
        case types.ACT_AGREGAR:
            newState.tareas = [
                ...state,
                {
                    id: Math.max(...state.tareas.map((t) => (t.id)), 0) + 1,
                    accion: action.nombre,
                    done: false
                }
            ]
            break;
        case types.ACT_ELIMINAR:
            newState.tareas = newState.tareas.filter((item) => (item.id !== action.id));
            break;

        case types.ACT_REALIZAR:
            newState.tareas.forEach(t => {
                (t.id===action.id) && (t.done = !t.done);
            });
            break;

        default:
            break;

    }


    return newState;
}

export default reducer;