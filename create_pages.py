with open("evento-detalle.html", "r") as f:
    template = f.read()

# BELARDE
belarde = template
belarde = belarde.replace("Familia Aristimuño", "Familia Sepúlveda Belarde")
belarde = belarde.replace("Sudeste Asiático &amp; Arizona · Levantando intercesores para el mundo budista", "El Hoyo, Chubut · Misión Mapuche")
belarde = belarde.replace("https://www.instagram.com/fliaaristimuno/", "#")
belarde = belarde.replace("https://wa.me/541131917009", "#")
belarde = belarde.replace("50.000 intercesores por el mundo budista", "Misión Mapuche y trabajo rural")
belarde = belarde.replace("Misión Posible a Tokyo", "Discipulado Rural en El Hoyo")
belarde = belarde.replace("ASIA — MUNDO BUDISTA", "AMÉRICA — SUR ARGENTINO")
belarde = belarde.replace("Visión", "Ministerio")

# Keep the navbar, replace the body content from "<!-- Viaje a Tokyo -->" down to "<!-- Ofrendas y Donaciones -->"
import re
belarde = re.sub(r'<!-- Viaje a Tokyo -->.*?<!-- Ofrendas y Donaciones -->', """
            <!-- Informe Septiembre -->
            <div class="detalle-bloque reveal" style="margin-bottom: 3rem;">
                <div class="section-header text-center" style="margin-bottom: 2rem;">
                    <span class="tag" style="background: var(--primary-color); color: white; margin-bottom: 1rem;">
                        <i class="fas fa-file-alt"></i> REPORTE DEL MES
                    </span>
                    <h2>Informe Septiembre</h2>
                </div>
                <div class="proyecto-highlight" style="background: white; border-top: 6px solid var(--primary-color); border-radius: 20px; padding: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.06); color: var(--text-dark);">
                    <img src="assets/images/sepulveda_belarde_sept.jpg" style="width:100%; border-radius:12px; margin-bottom: 2rem;">
                    
                    <h3 style="color: var(--primary-dark); font-size: 1.5rem; margin-bottom: 1rem;">Amada iglesia, pastores, familia y amigos:</h3>
                    <p style="font-size: 1.1rem; line-height: 1.8; margin-bottom: 1rem;">Queremos contarles que este mes ha sido de mucha bendición. En primer lugar, porque hemos comenzado a ver el fruto de las visitas que hicimos a las zonas rurales con ayuda de ropa y abrigo.</p>
                    <p style="font-size: 1.1rem; line-height: 1.8; margin-bottom: 1rem;">Hay dos familias que se han comunicado con nosotros, las dos son de origen mapuche y desean que los volvamos a visitar, a una de ellas les estamos enviando los devocionales todos los días y con la otra hablamos por teléfono. Solo el Espíritu Santo puede tocar los corazones y llegar en el momento justo (pedimos oración por ellos, <strong>Carmen y Germán</strong> por su matrimonio/restauración, y <strong>Héctor</strong> por liberación espiritual, está siendo atormentado por los espíritus) quedamos en ir a verle en estos días.</p>
                    <p style="font-size: 1.1rem; line-height: 1.8; margin-bottom: 1rem;">Seguimos trabajando en el Hoyo dando discipulado a dos familias y en este mes se agregó un matrimonio nuevo que hicimos contacto llevándoles ropa y abrigo, él se llama <strong>Julián</strong> y ella <strong>Alejandra</strong> (pedimos oración por sus oraciones, ella está con diálisis y él con problemas de adicción, que Dios traiga libertad, sanidad y vida plena en Jesucristo).</p>
                    <p style="font-size: 1.1rem; line-height: 1.8; margin-bottom: 1.5rem;">De igual manera estamos visitando un barrio donde viven 15 familias con mucha necesidad de Dios, hay muchos niños y los estamos visitando una vez a la semana (pedimos que nos ayuden a orar para comenzar un trabajo entre ellos).</p>
                </div>
            </div>

            <!-- Video Testimonio -->
            <div class="detalle-bloque reveal" style="margin-bottom: 3rem;">
                <div class="section-header text-center" style="margin-bottom: 2rem;">
                    <span class="tag" style="background: #e53935; color: white; margin-bottom: 1rem;">
                        <i class="fab fa-youtube"></i> MATERIAL AUDIOVISUAL
                    </span>
                    <h2>Novedades desde el campo</h2>
                </div>
                <div class="recurso-card" style="padding:0; overflow:hidden; border-radius:20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                    <iframe width="100%" height="450" src="https://www.youtube.com/embed/6ABPNmHV_qw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                </div>
            </div>

            <!-- Motivos de Oración -->
            <div class="detalle-bloque reveal" style="margin-bottom: 4rem;">
                <div class="section-header text-center" style="margin-bottom: 2rem;">
                    <span class="tag" style="background: #dc2626; color: white; margin-bottom: 1rem;">
                        <i class="fas fa-hands-praying"></i> UNIDAD EN ORACIÓN
                    </span>
                    <h2>Pedidos de Oración</h2>
                </div>
                <div class="oracion-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
                    <div class="oracion-card" style="background: white; padding: 1.5rem; border-radius: 12px; border-left: 4px solid var(--primary-color); box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
                        <h4 style="color: var(--primary-dark); margin-bottom: 0.5rem;"><i class="fas fa-car" style="color: #10b981;"></i> Movilidad</h4>
                        <p>Dios es bueno y fiel, ya tenemos arreglada la camioneta, lista para seguir visitando los pueblos y las familias que tanto necesitan a Jesús.</p>
                    </div>
                    <div class="oracion-card" style="background: white; padding: 1.5rem; border-radius: 12px; border-left: 4px solid var(--primary-color); box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
                        <h4 style="color: var(--primary-dark); margin-bottom: 0.5rem;"><i class="fas fa-book" style="color: #3b82f6;"></i> Institutos Bíblicos y Familia</h4>
                        <p>Pedimos de sus oraciones por nosotros como familia, estamos enseñando en los institutos bíblicos. Abigail ya fue a cursar su segundo bimestre de segundo año del IBP, Cami gracias a Dios anda muy bien con el colegio.</p>
                    </div>
                    <div class="oracion-card" style="background: white; padding: 1.5rem; border-radius: 12px; border-left: 4px solid var(--primary-color); box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
                        <h4 style="color: var(--primary-dark); margin-bottom: 0.5rem;"><i class="fas fa-heart" style="color: #e6993a;"></i> Gratitud</h4>
                        <p>Gracias por orar por nosotros, gracias por ser parte, gracias por la generosidad de sus corazones. Los amamos y abrazamos a la distancia.</p>
                    </div>
                </div>
            </div>

<!-- Ofrendas y Donaciones -->""", belarde, flags=re.DOTALL)
belarde = re.sub(r'<!-- Recurso: Cambiar el Mapa Español -->.*?</div>\s*</div>\s*</div>', '', belarde, flags=re.DOTALL) # Clean up leftovers if any

