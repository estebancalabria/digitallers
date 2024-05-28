class Movimiento {
    monto
    concepto

    constructor(monto, concepto) {
        this.monto = monto;
        this.concepto = concepto;
    }

    getMonto() {
        return this.monto;
    }

    getConcepto() {
        return this.concepto;
    }
}

class Cuenta {
    numero;
    titular;
    //saldo;
    movimientos = [];

    constructor(numero, titular) {
        this.numero = numero;
        this.titular = titular;
        //this.saldo = 0;
    }

    depositar(monto, concepto) {
        let movimiento = new Movimiento(monto, concepto);
        this.movimientos.push(movimiento);
    }

    retirar(monto, concepto) {
        if (this.getSaldo() >= monto) {
            let movimiento = new Movimiento(-monto, concepto);
            this.movimientos.push(movimiento);
        }
    }

    getSaldo() {
        let saldo = 0;
        for (let movimiento of this.movimientos) {
            saldo += movimiento.getMonto();
        }
        return saldo;
    }

    getNumero() {
        return this.numero;
    }

    toString() {
        return `(${this.numero}) ${this.titular} [Saldo ${this.getSaldo()}]`
    }
}

class Banco {
    nombre;
    cuentas = [];

    constructor(nombre) {
        this.nombre = nombre;
    }

    abrirCuenta(titular) {
        let numero = Math.round(Math.random() * 1000000);
        let cuenta = new Cuenta(numero, titular);
        this.cuentas.push(cuenta);
    }

    getCuentas() {
        return this.cuentas;
    }

    getCuentaByNumero(numero) {
        for (let cuenta of this.cuentas) {
            if (cuenta.getNumero() == numero) {
                return cuenta;
            }
        }
        return null;
    }
}
