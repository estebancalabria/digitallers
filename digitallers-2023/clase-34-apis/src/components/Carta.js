import * as styles from "./Carta.styles"

const Carta = ({imagen, titulo, texto}) => {
    return (
        <div style={styles.card}>
            <img style={styles.cardImage} src={imagen} alt="titulo" />
            <div style={styles.cardBody}>
                <h3>{titulo}</h3>
                <p>{texto}</p>
            </div>
        </div>
    );
}
 
export default Carta;