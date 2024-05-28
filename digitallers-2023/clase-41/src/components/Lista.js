import * as Mui from "@mui/material"
import * as MuiIcons from "@mui/icons-material";

const Lista = ({ items }) => {
    return (<Mui.List>
        {
            items.map((item, index) => (
                <Mui.ListItem
                    key={index}
                    secondaryAction={<Mui.IconButton>
                        <MuiIcons.Edit />
                    </Mui.IconButton>}>
                    <Mui.ListItemIcon>
                        <Mui.IconButton>
                            <MuiIcons.Person />
                        </Mui.IconButton>
                    </Mui.ListItemIcon>
                    <Mui.ListItemText>
                        {item}
                    </Mui.ListItemText>
                </Mui.ListItem>
            ))
        }
    </Mui.List>);
}

export default Lista;