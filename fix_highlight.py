with open("evento-detalle.html", "r") as f:
    content = f.read()

import re

# 1. Update the CSS for .proyecto-highlight
css_pattern = r"\.proyecto-highlight \{.*?\.proyecto-actions \{.*?justify-content: center;\n        \}"
# Wait, let's just replace the whole CSS block for proyecto-highlight
# We can find it by doing a regex or simply replacing everything between .proyecto-highlight { and .recurso-card {
# Let's see the CSS structure.
