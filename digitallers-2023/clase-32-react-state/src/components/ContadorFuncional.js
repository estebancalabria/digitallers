import "bootstrap/dist/css/bootstrap.css";
import { useState } from "react";

function ContadorFuncional() {

    //En react, las variable de los componentes que se muestran (como este caso)
    //Son variables que si cambian quiero que se refresque el componente para reflejar visualmente el cambio
    //Estas variables se llaman "variables de estado" y se declaran de una manera particular...
    //Son variables que se declaran unando "hooks", en particular el hook useState
    const [contador, setContador] = useState(0);

    function resetContador(){
        setContador(0);
    }

    return (<div className="text-center border p-3 m-2 shadow">
        <h3>Contador Funcional {contador}</h3>
        <div>
            {/*Opcion 1 : Evento con funcion anonima */}
            <button className="btn btn-primary me-2" onClick={function(){
                (contador>0) && setContador(contador - 1);
            }}>
                -
            </button>

            {/*Opcion 2: Evento con funcion con nombre (flecha o tradicionaal) */}
            <button className="btn btn-danger" onClick={resetContador}>
                Reset
            </button>

            {/* Opcion 3 : Evento con funcion flecha => */}
            <button className="btn btn-primary ms-2" onClick={()=>{
                setContador(contador + 1);
            }}>
                +
            </button>
        </div>
    </div>);
}

export default ContadorFuncional;

