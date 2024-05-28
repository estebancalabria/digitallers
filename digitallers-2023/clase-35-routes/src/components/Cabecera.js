import "bootstrap/dist/css/bootstrap.css";

const Cabecera = ({titulo, subtitulo}) => {
    return (<header className="alert alert-info text-center mb-0">
        <h1>{titulo}</h1>
        <h2>{subtitulo}</h2>
    </header>);
}
 
export default Cabecera;