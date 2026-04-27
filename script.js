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

// ── Hero: efecto difuminado al hacer scroll ───────────────────
const heroSection = document.getElementById('inicio');
const heroContent = document.querySelector('.hero-content');
window.addEventListener('scroll', () => {
    if (!heroSection || !heroContent) return;
    const scrolled = window.scrollY;
    const heroH = heroSection.offsetHeight;
    const ratio = Math.min(scrolled / (heroH * 0.5), 1);
    // Difumina y sube el contenido suavemente
    heroContent.style.opacity = 1 - ratio * 0.65;
    heroContent.style.transform = `translateY(${-ratio * 30}px)`;
}, { passive: true });


// ── Swiper (Carrusel de Promotores) ───────────────────────────
document.addEventListener('DOMContentLoaded', () => {
    if (typeof Swiper !== 'undefined' && document.querySelector('.mySwiper')) {
        const swiper = new Swiper('.mySwiper', {
            slidesPerView: 1,
            spaceBetween: 20,
            autoplay: {
                delay: 4000,
                disableOnInteraction: false,
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            breakpoints: {
                640: {
                    slidesPerView: 2,
                    spaceBetween: 20,
                },
                992: {
                    slidesPerView: 3,
                    spaceBetween: 30,
                },
                1200: {
                    slidesPerView: 4,
                    spaceBetween: 30,
                }
            }
        });
    }

    if (typeof Swiper !== 'undefined' && document.querySelector('.mySwiperVoces')) {
        const swiperVoces = new Swiper('.mySwiperVoces', {
            slidesPerView: 1,
            spaceBetween: 20,
            autoplay: { delay: 4500, disableOnInteraction: false },
            pagination: { el: '.voces-pagination', clickable: true },
            breakpoints: {
                640: { slidesPerView: 2, spaceBetween: 20 },
                992: { slidesPerView: 3, spaceBetween: 30 }
            }
        });
    }
    
    // ── Filtros de Eventos ───
    const filterBtns = document.querySelectorAll('.filter-btn');
    let eventosSwiper = null;
    let originalEventosSlides = [];

    const eventosWrapper = document.getElementById('eventosWrapper');
    if (eventosWrapper) {
        originalEventosSlides = Array.from(eventosWrapper.querySelectorAll('.swiper-slide'));
    }

    function buildEventosSwiper() {
        if (eventosSwiper) {
            eventosSwiper.destroy(true, true);
            eventosSwiper = null;
        }
        if (document.querySelector('.eventosSwiper')) {
            eventosSwiper = new Swiper('.eventosSwiper', {
                slidesPerView: 1,
                spaceBetween: 20,
                loop: false,
                pagination: { el: '.eventos-pagination', clickable: true },
                navigation: { nextEl: '.eventos-btn-next', prevEl: '.eventos-btn-prev' },
                breakpoints: {
                    640:  { slidesPerView: 1, spaceBetween: 16 },
                    900:  { slidesPerView: 2, spaceBetween: 20 },
                    1200: { slidesPerView: 3, spaceBetween: 24 }
                }
            });
        }
    }

    function applyEventoFilter(filterValue) {
        if (!eventosWrapper) return;
        eventosWrapper.innerHTML = '';
        originalEventosSlides.forEach(slide => {
            const card = slide.querySelector('.evento-card-nueva');
            const distrito = card ? card.getAttribute('data-distrito') : null;
            if (filterValue === 'all' || distrito === filterValue) {
                eventosWrapper.appendChild(slide);
            }
        });
        buildEventosSwiper();
        
        // Ensure swiper updates its positioning
        if (eventosSwiper) {
            eventosSwiper.update();
            eventosSwiper.slideTo(0);
        }
    }

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => {
                b.classList.remove('active');
                b.setAttribute('aria-pressed', 'false');
            });
            btn.classList.add('active');
            btn.setAttribute('aria-pressed', 'true');
            // data-filter values: 'all', 'd1', 'd2', 'd3', 'd4', 'global'
            applyEventoFilter(btn.getAttribute('data-filter'));
        });
    });

    // Init on load
    buildEventosSwiper();

    // ── Devocionales Swiper ───────────────────────────────────────────
    if (document.querySelector('.devociSwiper')) {
        new Swiper('.devociSwiper', {
            slidesPerView: 1,
            spaceBetween: 20,
            loop: false,
            pagination: { el: '.devoci-pagination', clickable: true },
            navigation: { nextEl: '.devoci-btn-next', prevEl: '.devoci-btn-prev' },
            breakpoints: {
                640: { slidesPerView: 2, spaceBetween: 20 }
            }
        });
    }

    // ── Formación Misionera Swiper ───────────────────────────────────
    if (document.querySelector('.formacionSwiper')) {
        new Swiper('.formacionSwiper', {
            slidesPerView: 1,
            spaceBetween: 24,
            loop: false,
            pagination: { el: '.formacion-pagination', clickable: true },
            navigation: { nextEl: '.formacion-btn-next', prevEl: '.formacion-btn-prev' },
            breakpoints: {
                640:  { slidesPerView: 1 },
                900:  { slidesPerView: 2, spaceBetween: 24 },
                1200: { slidesPerView: 3, spaceBetween: 28 }
            }
        });
    }
    // ── Gira Redesign: Carrusel y Mapa Interactivo ──────────────────
    const missionaries = [
        {
            id: 'zamorano',
            name: 'Familia Zamorano',
            destination: 'Per&uacute; / Argentina',
            continent: 'america',
            continentLabel: 'AMERICA',
            continentColor: '#e6993a',
            quote: 'Construyendo el primer templo Kichwa en la selva peruana.',
            img: 'assets/images/zamorano_tour.png',
            link: 'https://www.instagram.com/p/DVg_d20Epdx/',
            coords: [-12.0464, -77.0428],
            whatsapp: '5492396601312'
        },
        {
            id: 'losmacc',
            name: 'Los Macc',
            destination: 'Sudeste Asi&aacute;tico',
            continent: 'asia',
            continentLabel: 'ASIA',
            continentColor: '#dc2626',
            quote: 'Presentar el evangelio en otra cultura es nuestro mayor desaf&iacute;o.',
            img: 'assets/images/LOS_MACC_1.png',
            link: 'https://www.instagram.com/p/DWH73FrDcLQ/?img_index=1',
            coords: [13.7563, 100.5018],
            whatsapp: '5493516825541'
        },
        {
            id: 'sepulveda',
            name: 'Flia. Sep&uacute;lveda Ramello',
            destination: 'Espa&ntilde;a',
            continent: 'europa',
            continentLabel: 'EUROPA',
            continentColor: '#3b82f6',
            quote: 'Sirviendo en 5 pa&iacute;ses: hoy con llamado a la iglesia espa&ntilde;ola.',
            img: 'assets/images/sepulveda_1.png',
            link: 'https://www.instagram.com/p/DV4CXrMiRmr/?img_index=1',
            coords: [40.4168, -3.7038],
            whatsapp: '5493516169210'
        },
        {
            id: 'aristimuno',
            name: 'Familia Aristimu&ntilde;o',
            destination: 'Asia — Mundo Budista',
            continent: 'asia',
            continentLabel: 'ASIA',
            continentColor: '#dc2626',
            quote: 'Levantando intercesores para la parte del mundo no alcanzada.',
            img: 'assets/images/aristimuno_1.png',
            link: 'https://www.instagram.com/p/DV1arDTkkjS/?img_index=1',
            coords: [27.7172, 85.3240],
            whatsapp: '541131917009'
        },
        {
            id: 'fabiana',
            name: 'Fabiana Llamas',
            destination: 'Mozambique — &Aacute;frica',
            continent: 'africa',
            continentLabel: 'AFRICA',
            continentColor: '#16a34a',
            quote: 'Misionera compartiendo testimonios de labor en el campo africano.',
            img: 'assets/images/fabiana_llamas.png',
            link: 'https://www.instagram.com/p/DVjj0nRDQYP/',
            coords: [-25.9692, 32.5732],
            whatsapp: '258872969506'
        },
        {
            id: 'analia',
            name: 'Anal&iacute;a V&aacute;zquez',
            destination: 'Mozambique — &Aacute;frica',
            continent: 'africa',
            continentLabel: 'AFRICA',
            continentColor: '#16a34a',
            quote: 'Proyecto PASA POR MOZAMBIQUE: Educaci&oacute;n e Identidad en Cristo.',
            img: 'assets/images/analia_vazquez.png',
            link: 'https://www.instagram.com/p/DWEIydbFEb2/?img_index=1',
            coords: [-18.6657, 35.5296],
            whatsapp: '541122505475'
        },
        {
            id: 'isayjose',
            name: 'Familia Misionera Isa y Jos&eacute;',
            destination: 'Asia',
            continent: 'asia',
            continentLabel: 'ASIA',
            continentColor: '#dc2626',
            quote: '5 estrellas en labor misionera. ¡S&iacute;guelos!',
            img: 'assets/images/familiamisioneraisayjose.png',
            link: 'https://www.instagram.com/isayjoseind/',
            coords: [34.0479, 100.6197],
            whatsapp: '5493512404281'
        }
    ];

    let giraSwiper = null;
    let giraMap = null;
    let giraMarkers = [];

    function renderGiraCards(filter) {
        const container = document.getElementById('gira-cards-container');
        if (!container) return;
        const filtered = filter === 'all' ? missionaries : missionaries.filter(m => m.continent === filter);
        
        container.innerHTML = filtered.map(m => `
            <div class="swiper-slide">
                <div class="gira-card">
                    <div class="gira-card-img-wrapper">
                        <img src="${m.img}" alt="${m.name}" class="gira-card-img"
                             onerror="this.closest('.gira-card-img-wrapper').classList.add('gira-img-fallback')">
                        <span class="gira-card-continent-badge" style="background:${m.continentColor}">
                            ${m.continentLabel}
                        </span>
                    </div>
                    <div class="gira-card-content">
                        <h3 class="gira-card-name">${m.name}</h3>
                        <p class="gira-card-dest"><i class="fas fa-plane-departure"></i> ${m.destination}</p>
                        <p class="gira-card-quote">${m.quote}</p>
                        <div class="gira-card-footer">
                            <a href="${m.link}" target="_blank"
                               class="btn-unified btn-unified-instagram gira-btn">
                                <i class="fab fa-instagram"></i> Ver en Instagram
                            </a>
                            ${m.whatsapp ? `<a href="https://wa.me/${m.whatsapp}" target="_blank"
                               class="btn-unified btn-unified-wa gira-btn">
                                <i class="fab fa-whatsapp"></i> Contactar
                            </a>` : ''}
                        </div>
                    </div>
                </div>
            </div>
        `).join('');
    }

    function updateGiraMarkers(filter) {
        if (!giraMap) return;
        
        giraMarkers.forEach(m => giraMap.removeLayer(m));
        giraMarkers = [];

        const filtered = filter === 'all' ? missionaries : missionaries.filter(m => m.continent === filter);
        const bounds = L.latLngBounds();

        filtered.forEach(m => {
            const marker = L.marker(m.coords, {
                icon: L.divIcon({
                    className: 'gira-minimal-marker',
                    html: '<div class="marker-dot"></div>',
                    iconSize: [20, 20],
                    iconAnchor: [10, 10]
                })
            }).addTo(giraMap);

            marker.bindPopup(`
                <div class="gira-popup-content">
                    <img src="${m.img}" class="popup-img">
                    <h4>${m.name}</h4>
                    <p>${m.destination}</p>
                    <a href="${m.link}" target="_blank" class="popup-btn">Ver Proyecto</a>
                </div>
            `, { closeButton: false, offset: [0, -5] });

            giraMarkers.push(marker);
            bounds.extend(m.coords);
        });

        if (filtered.length > 0) {
            if (filter !== 'all') {
                giraMap.fitBounds(bounds, { padding: [100, 100], maxZoom: 5 });
            } else {
                giraMap.setView([10, 0], 2);
            }
        }
    }

    function initGira() {
        if (!document.getElementById('gira-cards-container')) return;

        renderGiraCards('all');

        giraSwiper = new Swiper('.giraSwiper', {
            slidesPerView: 1,
            spaceBetween: 12,
            loop: false,
            autoplay: { delay: 5000, disableOnInteraction: true },
            pagination: { el: '.swiper-pagination', clickable: true },
            navigation: { nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev' },
            breakpoints: {
                768: { slidesPerView: 2, spaceBetween: 16 },
                1024: { slidesPerView: 3, spaceBetween: 20 }
            }
        });

        const mapContainer = document.getElementById('mapa-gira');
        if (mapContainer && typeof L !== 'undefined') {
            giraMap = L.map('mapa-gira', {
                center: [10, 0],
                zoom: 2,
                scrollWheelZoom: false,
                zoomControl: true
            });

            L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
                attribution: '&copy; OpenStreetMap &copy; CARTO'
            }).addTo(giraMap);

            updateGiraMarkers('all');
        }

        document.querySelectorAll('.filter-btn-gira').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('.filter-btn-gira').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                const continent = btn.getAttribute('data-continent');
                
                const container = document.getElementById('gira-cards-container');
                container.style.opacity = '0';
                container.style.transform = 'translateY(15px)';
                
                setTimeout(() => {
                    renderGiraCards(continent);
                    giraSwiper.update();
                    giraSwiper.slideTo(0);
                    updateGiraMarkers(continent);
                    
                    container.style.opacity = '1';
                    container.style.transform = 'translateY(0)';
                }, 400);
            });
        });
    }

    initGira();
});

