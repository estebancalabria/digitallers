

class Lista{
    elementos = [];

    /*constructor(){
        //No tiene constructor    
    }*/

    agregarElemento(elemento){
        this.elementos.push(elemento);
    }

    toString(){
        let cadena = '<ul class="list-group">';
        for (let elem of this.elementos){
            cadena += `<li class="list-group-item">${elem}</li>`
        }
        cadena += '</ul>';
        return cadena;
    }
}