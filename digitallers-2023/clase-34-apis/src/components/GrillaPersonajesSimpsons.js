import React, { Component } from 'react'; //Sinippet imrc
import axios from 'axios';
import Carta from './Carta';
import Loader from './Loader';

class GrillaPersonajesSimpsons extends Component { //Snippet cc
    state = { 
        loading : true,
        personajes : []  //remplaza al useState de los funcionales
    } 

    componentDidMount(){  //remplazo del useEffect
        setTimeout(()=>{
            axios.get("https://apisimpsons.fly.dev/api/personajes").then((resp)=>{
                this.setState({
                    personajes : resp.data.docs,
                    loading : false
                });
            });    
        }, 5000);
    }

    render() { 
        return (<div>
            <Loader show={this.state.loading}/>
            {
                this.state.personajes.map((p)=>(
                    <div key={p._id} style={{width:"24vw", display:"inline-block", verticalAlign: "top"}} >
                    <Carta 
                        
                        imagen={p.Imagen}
                        titulo={p.Nombre}
                        texto={p.Historia} />
                    </div>
                ))
            }
        </div>);
    }
}
 
export default GrillaPersonajesSimpsons;