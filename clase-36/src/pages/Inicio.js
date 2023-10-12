import "bootstrap/dist/css/bootstrap.css";
import pelis from "../pelis.jpg";

const Inicio = () => {
    return (<div className="m-3 text-center">
        <h1 className="alert alert-info">
            Bienvenidos a mi base de datos de pelis
        </h1>
        <img style={{width:"100%"}} src={pelis} alt="Logo Pelis" />
    </div>   
    );
}
 
export default Inicio;