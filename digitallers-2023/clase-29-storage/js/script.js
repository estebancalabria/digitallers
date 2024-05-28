
//Con SessionStorage
window.addEventListener("load",()=>{
    let inputs = document.querySelectorAll("input");
    //recorrer los inputs
    inputs.forEach((input)=>{
        input.value = sessionStorage.getItem(input.id);

        //Nos vamos a subscribir al evento keyup de cada input
        input.addEventListener("keyup", ()=>{
            sessionStorage.setItem(input.id, input.value)
        })
    });
})

//Con LocalStorage
/*window.addEventListener("load",()=>{
    let inputs = document.querySelectorAll("input");
    //recorrer los inputs
    inputs.forEach((input)=>{
        input.value = localStorage.getItem(input.id);

        //Nos vamos a subscribir al evento keyup de cada input
        input.addEventListener("keyup", ()=>{
            localStorage.setItem(input.id, input.value)
        })
    });
});*/