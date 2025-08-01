class Persona {
    #nombre;
    #apellido;

    constructor(nombre, apellido) {
        if (!nombre || !apellido || nombre.trim() === '' || apellido.trim() === '') {
            throw new Error("Nombre y apellido son obligatorios");
        }

        if (nombre.length > 50 || apellido.length > 50) {
            throw new Error("Nombre y apellido no pueden exceder los 50 caracteres");
        }

        if (!this._esSoloLetras(nombre) || !this._esSoloLetras(apellido)) {
            throw new Error("Nombre y apellido solo pueden contener letras del alfabeto");
        }

        if (nombre[0] !== nombre[0].toUpperCase() || apellido[0] !== apellido[0].toUpperCase()) {
            throw new Error("El nombre y el apellido deben comenzar con una letra mayúscula");
        }

        this.#nombre = nombre;
        this.#apellido = apellido;
    }
// Getters (propiedades de solo lectura)
    get nombre() {
        return this.#nombre;
    }

    get apellido() {
        return this.#apellido;
    }

    // Mostrar información
    mostrarInformacion() {
        console.log(`Nombre: ${this.#nombre}, Apellido: ${this.#apellido}`);
    }

    // Método privado para validar que el texto tenga solo letras
    _esSoloLetras(texto) {
        return /^[A-Za-zÁÉÍÓÚÑáéíóúñ]+$/.test(texto);
    }
}