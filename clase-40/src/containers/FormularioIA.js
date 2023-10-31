import { useNavigate } from "react-router-dom";
import { ACT_ADD } from "../actions/action-types";
import { useDispatch } from "react-redux";
import axios from "axios";
import Formulario from "../components/Formulario";




const FormularioIA = () => {

    const dispatch = useDispatch();
    const navigate = useNavigate();

    return (<Formulario
        titulo="Herramienta IA"
        campos={["nombre", "url", "tematica"]} 
        onSubmit={(elem)=>{
            axios.post("http://localhost:3001/ia", elem).then((resp)=>{
                let accion = {
                    type : ACT_ADD,
                    payload : resp.data
                };
                dispatch(accion);
                navigate(-1);
            })
        }}/>);
}
 
export default FormularioIA;