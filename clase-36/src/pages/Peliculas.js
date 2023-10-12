import "bootstrap/dist/css/bootstrap.css";

const Peliculas = ({peliculas}) => {
    return (<div>
        <h1 className="alert alert-info text-center mt-4">Peliculas</h1>
        <div className="row">
            {
                peliculas.map((peli)=>(
                    <div key={peli.id} className="col-sm-4 mb-4">
                        <div className="card w-100 h-100 text-center shadow">
                            <h4 className="card-title mt-2">{peli.nombre}</h4>
                            <div className="card-body">
                                <p className="card-text">
                                    {peli.genero}
                                    ({peli.año})
                                </p>
                            </div>
                        </div>
                    </div>
                ))
            }
        </div>
    </div>);
}
 
export default Peliculas;