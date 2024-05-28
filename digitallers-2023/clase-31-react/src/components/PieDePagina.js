import "bootstrap/dist/css/bootstrap.css";

//
// Opcion 1 : Con {} y return
//
/*const PieDePagina = ({empresa, disclaimer}) => {
     return <footer className="bg-dark text-light text-end fixed-bottom p-3">
        CopyRight {empresa}&copy;{new Date().getFullYear()}. {disclaimer}
     </footer>
}*/

//
// Opcion 2 : Con () y sin return (return implicito)
//
const PieDePagina = ({empresa, disclaimer}) => (
     <footer className="bg-dark text-light text-end fixed-bottom p-3">
       CopyRight {empresa}&copy;{new Date().getFullYear()}. {disclaimer}
    </footer>
);

export default PieDePagina;