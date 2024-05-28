import "bootstrap/dist/css/bootstrap.css";
import Cabecera from "./components/Cabecera";
import { BrowserRouter, Link, Route, Routes } from "react-router-dom";
import Inicio from "./pages/Inicio";
import Productos from "./pages/Productos";
import Contacto from "./pages/Contacto";
import Comprar from "./pages/Comprar";
import Vender from "./pages/Vender";

function App() {
  return (
    <BrowserRouter>
      <Cabecera titulo="Digitallers E-Commerce" subtitulo="La major app de ventas de react" />
      <nav>
        <ul className="nav bg-dark">
          <li className="nav-item">
            <Link className="nav-link" to="/">Inicio</Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link" to="/productos">Productos</Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link" to="/contacto">Contacto</Link>
          </li>
        </ul>
      </nav>
      <main className="container">
        <Routes>
          <Route path="/" element={<Inicio />} />
          <Route path="/productos" element={<Productos />} />
          <Route path="/contacto" element={<Contacto />} />
          <Route path="/comprar/:id" element={<Comprar />} />
          <Route path="/vender" element={<Vender />} />
        </Routes>

      </main>
    </BrowserRouter>
  );
}

export default App;
