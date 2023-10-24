import "bootstrap/dist/css/bootstrap.css";

const Contador = (props) => {
    return (<div className="alert alert-info text-center">
        <h1>Contador {props.valor}</h1>
        <div>
            {props.children}
        </div>
    </div>);
}
 
export default Contador;