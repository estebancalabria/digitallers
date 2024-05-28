import "bootstrap/dist/css/bootstrap.css";
import Cabecera from "./components/Cabecera";
import * as Bs from "react-bootstrap";
import TodoList from "./components/TodoList";

function App() {
  return (
    <div>
      <Cabecera titulo="Bienvenidos Digitalers" subtitulo="Ahora la Todo List en React" />
      <Bs.Container>
        <TodoList
          titulo="Lista de Platos"
          tareas={[
            { id: 1, nombre: "Pizza", done: true },
            { id: 2, nombre: "Hamburguesa", done: false },
            { id: 3, nombre: "Asado", done: false }]} />
      </Bs.Container>
    </div>
  );
}

export default App;
