import { useState } from "react";
import axios from "axios";
import { useEffect } from "react";
import Carta from "./Carta";

const GrillaPersonajesRickAndMorty = () => {

    const [personajes, setPersonajes] = useState([]);

    //REGLA : Para hacer llamadas asincronicas se usa el use effect
    useEffect(()=>{
        
        //axios.get("https://rickandmortyapi.com/api/character?page=3").then((resp)=>{
        axios.get("http://localhost:3000/personajes.json").then((resp)=>{
            setPersonajes(resp.data.results);
        })
    },[]);

    return (<div>
        {
            personajes.map((p)=>(
                <div style={{width:"24vw", display:"inline-block"}} key={p.id}>
                <Carta 
                    
                    imagen={p.image}
                    titulo={p.name}
                    texto={p.status} />
                </div>
            ))
        }
    </div>);
}
 
export default GrillaPersonajesRickAndMorty;