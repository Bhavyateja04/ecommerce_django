function filterCategory(category) {
    let cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        if (card.dataset.category == category || category == 'All') {
            card.style.display = "inline-block";
        } else {
            card.style.display = "none";
        }
    })
}
