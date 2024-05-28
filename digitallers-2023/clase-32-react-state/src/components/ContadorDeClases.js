import React, { Component } from 'react'; //Snippet imrc


class ContadorDeClases extends Component { //Snippet ccc
    /*constructor(props) {
        super(props);
    }*/

    //En los componentes de clases no se pueden usar los hooks
    //En los componentes de clases no hay variables de estado como en los funcionales
    //Todo el estado se guarda en un objeto json en la propiedad state (y se actualiza con el setState)
    state = { 
        contador : 0
     }

    //si bien los eventos se pueden manejar igual que en los componentes funcionales
    //voy a manejar los eventos de una forma distinta
    //para que me quede bien orientado a objetos voy a agregar primero los metodos de las cosas 
    //que puede hacer un contador
    incrementar(){
        //Opcion 1 : Pasarle un nuevo objeto state modificado
        this.setState({contador : this.state.contador+1})
    }

    decrementar(){
        //Opcion 2: Recibir una funcion flecha que recibe el state viejo y devuelve el nuevo
        //          Recibe una funcion pura (que la puedo probar aparte)
        (this.state.contador>0) && this.setState((prevState) => ({contador : prevState.contador-1}))
    }

    reset(){
        this.setState({contador: 0})
    }

    render() { 
        return (<div className="text-center border shadow p-3 m-2">
            <h3>Contador de Clases {this.state.contador}</h3>
            <div>
                <button className="btn btn-primary" onClick={this.decrementar.bind(this)}>
                    -
                </button>
                <button className="btn btn-danger ms-2 me-2" onClick={this.reset.bind(this)}>
                    Reset
                </button>
                <button className="btn btn-primary" onClick={this.incrementar.bind(this)}>
                    +
                </button>
            </div>
        </div>);
    }
}
 
export default ContadorDeClases; 