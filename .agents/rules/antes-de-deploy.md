---
trigger: always_on
---

Objetivo:
Trabajar en el proyecto web de manera local, probando cambios en index.html y demás archivos en la computadora. El sistema NO debe subir nada a GitHub ni Netlify hasta que se dé la orden explícita de deploy.

Reglas:

1. Guardar todos los cambios en la carpeta local del proyecto (/Users/guillermomonte/Downloads/PAGINA WEB).
2. Permitir que el usuario abra index.html en el navegador para revisar cómo se ve.
3. No ejecutar comandos de git push ni subir a Netlify automáticamente.
4. Solo cuando el usuario escriba la orden "Subir a producción" o "Deploy", entonces:
   - Ejecutar git add, git commit y git push.
   - Netlify debe desplegar la nueva versión.
5. Mientras tanto, todo el trabajo se mantiene local y se prueba en la computadora.
