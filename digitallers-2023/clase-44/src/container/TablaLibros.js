import { useDispatch, useSelector } from "react-redux";
import Tabla from "../components/Tabla";
import crearAccion from "../redux/action-creators";
import Swal from "sweetalert2";
import { useNavigate } from "react-router-dom";


const TablaLibros = () => {
    const listaLibros = useSelector(state => state.libros);
    const dispatch = useDispatch();
    const navigate = useNavigate();

    return (<Tabla
        columnas={["nombre", "autor"]}
        items={listaLibros} 
        onEditar={(libro)=>{
            navigate("editar/" + libro.id);
        }}
        onEliminar={(libro)=>{
            //alert(`Se elimina el libro ${libro.id}`)
            Swal.fire({
                title : "Esta seguro de eliminar?",
                showCancelButton: true,
                icon : "warning"
            }).then((resp)=>{
                if (resp.isConfirmed){
                    let accion = crearAccion.eliminarLibro(libro.id);
                    dispatch(accion);
                }
            })
        }}/>);
}


export default TablaLibros;