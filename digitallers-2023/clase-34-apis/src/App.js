import Cabecera from "./components/Cabecera";
import Carta from "./components/Carta";
import GrillaPersonajesRickAndMorty from "./components/GrillaPersonajesRickAndMorty";
import GrillaPersonajesSimpsons from "./components/GrillaPersonajesSimpsons";

function App() {
  return (
    <div>
      <Cabecera titulo="React Clase 34" subtitulo="LLamadas a API" />
      <main>
        {/*<GrillaPersonajesRickAndMorty />*/}
        <GrillaPersonajesSimpsons />
      </main>
    </div>
  );
}

export default App;
