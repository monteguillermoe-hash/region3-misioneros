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

// Inicialización del Mapa Interactivo (Leaflet)
document.addEventListener('DOMContentLoaded', () => {
    const mapElement = document.getElementById('mapa-region');
    // Verificamos si el contenedor del mapa existe en la página actual
    if (mapElement) {
        // Coordenadas aproximadas del centro de la Provincia de Buenos Aires
        const map = L.map('mapa-region', {
            center: [-36.0, -60.0],
            zoom: 6,
            scrollWheelZoom: false // Desactivar zoom con la rueda del mouse por defecto por usabilidad
        });

        // Capa de mapa base (OpenStreetMap gratuito)
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        // ==== Pines de Ejemplo (Placeholders) ====
        // Marker 1
        L.marker([-34.92, -57.95]).addTo(map)
         .bindPopup('<b>Distrito 1</b><br>La Plata y alrededores.<br><a href="#promotores">Ver Promotor</a>');
         
        // Marker 2
        L.marker([-38.00, -57.55]).addTo(map)
         .bindPopup('<b>Distrito 2</b><br>Mar del Plata y zona costera.<br><a href="#promotores">Ver Promotor</a>');

        // Marker 3
        L.marker([-38.71, -62.26]).addTo(map)
         .bindPopup('<b>Distrito 3</b><br>Bahía Blanca y sur de PBA.<br><a href="#promotores">Ver Promotor</a>');

        // Activar zoom con la rueda del mouse solo cuando el usuario hace clic en el mapa (mejor UX en móviles)
        map.on('focus', () => { map.scrollWheelZoom.enable(); });
        map.on('blur', () => { map.scrollWheelZoom.disable(); });
    }
});

