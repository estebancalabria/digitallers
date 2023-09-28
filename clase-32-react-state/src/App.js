import Cabecera from "./components/Cabecera";
import "./App.css";
import "bootstrap/dist/css/bootstrap.css";
import versus from "./vs.jpg"
import subzero from "./subzero.webp"
import scorpion from "./scorpion.webp"
import logo from "./mk-logo.png";
import ContadorFuncional from "./components/ContadorFuncional";
import ContadorDeClases from "./components/ContadorDeClases";


function App() {
  return (
    <div>
      <Cabecera titulo="Curso de React" subtitulo="Componentes de Clases vs Funcionales" imagen={logo} />
      <main className="container">
        <div className="row">
          <div className="col-5">
            <ContadorFuncional />
            <img src={subzero} alt="subzero" style={{width:"60%", marginLeft:"20%"}}   />
          </div>
          <div className="col-2">
            <img src={versus} alt="versus" style={{width:"100%", marginTop: "10em"}}  />
          </div>
          <div className="col-5">
            <ContadorDeClases />  
            <img src={scorpion} alt="scorpion" style={{width:"50%", marginLeft:"20%"}}   />
          </div>     
        </div>
      </main>
    </div>
  );
}

export default App;
