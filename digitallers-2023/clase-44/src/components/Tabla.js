import * as Mui from "@mui/material"
import * as MuiIcons from "@mui/icons-material"


const Tabla = ({ columnas, items, onEditar, onEliminar }) => {
    return (<Mui.Table>
        <Mui.TableHead>
            <Mui.TableRow>
                {

                    columnas.map((col, index) => (
                        <Mui.TableCell key={index} style={{ backgroundColor: "lightslategray" }}>
                            {
                                col.substr(0, 1).toUpperCase() + col.substr(1)
                            }
                        </Mui.TableCell>
                    ))

                }
                {
                    onEditar && <Mui.TableCell style={{ backgroundColor: "lightslategray" }}></Mui.TableCell>
                }
                {
                    onEliminar && <Mui.TableCell style={{ backgroundColor: "lightslategray" }}></Mui.TableCell>
                }
            </Mui.TableRow>
        </Mui.TableHead>
        <Mui.TableBody>
            {
                items.map((item, index) => (
                    <Mui.TableRow key={index}>
                        {
                            columnas.map((col, index) => (
                                <Mui.TableCell key={index}>
                                    {
                                        item[col]
                                    }
                                </Mui.TableCell>
                            ))
                        }
                        {
                            onEditar && <Mui.TableCell >
                                <Mui.Box textAlign="end">
                                    <Mui.IconButton onClick={()=>{
                                        onEditar(item)
                                    }}>
                                        <MuiIcons.Edit />
                                    </Mui.IconButton>
                                </Mui.Box>
                            </Mui.TableCell>
                        }
                        {
                            onEliminar && <Mui.TableCell >
                                <Mui.Box textAlign="end">
                                    <Mui.IconButton onClick={()=>{
                                        onEliminar(item);
                                    }}>
                                        <MuiIcons.Delete />
                                    </Mui.IconButton>
                                </Mui.Box>
                            </Mui.TableCell>
                        }
                    </Mui.TableRow>
                ))
            }
        </Mui.TableBody>
    </Mui.Table >);
}

export default Tabla;