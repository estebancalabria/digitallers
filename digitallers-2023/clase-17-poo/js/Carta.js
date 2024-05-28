        /*function crearCarta(imagen, titulo, descripcion) {
            return `
                <div class="col-4">
                    <div class="card h-100" style="width: 100%;">
                        <img class="card-img-top" src="${imagen}" alt="Card image cap" style="height:150px">
                        <div class="card-body">
                        <h5 class="card-title">${titulo}</h5>
                        <p class="card-text">${descripcion}</p>
                        </div>
                    </div>
                </div>`
        }*/

        class Carta {
            constructor(imagen, titulo, descripcion) {
                this.imagen = imagen;
                this.titulo = titulo;
                this.descripcion = descripcion;
            }

            toString() {
                return `
                <div class="col-4">
                    <div class="card h-100" style="width: 100%;">
                        <img class="card-img-top" src="${this.imagen}" alt="Card image cap" style="height:150px">
                        <div class="card-body">
                        <h5 class="card-title">${this.titulo}</h5>
                        <p class="card-text">${this.descripcion}</p>
                        </div>
                    </div>
                </div>`
            }
        }
