import "bootstrap/dist/css/bootstrap.css";
import Encabezado from "./components/Encabezado";
import PieDePagina from "./components/PieDePagina";
import logo from "./logo.svg";
import Lista from "./components/Lista";
import Titulo from "./components/Titulo";
import Swal from "sweetalert2";

function App() {
  return (
    <div>
      <Encabezado titulo="Digitalles con React" subtitulo="Bienvenidos a la clase 31" imagen={logo} />
      <main className="container">
        <Titulo texto="Milanga Go. Su Delivery preferido de milanesas" />
        <Lista 
          titulo="Tipos de Milanesa" 
          items={["Napolitana", "Pollo", "Carne", "Veggie", "Soja"]}
          onAccion={(item)=>{
            Swal.fire("Compra realizada", `Se agrego al carrito ${item}`)
          }}/>
      </main>
      <PieDePagina empresa="EducacionIT" disclaimer="Todos los derechos reservados" />
    </div>
  );
}

export default App;
