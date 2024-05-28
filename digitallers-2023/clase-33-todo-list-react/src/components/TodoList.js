import { useState } from "react";
import * as Bs from "react-bootstrap";
import Swal from "sweetalert2";
import { Slide, LightSpeed } from "react-reveal";

//Math.max(...items.map((i)=>(i.id)),0) + 1,
//Math.max(54,54,54,67,84,23,54)  ==> 84
//items.map((i)=>(i.id)) ==> [1,2,3,4]
//Math.max(...items.map((i)=>(i.id)))
//Math.max(...items.map((i)=>(i.id)) ,0)  ,0 por si el array esta vaio

//let t = {nombre:"pepe", done:true};
//let copiat = {...t};
//let doneModificado = {...t, done: !t.done};


function TodoList({ titulo, tareas }) {

    let [items, setItems] = useState(tareas);
    let [nuevaTarea, setNuevaTarea] = useState("");

    return (<Bs.ListGroup style={{ maxWidth: "50vw", margin: "auto" }}>
        <Bs.ListGroupItem active>{titulo}</Bs.ListGroupItem>
        <Bs.ListGroupItem>
            <Bs.InputGroup>
                <Bs.FormControl placeholder="Plato"
                    value={nuevaTarea}
                    onChange={(evt) => {
                        setNuevaTarea(evt.target.value);
                    }} />
                <Bs.Button variant="outline-primary"
                    onClick={() => {
                        /* if (nuevaTarea.length>0) {...} */
                        (nuevaTarea.length > 0) && setItems([...items,
                        {
                            id: Math.max(...items.map((i) => (i.id)), 0) + 1,
                            nombre: nuevaTarea,
                            done: false
                        }]);
                        setNuevaTarea("");
                    }}>
                    +
                </Bs.Button>
            </Bs.InputGroup>
        </Bs.ListGroupItem>
        {
            items.map((tarea) => (<Slide key={tarea.id} top><Bs.ListGroupItem>
                <Bs.FormCheck style={{ display: "inline" }} checked={tarea.done}
                    onChange={() => {
                        setItems(items.map((t) => ((tarea.id === t.id) ? { ...t, done: !t.done } : t)))
                    }} />

                <LightSpeed top spy={tarea.done}>
                    {tarea.done
                        ? <strike className="ms-3">{tarea.nombre}</strike>
                        : <span className="ms-3">{tarea.nombre}</span>}
                </LightSpeed>
                <Bs.Button variant="danger" className="float-end"
                    onClick={() => {
                        Swal.fire({
                            title: "Seguro Eliminar",
                            text: tarea.nombre,
                            showCancelButton: true,
                            icon: "warning"
                        }).then((resp) => {
                            resp.isConfirmed && setItems(items.filter((item) => (item.id !== tarea.id)))
                        });
                    }}>
                    -
                </Bs.Button>
            </Bs.ListGroupItem></Slide>))
        }
    </Bs.ListGroup>);
}

export default TodoList;