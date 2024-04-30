
document.addEventListener("DOMContentLoaded", function () {
    console.log("El archivo estático se está sirviendo bien");
    var searchInput = document.getElementById("searchInput");

    searchInput.addEventListener("input", function () {
        var value = searchInput.value.toLowerCase();
        console.log("Valor de búsqueda:", value);

        var cards = document.querySelectorAll("#pokemonList .card");

        cards.forEach(function (card) {
            var cardTitleElement = card.querySelector(".card-title");
            var cardTitle = cardTitleElement ? cardTitleElement.textContent.toLowerCase() : "";
            console.log("Título de la tarjeta:", cardTitle);

            card.style.display = cardTitle.includes(value) ? "block" : "none";
        });
    });
});
