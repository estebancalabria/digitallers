import { connect } from "react-redux"
import Contador from "../componets/Contador"

function mapStateToProps(state){
    return {
        valor : state.contador
    }
}

export default connect(mapStateToProps)(Contador);