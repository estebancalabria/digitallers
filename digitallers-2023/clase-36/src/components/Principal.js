import "bootstrap/dist/css/bootstrap.css";
import { Route, Routes } from "react-router-dom";

const Principal = ({rutas}) => {
    return (<main className="container">
        <Routes>
            {
                rutas.map((ruta)=>(
                    <Route key={ruta.url} path={ruta.url} element={ruta.componente}></Route>
                ))
            }
        </Routes>
    </main>);
}
 
export default Principal;