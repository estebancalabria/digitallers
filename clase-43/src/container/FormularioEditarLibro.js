import { useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import Formulario from "../components/Formulario";

const FormularioEditarLibro = () => {

    const params = useParams();
    const libro = useSelector
        (state => state.libros.filter(libro => libro.id == params.id)[0]);


    return (<Formulario 
        campos={["nombre","autor"]}
        item={libro}
        onSubmit={(libroModificado)=>{
            alert("Se modifica el libro" + JSON.stringify(libroModificado))
        }}
    />);
}

export default FormularioEditarLibro;