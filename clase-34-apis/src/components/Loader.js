
const Loader = ({show}) => {
    return (<div style={{
        position:"fixed",
        width:"100%",
        height:"100%",
        zIndex : 300,
        top : 0,
        right:0,
        background:"#E0E1E2 url('Loader.gif') no-repeat center",
        opacity : 0.9,
        display : show ? "block" : "none"
    }}>
    
    </div>);
}
 
export default Loader;