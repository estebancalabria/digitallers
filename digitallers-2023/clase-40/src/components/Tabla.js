import "bootstrap/dist/css/bootstrap.css";

const Tabla = ({items, columnas}) => {
    return (<table className="table">
        <thead>
            <tr>
            {
                columnas.map((col)=>(<th key={col}>{col}</th>))
            }
            </tr>
        </thead>
        <tbody>
            {
                items.map((item, index)=>(
                    <tr key={index}>
                        {columnas.map((col)=>(<td key={col}>{item[col]}</td>))}
                    </tr>
                ))
            }
        </tbody>
    </table>);
}
 
export default Tabla;