class Personaje {
    nombre;
    imagen;
    nivel;
    experiencia;
    vida;
    fuerza;
    destreza;

    constructor(nombre, imagen) {
        this.nombre = nombre;
        this.imagen = imagen;

        //Valores por Defecto:
        this.nivel = 1;
        this.experiencia = 0;
        this.vida = 100;
        this.fuerza = 10;
        this.destreza = 10;
    }

    getImagen(){
        if (this.estaVivo()){
            return this.imagen;
        }else{
            return this.imagen.replace(".png","-muerto.png");
        }
        
    }

    getNombre() {
        return this.nombre;
    }

    getNivel() {
        return this.nivel;
    }

    getExperiencia() {
        return this.experiencia;
    }

    getVida() {
        return this.vida;
    }

    getFuerza() {
        return this.fuerza;
    }

    getDestreza() {
        return this.destreza;
    }

    recibirDaño(daño) {
        if (this.estaVivo()) {
            this.vida -= daño;
        }
    }

    estaVivo() {
        return this.vida > 0;
    }

    atacar(enemigo) {
        if (this.estaVivo()) {
            enemigo.recibirDaño(this.fuerza);
            if (!enemigo.estaVivo()) {
                this.experiencia += 10;
            }
        }
    }
}
