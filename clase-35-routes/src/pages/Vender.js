import "bootstrap/dist/css/bootstrap.css";
import axios from "axios";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const Vender = () => {

    const [nombre, setNombre] = useState("");
    const [descripcion, setDescripcion] = useState("");
    const [precio, setPrecio] = useState(0);

    const navigate = useNavigate();

    return (<div>
        <h3 className="alert alert-info mb-3 mt-2 shadow">
            Datos del Producto a Vender
        </h3>
        <form className="p-4 shadow rouded-1">
            Nombre:
            <input type="text" className="form-control" onChange={(evt)=>{
                setNombre(evt.target.value);
            }}/>
            Descripcion:
            <textarea className="form-control" onChange={(evt=>{
                setDescripcion(evt.target.value);
            })}/>
            Precio:
            <input type="number" className="form-control" onChange={(evt)=>{
                setPrecio(evt.target.valueAsNumber);
            }}/>
            
            <button className="btn btn-primary w-100 mt-4" onClick={()=>{
                axios.post("http://localhost:3001/productos", {
                    nombre,  //es lo mismo que poner nombre:nombre
                    descripcion,
                    precio
                }).then(()=>{
                    navigate("/productos");
                })
            }}>
                Vender
            </button>
        </form>
    </div>);
} 
 
export default Vender;