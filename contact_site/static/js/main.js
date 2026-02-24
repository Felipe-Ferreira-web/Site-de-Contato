// Função para mostrar opções da header em celulares
function onToggleMenu(button) {
    const navLinks = document.querySelector('#nav-menu');

    navLinks.classList.toggle('top-[5rem]');
    
    button.classList.add('scale-90');
    setTimeout(() => button.classList.remove('scale-90'), 100);
}

window.addEventListener('resize', () => {
    if (window.innerWidth >= 768) {
        const navLinks = document.querySelector('#nav-menu');
        navLinks.classList.remove('top-[5rem]');
    }
});