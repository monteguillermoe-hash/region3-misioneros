with open("evento-detalle.html", "r") as f:
    content = f.read()

# Update meta description
content = content.replace(
    "con el proyecto 'De tu casa a las naciones'",
    "con el viaje 'Misión Posible a Tokyo' y el proyecto 'Change the Map'"
)

# Update the info card
old_card = """<div class="perfil-info-card" style="border-color: #16a34a;">
                    <div class="card-icon" style="background: #16a34a;"><i class="fas fa-home"></i></div>
                    <h4>Proyecto</h4>
                    <p>De tu casa a las naciones</p>
                </div>"""
new_card = """<div class="perfil-info-card" style="border-color: #16a34a;">
                    <div class="card-icon" style="background: #16a34a;"><i class="fas fa-plane-departure"></i></div>
                    <h4>Próximo Viaje</h4>
                    <p>Misión Posible a Tokyo</p>
                </div>"""
content = content.replace(old_card, new_card)

# Update the project section
old_proj = """<!-- Proyecto "De tu casa a las naciones" -->
            <div class="detalle-bloque reveal" style="margin-bottom: 3rem;">
                <div class="section-header text-center" style="margin-bottom: 2rem;">
                    <span class="tag" style="background: var(--secondary-color); color: var(--text-dark); margin-bottom: 1rem;">
                        <i class="fas fa-home"></i> PROYECTO MISIONERO
                    </span>
                    <h2>De tu casa a las naciones</h2>
                </div>
                <div class="proyecto-highlight">
                    <div class="proyecto-icon">🌏</div>
                    <h3>Un llamado para cada hogar</h3>
                    <p>
                        Este proyecto nace con la visión de que cada hogar puede ser un faro de luz para el mundo no alcanzado. Sin importar dónde te encontrés, desde tu propia casa podés ser parte activa de la obra misionera: orando, ofrendando y movilizando a otros hacia el campo.
                    </p>
                    <div class="proyecto-actions">
                        <a href="https://wa.me/541131917009" target="_blank" class="btn-unified" style="background: white; color: var(--primary-dark); font-weight: bold; border: none; padding: 0.9rem 2rem; border-radius: 50px; display: inline-flex; align-items: center; gap: 0.5rem;">
                            <i class="fab fa-whatsapp" style="color: #25D366; font-size: 1.2rem;"></i> Quiero participar
                        </a>
                        <a href="https://www.instagram.com/fliaaristimuno/" target="_blank" class="btn-unified" style="background: rgba(255,255,255,0.15); color: white; border: 2px solid rgba(255,255,255,0.4); font-weight: bold; padding: 0.9rem 2rem; border-radius: 50px; display: inline-flex; align-items: center; gap: 0.5rem; backdrop-filter: blur(4px);">
                            <i class="fab fa-instagram"></i> Seguir el proyecto
                        </a>
                    </div>
                </div>
            </div>"""

new_proj = """<!-- Viaje a Tokyo -->
            <div class="detalle-bloque reveal" style="margin-bottom: 3rem;">
                <div class="section-header text-center" style="margin-bottom: 2rem;">
                    <span class="tag" style="background: var(--secondary-color); color: var(--text-dark); margin-bottom: 1rem;">
                        <i class="fas fa-plane"></i> VIAJE MISIONERO
                    </span>
                    <h2>Misión Posible a Tokyo</h2>
                </div>
                <div class="proyecto-highlight">
                    <div class="proyecto-icon">🇯🇵</div>
                    <h3>Rumbo a Japón</h3>
                    <p>
                        Este martes 6 de octubre emprendemos viaje como misioneros hacia Japón. Con el proyecto <strong>"Change the Map"</strong>, buscamos levantar clamor y oración por el mundo Budista, creyendo firmemente que Dios va a transformar naciones enteras.
                    </p>
                    <div class="proyecto-actions">
                        <a href="https://wa.me/541131917009" target="_blank" class="btn-unified" style="background: white; color: var(--primary-dark); font-weight: bold; border: none; padding: 0.9rem 2rem; border-radius: 50px; display: inline-flex; align-items: center; gap: 0.5rem;">
                            <i class="fab fa-whatsapp" style="color: #25D366; font-size: 1.2rem;"></i> Escribinos
                        </a>
                        <a href="https://www.instagram.com/fliaaristimuno/" target="_blank" class="btn-unified" style="background: rgba(255,255,255,0.15); color: white; border: 2px solid rgba(255,255,255,0.4); font-weight: bold; padding: 0.9rem 2rem; border-radius: 50px; display: inline-flex; align-items: center; gap: 0.5rem; backdrop-filter: blur(4px);">
                            <i class="fab fa-instagram"></i> Acompañanos
                        </a>
                    </div>
                </div>
            </div>"""
content = content.replace(old_proj, new_proj)

with open("evento-detalle.html", "w") as f:
    f.write(content)
