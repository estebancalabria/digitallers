import "bootstrap/dist/css/bootstrap.css";

const Boton = ({ texto, onClick }) => {
    return (<button className="btn btn-primary m-1"
        onClick={() => { onClick() }}>
        {texto}
    </button>);
}

export default Boton;