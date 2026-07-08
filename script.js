document.addEventListener('DOMContentLoaded', () => {
    const btnMetodo = document.getElementById('btn-metodo');
    const btnHistoria = document.getElementById('btn-historia');
    
    const modalMetodo = document.getElementById('modal-metodo');
    const modalHistoria = document.getElementById('modal-historia');
    
    const closeBtns = document.querySelectorAll('.close-modal');
    
    function openModal(modal) {
        modal.classList.add('active');
    }
    
    function closeModal(modal) {
        modal.classList.remove('active');
    }
    
    if (btnMetodo) {
        btnMetodo.addEventListener('click', () => openModal(modalMetodo));
    }
    
    if (btnHistoria) {
        btnHistoria.addEventListener('click', () => openModal(modalHistoria));
    }
    
    closeBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const modal = e.target.closest('.modal');
            closeModal(modal);
        });
    });
    
    // Fechar clicando fora
    window.addEventListener('click', (e) => {
        if (e.target.classList.contains('modal')) {
            closeModal(e.target);
        }
    });
});
