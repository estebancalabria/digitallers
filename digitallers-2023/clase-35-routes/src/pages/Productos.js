import "bootstrap/dist/css/bootstrap.css";
import { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";


const Productos = () => {
    const navigate = useNavigate()

    const [productos, setProductos] = useState([]);
    useEffect(()=>{
        axios.get("http://localhost:3001/productos").then((resp)=>{
            setProductos(resp.data);
        })
    },[]);

    return (<div className="text-center">
        <h3 className="alert alert-info mt-3 shadow">Mis productos</h3>
        <div>
            <button className="btn btn-success float-end mb-2"
                onClick={()=>{navigate("/vender")}}>
                Vender!
            </button>
        </div>
        <div>
            <table className="table mt-2 border shadow">
                <thead>
                    <tr>
                        <th>Nombre</th>
                        <th>Descripcion</th>
                        <th>Precio</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                {
                    productos.map((prod)=>(
                        <tr key={prod.id}>
                            <td align="center" valign="middle">{prod.nombre}</td>
                            <td>{prod.descripcion}</td>
                            <td valign="middle">{prod.precio}</td>
                            <td valign="middle">
                                <button className="btn btn-primary float-end"
                                 onClick={()=>{
                                    navigate(`/comprar/${prod.id}`)
                                 }}>
                                    Comprar!
                                </button>
                            </td>
                        </tr>
                    ))
                }
                </tbody>
            </table>
        </div>
    </div>);
}
 
export default Productos;