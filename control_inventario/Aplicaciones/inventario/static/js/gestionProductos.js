(function(){
    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener("click",(e)=>{
            const confirmacion = confirm("¿Desea eliminar este producto?");
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });

    const btnEdicion = document.querySelectorAll(".btnEdicion");

    btnEdicion.forEach(btn => {
        btn.addEventListener("click",(e)=>{
            const confirmacion = confirm("¿Desea editar este producto?");
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });
})();