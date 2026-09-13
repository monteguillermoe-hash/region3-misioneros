from bs4 import BeautifulSoup
import re

with open("zamorano-detalle.html", "r") as f:
    soup = BeautifulSoup(f, "html.parser")

# Add Swiper CSS to <head> if not exists
head = soup.find('head')
if not head.find('link', href=re.compile("swiper-bundle.min.css")):
    new_link = soup.new_tag("link", rel="stylesheet", href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css")
    head.append(new_link)

# Transform each div.oracion-grid into a Swiper
grids = soup.find_all("div", class_="oracion-grid")
for grid in grids:
    grid["class"] = ["swiper", "oracionSwiper"]
    grid["style"] = "padding-bottom: 3.5rem;" # Space for pagination
    
    # Create swiper-wrapper
    wrapper = soup.new_tag("div", class_="swiper-wrapper")
    
    # Move all oracion-card children to wrapper
    cards = grid.find_all("div", class_="oracion-card", recursive=False)
    for card in cards:
        slide = soup.new_tag("div", class_="swiper-slide")
        card["style"] = "height: 100%; display: flex; flex-direction: column;"
        slide.append(card.extract())
        wrapper.append(slide)
        
    grid.append(wrapper)
    
    # Add pagination
    pagination = soup.new_tag("div", class_="swiper-pagination")
    grid.append(pagination)

# Add script at the end of body if not exists
body = soup.find('body')
if not soup.find('script', src=re.compile("swiper-bundle.min.js")):
    script_src = soup.new_tag("script", src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js")
    script_inline = soup.new_tag("script")
    script_inline.string = """
    document.addEventListener('DOMContentLoaded', () => {
        const swipers = document.querySelectorAll('.oracionSwiper');
        swipers.forEach(swiperEl => {
            new Swiper(swiperEl, {
                slidesPerView: 1,
                spaceBetween: 20,
                pagination: {
                    el: swiperEl.querySelector('.swiper-pagination'),
                    clickable: true,
                },
                breakpoints: {
                    640: { slidesPerView: 2, spaceBetween: 20 },
                    1024: { slidesPerView: 3, spaceBetween: 30 }
                }
            });
        });
    });
    """
    body.append(script_src)
    body.append(script_inline)

with open("zamorano-detalle.html", "w", encoding="utf-8") as f:
    f.write(str(soup))
