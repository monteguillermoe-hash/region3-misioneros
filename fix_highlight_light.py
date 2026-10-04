import re

with open("evento-detalle.html", "r") as f:
    content = f.read()

# Replace CSS
old_css = re.search(r'\.proyecto-highlight \{.*?\n        \.proyecto-actions \{', content, re.DOTALL).group(0)
new_css = """        .proyecto-highlight {
            background: white;
            box-shadow: 0 10px 30px rgba(0,0,0,0.06);
            border-radius: 20px;
            padding: 3.5rem 3rem;
            color: var(--text-dark);
            text-align: center;
            position: relative;
            border-top: 6px solid var(--primary-color);
        }
        .proyecto-icon {
            font-size: 3.5rem;
            margin-bottom: 1.5rem;
        }
        .proyecto-highlight h3 {
            font-size: 2.2rem;
            font-weight: 800;
            color: var(--primary-dark);
            margin-bottom: 1rem;
        }
        .proyecto-highlight p {
            font-size: 1.15rem;
            font-weight: 500;
            line-height: 1.8;
            color: #334155;
            max-width: 700px;
            margin: 0 auto 2.5rem;
        }
        .proyecto-actions {"""
content = content.replace(old_css, new_css)

# Replace buttons in HTML
old_actions = """<div class="proyecto-actions">
                        <a href="https://wa.me/541131917009" target="_blank" class="btn-unified" style="background: white; color: var(--primary-dark); font-weight: bold; border: none; padding: 0.9rem 2rem; border-radius: 50px; display: inline-flex; align-items: center; gap: 0.5rem;">
                            <i class="fab fa-whatsapp" style="color: #25D366; font-size: 1.2rem;"></i> Escribinos
                        </a>
                        <a href="https://www.instagram.com/fliaaristimuno/" target="_blank" class="btn-unified" style="background: rgba(255,255,255,0.15); color: white; border: 2px solid rgba(255,255,255,0.4); font-weight: bold; padding: 0.9rem 2rem; border-radius: 50px; display: inline-flex; align-items: center; gap: 0.5rem; backdrop-filter: blur(4px);">
                            <i class="fab fa-instagram"></i> Acompañanos
                        </a>
                    </div>"""
new_actions = """<div class="proyecto-actions">
                        <a href="https://wa.me/541131917009" target="_blank" class="btn-unified" style="background: var(--primary-color); color: white; font-weight: bold; border: none; padding: 0.9rem 2rem; border-radius: 50px; display: inline-flex; align-items: center; gap: 0.5rem; box-shadow: 0 4px 15px rgba(0,0,0,0.15);">
                            <i class="fab fa-whatsapp" style="font-size: 1.2rem;"></i> Escribinos
                        </a>
                        <a href="https://www.instagram.com/fliaaristimuno/" target="_blank" class="btn-unified" style="background: white; color: var(--primary-color); border: 2px solid var(--primary-color); font-weight: bold; padding: 0.9rem 2rem; border-radius: 50px; display: inline-flex; align-items: center; gap: 0.5rem;">
                            <i class="fab fa-instagram"></i> Acompañanos
                        </a>
                    </div>"""
content = content.replace(old_actions, new_actions)

with open("evento-detalle.html", "w") as f:
    f.write(content)
