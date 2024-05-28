import { connect } from "react-redux"
import Boton from "../componets/Boton"
import { ACT_RESET } from "../../actions/action-types"


function mapStateToProps(state){
    return {
        texto : `Reset (${state.contador})`
    }
}

function mapDispatchToProps(dispatch){
    return {
        onClick : ()=>{
            dispatch({
                type : ACT_RESET
            })
        }
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Boton);