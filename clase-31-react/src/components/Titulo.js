import "bootstrap/dist/css/bootstrap.css";
import { Component } from "react";
import PropTypes from "prop-types";

class Titulo extends Component{
    render(){
        return (<h2 className="text-center text-primary">
            {this.props.texto}
        </h2>)
    }
}

//Con Munuscula!!!
//Las propTypes son opcionales
//Son una buena idea para documentar que props debe recibir el componente
Titulo.propTypes = {
    texto : PropTypes.string.isRequired
}

export default Titulo;