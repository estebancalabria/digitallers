import { useSelector } from "react-redux";
import Contador from "../componets/Contador";


const ContadorHook = (props) => {

    const contador = useSelector(store => store.contador);

    return (<Contador valor={contador}>
        {props.children}
    </Contador>);
}
 
export default ContadorHook;