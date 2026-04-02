// Efecto de Scroll en Navbar
const navbar = document.getElementById('navbar');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Menú Móvil
const mobileToggle = document.querySelector('.mobile-toggle');
const navLinks = document.getElementById('nav-links');
const navItems = document.querySelectorAll('.nav-item');

mobileToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});

navItems.forEach(item => {
    item.addEventListener('click', () => {
        navLinks.classList.remove('active');
    });
});

// Animaciones de Aparición (Reveal)
const revealElements = document.querySelectorAll('.reveal');

const revealOnScroll = () => {
    const windowHeight = window.innerHeight;
    const elementVisible = 150;

    revealElements.forEach(el => {
        const elementTop = el.getBoundingClientRect().top;
        if (elementTop < windowHeight - elementVisible) {
            el.classList.add('active');
        }
    });
};

window.addEventListener('scroll', revealOnScroll);
revealOnScroll(); // Activar en carga inicial

// Simulación de Formulario
const formOracion = document.getElementById('form-oracion');
const oracionSuccess = document.getElementById('oracion-success');

if (formOracion) {
    formOracion.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const btn = formOracion.querySelector('button[type="submit"]');
        const originalText = btn.textContent;
        btn.textContent = 'Enviando...';
        btn.disabled = true;

        setTimeout(() => {
            formOracion.reset();
            btn.textContent = originalText;
            btn.disabled = false;
            
            oracionSuccess.classList.remove('hidden');
            
            setTimeout(() => {
                oracionSuccess.classList.add('hidden');
            }, 5000);
        }, 1500);
    });
}
