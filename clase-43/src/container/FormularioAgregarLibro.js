import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import Formulario from "../components/Formulario";
import crearAccion from "../redux/action-creators"

const FormularioAgregarLibro = () => {

    const dispatch = useDispatch();
    const navigate = useNavigate();

    return (<Formulario
           campos={["nombre", "autor"]}
           onSubmit={(librito)=>{
            let accion = crearAccion.agregarLibro(librito);
            dispatch(accion);
            navigate(-1);
           }}/>
     );
}
 
export default FormularioAgregarLibro;