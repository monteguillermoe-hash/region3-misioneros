# Misiones Región 3 - UAD Argentina

Bienvenido al proyecto web de misiones de la Región 3. Este documento explica cómo mantener y actualizar el sitio digital.

## Estructura de Archivos

- **`index.html`**: Contiene toda la estructura y contenido del sitio. Aquí puedes cambiar los textos de bienvenida, agregar los nombres de eventos o editar la información de los misioneros.
- **`estilos.css`**: Contiene los colores, tipografías y el diseño general. Para cambiar el color principal (actualmente naranja cálido), busca la variable `--primary-color` en la parte superior.
- **`script.js`**: Controla las interacciones de animación, el comportamiento del menú en móviles y la simulación del formulario de oración.
- **`assets/images/`**: Aquí se encuentran las imágenes utilizadas. Si deseas cambiar una imagen, simplemente colócala en esta carpeta y actualiza el nombre en el archivo `index.html`, o reemplaza el archivo actual manteniendo el mismo nombre (ej: `hero.png`).

## ¿Cómo editar textos e información?

1. Abre `index.html` en un editor de texto o código (por ejemplo, Visual Studio Code).
2. Busca la sección que deseas editar. Si necesitas modificar el correo electrónico de contacto, busca `info@comunidaddefe.com` casi al final del documento.
3. Guarda el archivo. Abre `index.html` en tu navegador dando doble clic sobre él para ver los cambios localmente.

## ¿Cómo publicar la página web? (Netlify + GitHub)

El proyecto ya incluye un repositorio Git en la carpeta local, lo que facilita su subida y publicación automática.

1. **Subir a GitHub**:
   - Crea una cuenta en [GitHub](https://github.com/) si no la tienes.
   - Haz clic en el botón '+' y elige "New Repository". Llámalo por ejemplo "iglesia-web". No marques ninguna casilla adicional.
   - Abre tu terminal en la carpeta `PAGINA WEB` y ejecuta estos comandos (reemplazando tu URL):
     ```bash
     git remote add origin https://github.com/TU_USUARIO/iglesia-web.git
     git branch -M main
     git push -u origin main
     ```
2. **Publicar en Netlify con actualización automática**:
   - Ingresa a [Netlify](https://www.netlify.com/).
   - Ve a **"Add new site"** y elige **"Import an existing project"**.
   - Conecta tu cuenta de GitHub, selecciona tu repositorio `iglesia-web` y oprime **"Deploy site"**.
   - ¡Página en vivo! En segundos Netlify te asignará una URL gratuita. De ahora en adelante, cada que guardes y "pushees" cambios a GitHub, la página web se actualizará sola.
