import * as types from "../actions/action-types";


//La accion es un objeto json que tiene una propiedad type


function reducer(state, action) {
    let newState = { ...state };

    switch (action.type) {
        case types.ACT_INCREMENTAR:
            newState.contador = state.contador + 1;
            break;
        case types.ACT_DECREMENTAR:
            newState.contador = state.contador - 1;
            break;
        case types.ACT_RESET:
            newState.contador = 0;
            break;

        default:
            break;
    }

    return newState;
}

export default reducer;