with open("sepulveda-belarde.html", "w") as f:
    f.write(belarde)

# RAMELLO
ramello = template
ramello = ramello.replace("Familia Aristimuño", "Familia Sepúlveda Ramello")
ramello = ramello.replace("Sudeste Asiático &amp; Arizona · Levantando intercesores para el mundo budista", "Europa · Con un llamado a la iglesia española")
ramello = ramello.replace("https://www.instagram.com/fliaaristimuno/", "https://www.instagram.com/p/DV4CXrMiRmr/?img_index=1")
ramello = ramello.replace("https://wa.me/541131917009", "https://wa.me/5493516169210")
ramello = ramello.replace("50.000 intercesores por el mundo budista", "Evangelización, pastoreo y educación cristiana")
ramello = ramello.replace("Misión Posible a Tokyo", "Un nuevo impulso a la iglesia española")
ramello = ramello.replace("ASIA — MUNDO BUDISTA", "EUROPA — ESPAÑA")

ramello = re.sub(r'<!-- Viaje a Tokyo -->.*?<!-- Ofrendas y Donaciones -->', """
            <div class="detalle-bloque reveal" style="margin-bottom: 3rem;">
                <div class="section-header text-center" style="margin-bottom: 2rem;">
                    <span class="tag" style="background: var(--primary-color); color: white; margin-bottom: 1rem;">
                        <i class="fas fa-globe-europe"></i> PROYECTO MISIONERO
                    </span>
                    <h2>España: Un nuevo impulso</h2>
                </div>
                <div class="proyecto-highlight" style="background: white; border-top: 6px solid var(--primary-color); border-radius: 20px; padding: 2.5rem; box-shadow: 0 10px 30px rgba(0,0,0,0.06); color: var(--text-dark); text-align: left;">
                    
                    <p style="font-size: 1.1rem; line-height: 1.8; margin-bottom: 1rem;">Los cristianos evangélicos representan casi el 2% de la población en España. La iglesia española ha crecido de manera exponencial durante los últimos 20 años. Gran parte de este crecimiento se debe a la inmigración especialmente de Latinoamérica.</p>
                    <p style="font-size: 1.1rem; line-height: 1.8; margin-bottom: 1rem;">Creemos que todo este movimiento migratorio es parte de un plan de Dios para dar un nuevo impulso a la iglesia española. Los habitantes de esta nación están siendo alcanzados. Por ahora, los evangélicos representan un reducido porcentaje de la población, pero de a poco los españoles van escuchando el mensaje de salvación.</p>
                    <p style="font-size: 1.1rem; line-height: 1.8; margin-bottom: 1rem;">Otra faceta de la evangelización en España lo constituyen los miles de inmigrantes provenientes de la África subsahariana (musulmanes). De la misma manera que cientos de musulmanes han llegado a esas tierras, Dios ha movilizado a cientos de latinos a la península ibérica para reforzar los esfuerzos que los cristianos españoles han venido haciendo en pro de la evangelización de estas masas de inmigrantes.</p>
                    <p style="font-size: 1.1rem; line-height: 1.8; margin-bottom: 1.5rem;">España (toda Europa en realidad) está atravesando un proceso de cambios en lo que a su demografía se refiere. La migración está cambiando el panorama social de esta nación. Se calcula que de los 45 millones y medio de habitantes, casi el 15% lo constituyen los inmigrantes. No tenemos dudas que Dios controla todos los eventos mundiales que suceden; y la inmigración no es una excepción.</p>
                    <div style="background: var(--bg-light); padding: 1.5rem; border-radius: 12px; border-left: 4px solid var(--secondary-color);">
                        <p style="font-size: 1.15rem; font-style: italic; margin: 0; color: var(--primary-dark);">Después de haber servido en 5 países, siendo Etiopia en donde más permanecimos, Dios, por medio de un llamado claro y especifico, nos habló para unir nuestros esfuerzos a la iglesia española.</p>
                    </div>
                </div>
            </div>

            <div class="detalle-bloque reveal" style="margin-bottom: 3rem;">
                <div class="section-header text-center" style="margin-bottom: 2rem;">
                    <h2>Metas Específicas</h2>
                </div>
                <div class="oracion-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
                    <div class="oracion-card" style="background: white; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #3b82f6; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
                        <h4 style="color: var(--primary-dark); margin-bottom: 0.5rem;"><i class="fas fa-church"></i> Ministerio Pastoral</h4>
                        <p>En una primera etapa serviremos junto a un pastor local (adaptación). En la segunda etapa, nos involucraremos en la actividad pastoral, ya sea estableciendo una nueva congregación o pastoreando una existente carente de pastores.</p>
                    </div>
                    <div class="oracion-card" style="background: white; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #e6993a; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
                        <h4 style="color: var(--primary-dark); margin-bottom: 0.5rem;"><i class="fas fa-globe-africa"></i> Inmigración Africana</h4>
                        <p>Debido a nuestra experiencia transcultural en Etiopia, creemos tener herramientas para poder acercarnos también a personas provenientes de África.</p>
                    </div>
                    <div class="oracion-card" style="background: white; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #10b981; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
                        <h4 style="color: var(--primary-dark); margin-bottom: 0.5rem;"><i class="fas fa-book-open"></i> Educación Cristiana</h4>
                        <p>Ambos somos profesores de institutos bíblicos. Sabemos que la obra en España está creciendo y los obreros necesitan ser capacitados en el ministerio cristiano.</p>
                    </div>
                    <div class="oracion-card" style="background: white; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #dc2626; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
                        <h4 style="color: var(--primary-dark); margin-bottom: 0.5rem;"><i class="fas fa-bullhorn"></i> Promoción de Misiones</h4>
                        <p>Siempre estuvimos en la promoción de la obra. Como directores de la EFM Córdoba participamos en la capacitación de más de cien aspirantes. Queremos compartir esta experiencia con la iglesia española.</p>
                    </div>
                </div>
            </div>

            <div class="detalle-bloque reveal" style="margin-bottom: 4rem;">
                <div class="section-header text-center" style="margin-bottom: 2rem;">
                    <span class="tag" style="background: #dc2626; color: white; margin-bottom: 1rem;">
                        <i class="fas fa-hands-praying"></i> PETICIONES
                    </span>
                    <h2>Motivos de Oración y Necesidades</h2>
                </div>
                <div style="max-width: 600px; margin: 0 auto; background: white; padding: 2rem; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                    <ul style="font-size: 1.1rem; line-height: 1.8; color: var(--text-dark); padding-left: 1.5rem;">
                        <li style="margin-bottom: 0.8rem;">Por <strong>dirección</strong> para conocer el lugar específico donde nos estableceremos.</li>
                        <li style="margin-bottom: 0.8rem;">Por <strong>provisión económica</strong> para compra de pasajes.</li>
                        <li>Por <strong>apertura de iglesias y hermanos</strong> que se comprometerán a apoyarnos en lo económico.</li>
                    </ul>
                    <hr style="margin: 2rem 0; border: 0; border-top: 1px solid #e2e8f0;">
                    <h4 style="color: var(--primary-dark); margin-bottom: 1rem;"><i class="fas fa-address-book"></i> Datos de Contacto</h4>
                    <p style="margin: 0.5rem 0;"><strong>Email:</strong> crisetiope@hotmail.com</p>
                    <p style="margin: 0.5rem 0;"><strong>Facebook:</strong> Cristian Sepulveda – Erica Ramello</p>
                </div>
            </div>

<!-- Ofrendas y Donaciones -->""", ramello, flags=re.DOTALL)
ramello = re.sub(r'<!-- Recurso: Cambiar el Mapa Español -->.*?</div>\s*</div>\s*</div>', '', ramello, flags=re.DOTALL)

with open("sepulveda-ramello.html", "w") as f:
    f.write(ramello)
