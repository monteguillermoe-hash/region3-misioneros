import re
with open("script.js", "r") as f:
    content = f.read()

new_missionary = """{
            id: 'sepulveda-belarde',
            name: 'Familia Sepúlveda Belarde',
            destination: 'El Hoyo — Argentina',
            continent: 'america',
            continentLabel: 'AMÉRICA',
            continentColor: '#16a34a',
            quote: 'Trabajando en Misión Mapuche y discipulado rural en El Hoyo, Chubut.',
            img: 'assets/images/sepulveda_belarde_sept.jpg',
            link: 'sepulveda-belarde.html',
            customImageLink: 'sepulveda-belarde.html',
            coords: [-42.0667, -71.5167],
            whatsapp: ''
        },
        {
            id: 'zamorano',"""

content = content.replace("{\n            id: 'zamorano',", new_missionary)

# Also update Sepúlveda Ramello to have a custom link
content = content.replace(
    "id: 'sepulveda',\n            name: 'Flia. Sep&uacute;lveda Ramello',\n            destination: 'Espa&ntilde;a',\n            continent: 'europa',\n            continentLabel: 'EUROPA',\n            continentColor: '#3b82f6',\n            quote: 'Sirviendo en 5 pa&iacute;ses: hoy con llamado a la iglesia espa&ntilde;ola.',\n            img: 'assets/images/sepulveda_1.png',\n            link: 'https://www.instagram.com/p/DV4CXrMiRmr/?img_index=1',",
    "id: 'sepulveda',\n            name: 'Flia. Sep&uacute;lveda Ramello',\n            destination: 'Espa&ntilde;a',\n            continent: 'europa',\n            continentLabel: 'EUROPA',\n            continentColor: '#3b82f6',\n            quote: 'Sirviendo en 5 pa&iacute;ses: hoy con llamado a la iglesia espa&ntilde;ola.',\n            img: 'assets/images/sepulveda_1.png',\n            link: 'https://www.instagram.com/p/DV4CXrMiRmr/?img_index=1',\n            customImageLink: 'sepulveda-ramello.html',"
)

with open("script.js", "w") as f:
    f.write(content)
