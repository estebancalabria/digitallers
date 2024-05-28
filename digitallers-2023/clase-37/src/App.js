import "bootstrap/dist/css/bootstrap.css";
import axios from 'axios';
import { useEffect } from 'react';
import { useState } from 'react';
import Lista from './components/Lista';
import NoticiasContext from "./context/NoticiasContext";
import ListaSinProps from "./components/ListaSinProps";
import { Provider } from "react-redux";
import store from "./redux/store";
import ListaConRedux from "./components/ListaConRedux";

function App() {

  const [noticias, setNoticias] = useState([]);
  useEffect(() => {
    axios.get("noticias.json").then((resp) => {
      setNoticias(resp.data);
    });
  }, []);

  return (
    <div className="container">
      <button className="btn btn-primary m-3" onClick={()=>{
          setNoticias([...noticias,
          {
              id : noticias.length+1,
              titulo : `Noticia ${noticias.length+1}`,
              contenido : `Contenido ${noticias.length+1}`
          }])
      }}>
        Agregar Noticia (No funciona con Redux)
      </button>
      <section>
        <h1>Props Drilling</h1>
        <Lista titulo="Noticias" items={noticias.map((n) => (n.titulo))} />
      </section>
      <section>
        <NoticiasContext.Provider value={noticias}>
          <h1>Context Api</h1>
          <ListaSinProps />
        </NoticiasContext.Provider>
      </section>
      <section>
        <Provider store={store}>
          <h1>Redux</h1>
          <ListaConRedux />
        </Provider>
      </section>
    </div>
  );
}

export default App;
