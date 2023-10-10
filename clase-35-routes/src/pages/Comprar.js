import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import axios from "axios";

const Comprar = () => {

    const params = useParams("");
    const navigate = useNavigate();
    const [producto, setProducto] = useState({})
    useEffect(() => {
        axios.get("http://localhost:3001/productos/" + params.id).then((resp) => {
            setProducto(resp.data);
        })
    }, []);

    return (<div>
        <h3 className="alert alert-info shadow text-center mb-2 mt-3">Datos del producto a comprar</h3>
        <div className="text-center">
            <h4>{producto.nombre}</h4>
            <p className="m-3">
                {producto.descripcion}
            </p>
            <h4>
                {producto.precio}
            </h4>
        </div>

        <button className="btn btn-primary w-100" onClick={()=>{
            navigate(-1);
        }}>
            Confirmar Compra
        </button>
    </div>);
}

export default Comprar;