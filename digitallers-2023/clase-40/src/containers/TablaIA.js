import { useSelector } from "react-redux";
import Tabla from "../components/Tabla";

const TablaIA = () => {

    const listaIA = useSelector(state=>state.ia);

    return (<Tabla 
        items={listaIA}
        columnas={["nombre","url","tematica"]}
    />);
}
 
export default TablaIA;