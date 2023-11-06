import * as Mui from "@mui/material"


const Tabla = ({ columnas, items }) => {
    return (<Mui.Table>
        <Mui.TableHead>
            <Mui.TableRow>
                {

                    columnas.map((col, index) => (
                        <Mui.TableCell key={index} style={{backgroundColor:"lightslategray"}}>
                            {col.substr(0,1).toUpperCase() + col.substr(1)}
                        </Mui.TableCell>
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