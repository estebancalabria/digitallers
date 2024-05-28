import { Provider } from "react-redux";
//import Lista from "./view/components/Lista";
import TodoList from "./view/containers/TodoList";
import todoListStore from "./store/todoListStore";

function App() {
     {/* Que le falta al provider */}
  return (

    <Provider store={todoListStore}>
      <div style={{
        display: 'flex',
        alignItems: "center",
        justifyContent: "center",
        height: "100vh"
      }}>
       
        {/*<Lista titulo="Tareas" items={["caminar", "correr"]} />*/}
        <TodoList />
      </div>
    </Provider>
  );
}

export default App;
