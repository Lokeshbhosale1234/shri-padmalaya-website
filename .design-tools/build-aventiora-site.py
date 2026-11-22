from pathlib import Path
import hashlib, shutil
root=Path(__file__).resolve().parents[1]
backup=root/'backups/pre-aventiora-main-index.html'
if not backup.exists(): shutil.copy2(root/'index.html',backup)
places=[('kerala','Kerala','केरळ','A gentler rhythm.','निवांत सफर.','Traditional Kerala houseboat cruising a palm-lined backwater'),('agra','Agra','आग्रा','A timeless kind of wonder.','कालातीत सौंदर्य.','The Taj Mahal framed by its grand entrance arch'),('jaipur','Jaipur','जयपूर','Follow the colours.','रंगांच्या वाटेने.','The intricately carved pink facade of Hawa Mahal, Jaipur'),('varanasi','Varanasi','वाराणसी','Some mornings stay with you.','मनात राहणारी सकाळ.','Wooden boats on the Ganges beside the historic Varanasi ghats'),('rail','The Himalayas','हिमालय','Take the scenic way.','निसर्गरम्य वाटेने.','Wide Himalayan mountain landscape at Rohtang Pass')]
cards=[]
for index,(id,en,mr,desc,desc_mr,alt) in enumerate(places):
    cards.append(f'<article class="destination destination-{index}" data-reveal><button class="destination-button" type="button" data-journey="{id}" aria-label="Explore {en}"><div class="destination-image"><img src="assets/travel/{id}.webp" alt="{alt}" width="1200" height="1400" loading="lazy" data-parallax><span class="destination-arrow" aria-hidden="true">↗</span></div><div class="destination-caption"><h3 data-en="{en}" data-mr="{mr}">{en}</h3><span data-en="{desc}" data-mr="{desc_mr}">{desc}</span></div></button></article>')
html=(root/'.design-tools/aventiora-site.template.html').read_text(encoding='utf8').replace('DESTINATION_CARDS','\n'.join(cards))
html=html.replace('assets/travel/ocean.webm','assets/travel/ocean-film.mp4').replace('assets/travel/coast.webm','assets/travel/coast-film.mp4')
html=html.replace('assets/travel/ocean-film.mp4','assets/travel/hero-film.mp4').replace('assets/travel/ocean.webp','assets/travel/hero.webp')
logo='<span class="brand-emblem" aria-hidden="true"><span class="brand-badge"><img src="assets/logo.webp" alt="" width="201" height="129"></span><span class="brand-hover-symbol">✳</span></span>'
html=html.replace('<span class="brand-symbol" aria-hidden="true">✳</span>',logo)
html=html.replace('<span class="brand-symbol">✳</span>',logo)
for name in ['css','js']:
    content=(root/f'.design-tools/aventiora-site.{name}').read_bytes()
    (root/f'assets/aventiora-site.{name}').write_bytes(content)
version=hashlib.sha256(html.encode()+(root/'assets/aventiora-site.css').read_bytes()+(root/'assets/aventiora-site.js').read_bytes()).hexdigest()[:12]
(root/'index.html').write_text(html.replace('VERSION',version),encoding='utf8')
print('Built Aventiora-inspired Shri Padmalaya',version)
