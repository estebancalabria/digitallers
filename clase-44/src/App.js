import { Provider } from "react-redux";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import store from "./redux/store";
import Cabecera from "./components/Cabecera";
import * as Mui from "@mui/material"
import TablaLibros from "./container/TablaLibros";
import FormularioAgregarLibro from "./container/FormularioAgregarLibro";
import FormularioEditarLibro from "./container/FormularioEditarLibro";
import { Fade } from "react-reveal";

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
              <Fade left>
                <Mui.Box>
                  <Mui.Typography variant="h2">Agregar Libro</Mui.Typography>
                  <FormularioAgregarLibro />
                </Mui.Box>
              </Fade>
            } />
            <Route path="editar/:id" element={
              <Fade right>
                <Mui.Box>
                  <Mui.Typography variant="h2">Editar Libro</Mui.Typography>
                  <FormularioEditarLibro />
                </Mui.Box>
              </Fade>
            } />
          </Routes>
        </Mui.Container>
      </BrowserRouter>
    </Provider>
  );
}

export default App;
