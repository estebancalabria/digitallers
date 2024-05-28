import * as Mui from "@mui/material"
//import * as MuiIcons from "@mui/icons-material";

const Tabla = ({ columnas, items }) => {
    return (<Mui.Table>
        <Mui.TableHead>
            <Mui.TableRow>
                {

                    columnas.map((col, index) => (
                        <Mui.TableCell key={index}>{col}</Mui.TableCell>
                    ))

                }
            </Mui.TableRow>
        </Mui.TableHead>
        <Mui.TableBody>
                {
                    items.map((item,index)=>(
                        <Mui.TableRow key={index}>
                            {
                                columnas.map((col,index)=>(
                                    <Mui.TableCell key={index}>
                                        {item[col]}
                                    </Mui.TableCell>
                                ))
                            }
                        </Mui.TableRow>
                    ))
                }
        </Mui.TableBody>
    </Mui.Table>);
}

export default Tabla;