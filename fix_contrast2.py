with open("evento-detalle.html", "r") as f:
    content = f.read()

# Change the background of .proyecto-highlight to a very dark solid color, not a gradient
old_bg = "background: linear-gradient(135deg, #005a5e 0%, #001a3d 100%);"
new_bg = "background: #0f172a; /* Solid very dark slate for maximum contrast */\n            box-shadow: inset 0 0 0 2px rgba(255,255,255,0.1), 0 10px 30px rgba(0,0,0,0.15);"
content = content.replace(old_bg, new_bg)

# Make paragraph even bigger and bolder
old_p_css = """        .proyecto-highlight p {
            font-size: 1.15rem;
            font-weight: 500;
            line-height: 1.8;
            opacity: 1;
            max-width: 650px;
            margin: 0 auto 2.5rem;
            text-shadow: 0 1px 3px rgba(0,0,0,0.4);
        }"""
new_p_css = """        .proyecto-highlight p {
            font-size: 1.25rem;
            font-weight: 600;
            line-height: 1.8;
            opacity: 1;
            max-width: 700px;
            margin: 0 auto 2.5rem;
            color: #f8fafc; /* Very light slate */
            text-shadow: 0 2px 4px rgba(0,0,0,0.8);
        }"""
content = content.replace(old_p_css, new_p_css)

with open("evento-detalle.html", "w") as f:
    f.write(content)
