import "bootstrap/dist/css/bootstrap.css";
import PropTypes from 'prop-types';

function Cabecera({titulo, subtitulo, imagen}) {  //Lo genere poniendo ffc y enger
    return (<header className="alert bg-dark text-light text-center">
        <img src={imagen} alt="logo" className="float-start" style={{width:"10vw"}}/>
        <img src={imagen} alt="logo" className="float-end" style={{width:"10vw"}}/>
        <h1>{titulo}</h1>
        <h2>{subtitulo}</h2>
    </header>);
}

Cabecera.propTypes = {
    titulo : PropTypes.string.isRequired,
    subtitulo : PropTypes.string.isRequired
}

export default Cabecera;


//Snppets
//ffc  : Componente Funcional
//ccc  : Componente de Clases con Constructor
//cc   : Componente de Clases
//sfc  : Componente Funcional Flecha