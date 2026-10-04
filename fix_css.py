with open("evento-detalle.html", "r") as f:
    content = f.read()

# Fix the gradient to be darker and more readable
old_bg = "background: linear-gradient(135deg, var(--primary-color) 0%, #003270 100%);"
new_bg = "background: linear-gradient(135deg, #005a5e 0%, #001a3d 100%);"
content = content.replace(old_bg, new_bg)

# Fix paragraph opacity, size, and weight
old_p_css = """        .proyecto-highlight p {
            font-size: 1.1rem;
            line-height: 1.8;
            opacity: 0.88;
            max-width: 650px;
            margin: 0 auto 2.5rem;
        }"""
new_p_css = """        .proyecto-highlight p {
            font-size: 1.15rem;
            font-weight: 500;
            line-height: 1.8;
            opacity: 1;
            max-width: 650px;
            margin: 0 auto 2.5rem;
            text-shadow: 0 1px 3px rgba(0,0,0,0.4);
        }"""
content = content.replace(old_p_css, new_p_css)

with open("evento-detalle.html", "w") as f:
    f.write(content)
