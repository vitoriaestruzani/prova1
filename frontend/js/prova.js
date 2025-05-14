// Interatividade Básica
document.querySelectorAll('.album-card').forEach(card => {
    card.addEventListener('click', () => {
        // Lógica para reproduzir música
        console.log('Reproduzindo...');
    });
});

// Botão Seguir
document.querySelectorAll('.btn-primary').forEach(btn => {
    btn.addEventListener('click', function() {
        this.textContent = this.textContent === 'Seguir' ? 'Seguindo' : 'Seguir';
        this.style.backgroundColor = this.textContent === 'Seguindo' ? '#4CAF50' : '#1db954';
    });
});

// Barra de Pesquisa
document.querySelector('.search-bar input').addEventListener('input', function(e) {
    const searchTerm = e.target.value.toLowerCase();
    document.querySelectorAll('.album-card').forEach(card => {
        const title = card.querySelector('h3, h4').textContent.toLowerCase();
        card.style.display = title.includes(searchTerm) ? 'block' : 'none';
    });
});