// Função para mostrar opções da header em celulares
function onToggleMenu(button) {
    const navLinks = document.querySelector('#nav-menu');
    const iconContainer = document.querySelector('#icon-container');

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

// Função para envio de formulário
const btn = document.querySelector('#submitbtn')

btn.addEventListener('click', function(event){
    event.preventDefault()

    const name = document.querySelector('#name').value
    const email = document.querySelector('#email').value
    const object = document.querySelector('#object').value
    const message = document.querySelector('#message').value

    console.log(name)
})