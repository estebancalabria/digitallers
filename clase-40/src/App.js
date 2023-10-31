import { BrowserRouter, Link, Routes, Route } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.css";
import { Provider } from "react-redux";
import store from "./store/store";
import TablaIA from "./containers/TablaIA";
import FormularoIA from "./containers/FormularioIA";

function App() {
  return (
    <BrowserRouter>
      <Provider store={store}>
        <header className="alert alert-info text-center">
          <h1>Catalogo de Inteligencias Artificiales</h1>
        </header>
        <main className="container">
          <Routes>
            <Route path="" element={<div>
              <div className="text-end">
                <Link to="agregar">Agregar</Link>
              </div>
              <TablaIA />
            </div>} />

            <Route path="agregar" element={ <FormularoIA />} />
          </Routes>

        </main>
      </Provider>
    </BrowserRouter>
  );
}

export default App;
