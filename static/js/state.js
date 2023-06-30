const myBtn = document.querySelector("#myBtn");
const state = document.querySelector("#state");
myBtn.addEventListener("click", function() {
    state.textContent='Aguarde...';
});
const down_link = document.querySelector("#down-link");
down_link.addEventListener("click", function() {
    state.style.color = "#ff0000";
    state.textContent='Baixando... Cheque os downloads.';
    down_link.textContent="";
})