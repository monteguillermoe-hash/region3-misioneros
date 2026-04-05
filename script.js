// ── Navbar scroll effect ──────────────────────────────────────
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 50);
});

// ── Menú móvil ────────────────────────────────────────────────
const mobileToggle = document.querySelector('.mobile-toggle');
const navLinks     = document.getElementById('nav-links');
const navItems     = document.querySelectorAll('.nav-item');

mobileToggle.addEventListener('click', () => {
    const open = navLinks.classList.toggle('active');
    mobileToggle.setAttribute('aria-expanded', open);
});

navItems.forEach(item => {
    item.addEventListener('click', () => {
        navLinks.classList.remove('active');
        mobileToggle.setAttribute('aria-expanded', false);
    });
});

document.addEventListener('click', e => {
    if (!navbar.contains(e.target)) {
        navLinks.classList.remove('active');
        mobileToggle.setAttribute('aria-expanded', false);
    }
});

// ── Reveal on scroll ─────────────────────────────────────────
const revealEls = document.querySelectorAll('.reveal');
const revealOnScroll = () => {
    const vh = window.innerHeight;
    revealEls.forEach(el => {
        if (el.getBoundingClientRect().top < vh - 100) el.classList.add('active');
    });
};
window.addEventListener('scroll', revealOnScroll, { passive: true });
revealOnScroll();

// ── Active nav link por sección visible ──────────────────────
const sections     = document.querySelectorAll('section[id], footer[id]');
const navLinkItems = document.querySelectorAll('.nav-item[href^="#"]');
const sectionObs   = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            navLinkItems.forEach(l => l.classList.remove('active'));
            const a = document.querySelector(`.nav-item[href="#${entry.target.id}"]`);
            if (a) a.classList.add('active');
        }
    });
}, { threshold: 0.3 });
sections.forEach(s => sectionObs.observe(s));

// ── Mapa Leaflet — 5 Distritos Región 3 ──────────────────────
document.addEventListener('DOMContentLoaded', () => {
    const mapEl = document.getElementById('mapa-region');
    if (!mapEl || typeof L === 'undefined') return;

    const map = L.map('mapa-region', {
        center: [-37.4, -61.8],
        zoom: 6,
        scrollWheelZoom: false
    });

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
        maxZoom: 18
    }).addTo(map);

    map.on('focus', () => map.scrollWheelZoom.enable());
    map.on('blur',  () => map.scrollWheelZoom.disable());

    const icono = (color, label) => L.divIcon({
        className: '',
        html: `<div style="width:46px;height:46px;border-radius:50%;background:${color};border:3px solid white;box-shadow:0 3px 12px rgba(0,0,0,0.35);display:flex;align-items:center;justify-content:center;font-family:Montserrat,sans-serif;font-weight:800;font-size:11px;color:white;cursor:pointer;">${label}</div>`,
        iconSize: [46, 46],
        iconAnchor: [23, 23]
    });

    const popup = (titulo, ciudades) =>
        `<div style="font-family:Montserrat,sans-serif;min-width:190px;padding:4px 2px;">
            <strong style="color:#008f96;font-size:0.95rem;">${titulo}</strong>
            <p style="margin:6px 0 8px;font-size:0.8rem;color:#444;line-height:1.5;">${ciudades}</p>
            <a href="#promotores" style="color:#00AAB2;font-weight:700;font-size:0.82rem;">Ver promotores →</a>
         </div>`;

    [
        { lat:-36.61, lng:-64.28, color:'#00AAB2', label:'D1',
          titulo:'Distrito 1 — La Pampa',
          ciudades:'Toda la provincia de La Pampa.' },
        { lat:-38.30, lng:-62.00, color:'#007d85', label:'D2',
          titulo:'Distrito 2 — Sudoeste PBA',
          ciudades:'Bahía Blanca, Tres Arroyos, Necochea, Tornquist, Patagones y más.' },
        { lat:-37.70, lng:-57.10, color:'#F9B22C', label:'D3',
          titulo:'Distrito 3 — Costa Atlántica',
          ciudades:'Mar del Plata, Balcarce, Villa Gesell, Pinamar, Partido de la Costa y más.' },
        { lat:-35.90, lng:-62.00, color:'#00AAB2', label:'D4',
          titulo:'Distrito 4 — Noroeste PBA',
          ciudades:'Pehuajó, Trenque Lauquen, Olavarría, 9 de Julio, Carlos Casares y más.' },
        { lat:-37.50, lng:-59.50, color:'#007d85', label:'D5',
          titulo:'Distrito 5 — Centro/Este PBA',
          ciudades:'Tandil, Azul, Cañuelas, Lobos, Saladillo, Chascomús y más.' }
    ].forEach(d => {
        L.marker([d.lat, d.lng], { icon: icono(d.color, d.label) })
            .addTo(map)
            .bindPopup(popup(d.titulo, d.ciudades), { maxWidth: 260 });
    });
});
