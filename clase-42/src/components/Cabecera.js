import * as Mui from "@mui/material"
import * as MuiIcons from "@mui/icons-material";

const Cabecera = ({titulo}) => {
    return (<Mui.AppBar variant="elevation" position="static">
    <Mui.Toolbar variant="dense">
      <Mui.IconButton color="inherit">
        <MuiIcons.Menu />
      </Mui.IconButton>
      <Mui.Typography variant="h6" align="center" sx={{ ml: 2 }} >
        {titulo}
      </Mui.Typography>
    </Mui.Toolbar>
  </Mui.AppBar>);
}
 
export default Cabecera;