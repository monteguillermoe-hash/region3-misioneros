with open("zamorano-detalle.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('class_=', 'class=')

with open("zamorano-detalle.html", "w", encoding="utf-8") as f:
    f.write(content)
