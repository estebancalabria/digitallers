import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams } from "react-router-dom";
import Formulario from "../components/Formulario";
import crearAccion from "../redux/action-creators";

const FormularioEditarLibro = () => {

    const params = useParams();
    const libro = useSelector
    // eslint-disable-next-line
        (state => state.libros.filter(libro => libro.id == params.id)[0]);
    const dispatch = useDispatch();
    const navigate = useNavigate();

    return (<Formulario 
        campos={["nombre","autor"]}
        item={libro}
        onSubmit={(libroModificado)=>{
            let accion = crearAccion.modificarLibro(libroModificado);
            dispatch(accion);
            navigate(-1);
        }}
    />);
}

export default FormularioEditarLibro;