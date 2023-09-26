import "bootstrap/dist/css/bootstrap.css";
import { Component } from "react";
import PropTypes from "prop-types";
import Swal from "sweetalert2";

class Lista extends Component {

    //Opcion 1:
    /*render(){
        return (<ul className="list-group">
            {this.props.titulo && <li className="list-group-item active">{this.props.titulo}</li>}
            {this.props.items.map((item,index)=>(<li key={index} className="list-group-item">
                {item}
            </li>))}
        </ul>)
    }*/

    comprarElemento() {
        alert(this); //Undefined si no hago el bind
        Swal.fire("Compra realizada", "Se agrego al carrito")
    }

    //Opcion 2:
    render() {
        const { titulo, items } = this.props;

        return (<ul className="list-group">
            {titulo && <li className="list-group-item active">{titulo}</li>}
            {items.map((item, index) => (<li key={index} className="list-group-item">
                {item}

                {
                    //Opcion 1 : Sin el bind (En el metodo se pierde el this)
                    //<button className="btn btn-primary float-end" onClick={this.comprarElemento}>
                    //    Comprar
                    //</button>
                }
                {
                    //Opcion 2: Usar el bind para que no desaparezca el this
                    /*<button className="btn btn-primary float-end" onClick={this.comprarElemento.bind(this)}>
                        Comprar
                    </button>*/
                }
                {
                    //Opcion 3: Pasarle el metodo desde afuera
                    this.props.onAccion && <button className="btn btn-primary float-end"
                        onClick={()=>{this.props.onAccion(item)}}>
                        Accion
                    </button>
                }
            </li>))}
        </ul>)
    }
}

Lista.propTypes = {
    titulo: PropTypes.string.isRequired,
    items: PropTypes.array.isRequired
}

export default Lista;
