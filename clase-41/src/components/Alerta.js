import * as Mui from "@mui/material"
//import * as MuiIcons from "@mui/icons-material";

const Alerta = ({ texto }) => {
    return (<Mui.Alert variant="standard">
        <Mui.AlertTitle>
            <Mui.Typography>{texto}</Mui.Typography>
        </Mui.AlertTitle>
    </Mui.Alert>);
}

export default Alerta;