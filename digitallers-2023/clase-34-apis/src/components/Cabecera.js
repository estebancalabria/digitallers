import * as styles from "./Cabecera.styles"

const Cabecera = ({titulo, subtitulo}) => {
    return (<header style={styles.headerStyle}>
        <h1>{titulo}</h1>
        <h2>{subtitulo}</h2>
    </header>);
}
 
export default Cabecera;