// ── PWA Installation & Service Worker ───────────────────────────
document.addEventListener('DOMContentLoaded', () => {
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('./sw.js')
            .then(reg => console.log('Service Worker registrado con éxito', reg))
            .catch(err => console.error('Error al registrar el Service Worker', err));
    }

    let deferredPrompt;
    const pwaBanner = document.getElementById('pwa-install-banner');
    const installBtn = document.getElementById('btn-pwa-install');
    const dismissBtn = document.getElementById('btn-pwa-dismiss');

    window.addEventListener('beforeinstallprompt', (e) => {
        e.preventDefault();
        deferredPrompt = e;
        if (pwaBanner) {
            pwaBanner.classList.remove('hidden');
            setTimeout(() => pwaBanner.classList.add('show'), 100);
        }
    });

    if (installBtn && pwaBanner) {
        installBtn.addEventListener('click', async () => {
            if (deferredPrompt) {
                pwaBanner.classList.remove('show');
                setTimeout(() => pwaBanner.classList.add('hidden'), 500);
                deferredPrompt.prompt();
                const { outcome } = await deferredPrompt.userChoice;
                console.log(`PWA instalación: ${outcome}`);
                deferredPrompt = null;
            }
        });
    }

    if (dismissBtn && pwaBanner) {
        dismissBtn.addEventListener('click', () => {
            pwaBanner.classList.remove('show');
            setTimeout(() => pwaBanner.classList.add('hidden'), 500);
        });
    }

    window.addEventListener('appinstalled', () => {
        if (pwaBanner) {
            pwaBanner.classList.remove('show');
            pwaBanner.classList.add('hidden');
        }
        deferredPrompt = null;
        console.log('PWA instalada exitosamente');
    });
});
