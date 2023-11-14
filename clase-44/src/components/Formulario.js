import * as Mui from "@mui/material";
import { useState } from "react";

const Formulario = ({campos, item, onSubmit}) => {

    const [formState, setFormState] = useState(item ? item : {});

    return (<form>
        {
            campos.map((campo)=>(
                <Mui.FormGroup key={campo}>
                    <Mui.FormControl>
                        <Mui.TextField 
                            label={campo} 
                            sx={{mt:1, mb:1}} 
                            value={item && formState[campo]}
                            onChange={(evt)=>{
                                let newState = {...formState};
                                newState[campo] = evt.target.value;
                                setFormState(newState);
                            }}/>
                    </Mui.FormControl>
                    
                </Mui.FormGroup>
            ))
        }
        <Mui.Box textAlign="end">
            <Mui.Button 
                variant="contained"
                onClick={()=>{onSubmit(formState)}}>
                Submit
            </Mui.Button>
        </Mui.Box>
    </form>);
}
 
export default Formulario;