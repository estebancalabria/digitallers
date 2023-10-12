import { useState } from "react";
import { useNavigate } from "react-router-dom";

const NuevaPelicula = ({onAgregarPelicula}) => {
    const generos = ['Crimen', 'Drama', 'Acción', 'Aventura', 'Biografía', 'Animación', 'Comedia', 'Misterio', 'Guerra', 'Ciencia ficción', 'Acción'];

    const [nombre, setNombre] = useState("");
    const [año, setAño] = useState(new Date().getFullYear());
    const [genero, setGenero] = useState("");
    const navigate = useNavigate();

    return (<div>
             <h1 className="alert alert-info text-center mt-4">
                Nueva Pelicula
             </h1>
             <form>
                    Nombre:
                    <input className="form-control" type="text" 
                        onChange={(evt)=>{setNombre(evt.target.value)}}/>

                    Año
                    <input className="form-control" type="number" 
                        min={1985} 
                        max={new Date().getFullYear()} 
                        onChange={(evt)=>{setAño(evt.target.valueAsNumber)}}/>

                    Genero
                    <select className="form-select">
                        <option selected>Elija el genero...</option>
                        {
                            [...new Set(generos)].sort().map((g)=>(
                                <option key={g} value={g}>{g}</option>
                            ))
                        }
                    </select>

                    <button type="button" className="btn btn-primary mt-4 w-100" onClick={()=>{
                        onAgregarPelicula({nombre,año,genero});
                        navigate(-1);
                    }}>
                        Agregar Pelicula En Memoria
                    </button>
             </form>
        </div>);
}
 
export default NuevaPelicula;