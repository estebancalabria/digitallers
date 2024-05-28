import "bootstrap/dist/css/bootstrap.css";

const Lista = ({titulo, items}) => {
    return (<ul className="list-group">
        <li className="list-group-item active">{titulo}</li>
        {
            items.map((item, index)=>(
                <li key={index} className="list-group-item ">{item}</li>
            ))
        }
    </ul>);
}
 
export default Lista;