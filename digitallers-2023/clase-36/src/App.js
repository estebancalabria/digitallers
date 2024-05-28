
import { BrowserRouter } from 'react-router-dom';
import Cabecera from './components/Cabecera';
import Inicio from './pages/Inicio';
import Peliculas from './pages/Peliculas';
import NuevaPelicula from './pages/NuevaPelicula';
import Navegacion from './components/Navegacion';
import Principal from './components/Principal';
import { useEffect, useState } from 'react';
import axios from 'axios';

function App() {

  const [peliculas, setPeliculas] = useState([]);
  useEffect(() => {
    axios.get("http://localhost:3001/peliculas").then((resp) => {
      setPeliculas(resp.data);
    });
  }, []);

  const rutas = [
    { url: "", nombre: "Inicio", componente: <Inicio /> },
    {
      url: "peliculas",
      nombre: "Peliculas",
      componente: <Peliculas peliculas={peliculas} />
    },
    {
      url: "nueva",
      nombre: "Nueva",
      componente: <NuevaPelicula onAgregarPelicula={(peli)=>{
        setPeliculas([...peliculas, peli]);
      }}/>
    },
  ]

  return (
    <BrowserRouter>
      <Cabecera titulo="React Pelis Library" subtitulo="Digitallers Clase 36" />
      <Navegacion rutas={rutas} />
      <Principal rutas={rutas} />
    </BrowserRouter>
  );
}

export default App;
