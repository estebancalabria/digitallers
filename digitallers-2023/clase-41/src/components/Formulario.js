import * as Mui from "@mui/material";
import * as MuiIcons from "@mui/icons-material";

const Formulario = ({campos}) => {
    return (<form>
        {
            campos.map((campo)=>(
                <Mui.FormGroup key={campo}>
                    <Mui.FormControl>
                        <Mui.TextField label={campo} sx={{mt:1, mb:1}} />
                    </Mui.FormControl>
                    
                </Mui.FormGroup>
            ))
        }
        <Mui.Box textAlign="end">
            <Mui.Button variant="contained">Submit</Mui.Button>
        </Mui.Box>
    </form>);
}
 
export default Formulario;