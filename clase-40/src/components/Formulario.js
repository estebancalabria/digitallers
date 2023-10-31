import "bootstrap/dist/css/bootstrap.css";
import {  useState } from "react";

const Formulario = ({ titulo, campos, onSubmit }) => {

    const [estado, setEstado] = useState({});

    return (
        <div>
            <h3 className="alert alert-info">{titulo}</h3>
            <form>
                {
                    campos.map((campo) => (<div key={campo}>
                        <label>{campo}</label>
                        <input
                            type="text" 
                            className="form-control"
                            onChange={(evt) => {
                                let newState = { ...estado }
                                newState[campo] = evt.target.value;
                                setEstado(newState);
                            }} />
                    </div>))
                }
                <button type="button"
                    className="btn btn-primary w-100 mt-2"
                    onClick={() => {
                        onSubmit(estado);
                    }}>
                    Submit
                </button>
            </form>
        </div>
    );
}

export default Formulario;