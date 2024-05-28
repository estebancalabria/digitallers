import { useSelector } from "react-redux";
import Lista from "./Lista";

const ListaConRedux = () => {

    const noticias = useSelector(store => store.noticias);

    return (<Lista titulo="Noticias (Desde el Store, con Redux)"
        items={noticias.map((n) => (n.titulo))}>

    </Lista>);
}

export default ListaConRedux;