import { useDispatch } from "react-redux";
import { ACT_INCREMENTAR } from "../../actions/action-types";
import Boton from "../componets/Boton";

const Incrementar = () => {

    const dispatch = useDispatch();

    return (<Boton texto="+"
        onClick={() => {
            //va a hacer llegar la accion al reducer
            dispatch({
                type : ACT_INCREMENTAR
            })
        }} />);
}

export default Incrementar;