import * as Mui from "@mui/material"
import * as MuiIcons from "@mui/icons-material";

const Carta = ({ titulo, texto, imagen, accion }) => {
    return (<Mui.Card>
        <Mui.CardMedia image={imagen} style={{ height: "30vh" }} />
        <Mui.CardHeader title={titulo} />
        <Mui.CardContent>
            {texto}
        </Mui.CardContent>
        <Mui.CardActionArea>
            <Mui.CardActions>
                {accion}
            </Mui.CardActions>

        </Mui.CardActionArea>
    </Mui.Card>);
}

export default Carta;