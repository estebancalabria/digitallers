import "bootstrap/dist/css/bootstrap.css";
import Swal from "sweetalert2";

//
//  Opcion 1: Recibiendo el objeto props
//            La opcion mas comun. El parametro puede llamarse de cualquier manera pero por convencion
//            le llamamos props.
//
/*function Encabezado(props) {
    //alert(JSON.stringify(props));

    return (<header className="alert alert-info text-center">
        <h1>{props.titulo}</h1>
        <h2>{props.subtitulo}</h2>
    </header>);
}*/

//
//  Opcion 2 : Deconstruyendo las props
//             De esta manera me ahorro de escribir props. en todos lados
//
/*function Encabezado(props) {
    const {titulo, subtitulo} = props;

    return (<header className="alert alert-info text-center">
        <h1>{titulo}</h1>
        <h2>{subtitulo}</h2>
    </header>);
}*/

//
// Opcion 3 : Desreferencio parametros
//            Documenta que parametros necesitamos con solo ver la firma del metodo
//
function Encabezado({titulo, subtitulo, imagen}) {
    return (<header className="alert alert-info text-center">
        { imagen && <img src={imagen} alt="titulo" className="float-start" style={{height: "100px"}} /> }
        
        <button className="btn btn-primary float-end" onClick={()=>{
            Swal.fire("La hora actual es", new Date().toLocaleString());
        }}>
            &#9200;
        </button>

        <h1>{titulo}</h1>
        <h2>{subtitulo}</h2>
    </header>);
}


export default Encabezado;