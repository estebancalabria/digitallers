import "bootstrap/dist/css/bootstrap.css";
import "./App.css"
import logo from "./logo.svg"

function App() {

  let titulo = "Bienvenidos a React";

  let contenedor = {
    backgroundColor: "lightgrey",
    padding: "2em",
    minHeight: "100vh",
    textAlign: "center"
  }

  /*let caracteristicasReact = [
    <li key="titulo" className="list-group-item active">React es...</li>,
    <li key={1} className="list-group-item">Prolijo</li>,
    <li key={2} className="list-group-item">Ordenado</li>,
    <li key={3} className="list-group-item">Completo</li>,
    <li key={4} className="list-group-item">Amigable</li>,
    <li key={5} className="list-group-item">Me enamore &#10084;&#65039;</li>
  ];*/

  let caracteristicasReact = ["Prolijo", "Ordenado", "Completo", "Amigable"];

  return (
    <div>
      <header className="alert alert-info text-center shadow mb-0">
        <h1>
          <img className="girar" src={logo} alt="Logo de React" style={{ height: "80px" }} />
          {titulo}
          <img className="girar" src={logo} alt="Logo de React" style={{ height: "80px" }} />
        </h1>
      </header>
      <main style={contenedor}>
        <h3>Bienvendos! </h3>
        <ul className="list-group w-50 mx-auto shadow">
          <li key="titulo" className="list-group-item active">React es...</li>
          {
            caracteristicasReact.map((c) => (<li key={c} className="list-group-item">{c}</li>))
          }
        </ul>
      </main>
      <footer className="bg-dark text-light text-end fixed-bottom p-3 shadow">
        CopyRight&copy;2023 EducacionIT. Todos los derechos reservados.
      </footer>
    </div>
  );
}

export default App;
