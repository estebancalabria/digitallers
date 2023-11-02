import { AppBar, Button, IconButton, Paper, Toolbar, Typography } from "@mui/material";
import * as Mui from "@mui/material"
import * as MuiIcons from "@mui/icons-material";
import Lista from "./components/Lista";
import Alerta from "./components/Alerta";
import Tabla from "./components/Tabla";
import Carta from "./components/Carta";
import Formulario from "./components/Formulario";


function App() {
  return (
    <div>
      <AppBar variant="elevation">
        <Toolbar variant="dense">
          <IconButton color="inherit">
            <MuiIcons.Menu />
          </IconButton>
          <Typography variant="h6" align="center" sx={{ ml: 2 }} >
            Bienvenidos a Mi Aplicacion
          </Typography>
        </Toolbar>
      </AppBar>
      <Mui.Container sx={{ mt: 9 }}>
        <Mui.Paper>
          <Alerta texto="Listas" />
          <Lista items={["Juan", "Pedro", "Ramiro", "Ana"]} />
        </Mui.Paper>

        <Mui.Paper sx={{ mt: 2 }}>
          <Alerta texto="Tabla" />
          <Tabla
            columnas={["nombre", "apellido", "edad"]}
            items={[{ nombre: "Alicia", apellido: "Fernandez", edad: 31 },
            { nombre: "Bob", apellido: "Dylan", edad: 68 },
            { nombre: "Charles", apellido: "Xavier", edad: 72 }]} />
        </Mui.Paper>

        <Mui.Paper sx={{ mt: 2 , p:1}}>
          <Alerta texto="Carta" />
          <Mui.Grid container sx={{mt:1}}  spacing={2}>
            {
              [1, 2, 3, 4].map((item) => (
                <Mui.Grid key={item} item xs={3}>
                  <Carta
                    imagen="https://thispersondoesnotexist.com/"
                    titulo="Juan Perez"
                    texto="Un programador de Microsoft que tiene su propia empresa"
                    accion="Mas Info.." />

                </Mui.Grid>
              ))
            }
          </Mui.Grid>
        </Mui.Paper>

        <Mui.Paper sx={{p:2}}>
          <Alerta texto="Formulario" />
          <Formulario campos={["nombre", "apellido", "edad"]} />
        </Mui.Paper>



      </Mui.Container>
    </div>
  );
}

export default App;
