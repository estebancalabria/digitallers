import { connect } from "react-redux";
import Lista from "../components/Lista";


function mapStateToProps(state){
    return {
        items : state.tareas.map((tarea)=>(tarea.accion))   
    }
}

export default connect(mapStateToProps)(Lista);