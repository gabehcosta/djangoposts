(function () {

    const botaoExcluir = document.querySelectorAll(".botao-excluir");

    botaoExcluir.forEach(botao => {
        botao.addEventListener("click", (e) => {
            const confirmacao = confirm("Tem certeza que quer excluir essa postagem?");
            if(!confirmacao) {
                e.preventDefault();
            }
        });
    });
})();