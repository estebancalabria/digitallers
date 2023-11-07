import { Provider } from "react-redux";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import store from "./redux/store";
import Cabecera from "./components/Cabecera";
import * as Mui from "@mui/material"
import TablaLibros from "./container/TablaLibros";
import FormularioLibro from "./container/FormularioLibro";

function App() {
  return (
    <Provider store={store}>
      <BrowserRouter>
        <Cabecera titulo="Mi Deslumbrante BookStore en React" />
        <Mui.Container sx={{ mt: 3 }}>
          <Routes>
            <Route path="/" element={
              <>
                <Mui.Box textAlign="end">
                  <Link to="agregar">Nuevo Libro</Link>
                </Mui.Box>
                <TablaLibros />
              </>
            } />
            <Route path="agregar" element={
              <FormularioLibro />
            } />
          </Routes>
        </Mui.Container>
      </BrowserRouter>
    </Provider>
  );
}

export default App;
