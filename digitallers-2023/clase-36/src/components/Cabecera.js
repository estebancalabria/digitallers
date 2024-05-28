import "bootstrap/dist/css/bootstrap.css";

const Cabecera = ({titulo, subtitulo}) => {
    return (<header className="bg-dark text-light text-center mb-0 p-2">
        <h1>{titulo}</h1>
        <h2>{subtitulo}</h2>
    </header>);
}
 
export default Cabecera;