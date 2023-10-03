import React, { Component } from 'react'; //Smippet imrc
import * as Bs from "react-bootstrap";
import PropTypes from 'prop-types';

class Cabecera extends Component {  //Snippet cc
    render() { 
        return (<Bs.Alert className='text-center' variant='primary'>
            <h1>{this.props.titulo}</h1>
            <h2>{this.props.subtitulo}</h2>
        </Bs.Alert> );
    }
}

Cabecera.propTypes = {  //la p de propTypes aca es con minuscula!!
    titulo : PropTypes.string.isRequired,
    subtitulo: PropTypes.string.isRequired
}
 
export default Cabecera;