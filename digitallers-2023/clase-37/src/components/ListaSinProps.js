import { useContext } from "react";
import NoticiasContext from "../context/NoticiasContext";
import Lista from "./Lista";

const ListaSinProps = () => {

    const noticias = useContext(NoticiasContext);

    return (<Lista titulo="Noticias (Sin Props)"
        items={noticias.map((n) => (n.titulo))}></Lista>);
}

export default ListaSinProps;