import re, base64, hashlib, os, shutil, json
SRC='/workspace/pureau-concept-site'; OUT='/workspace/pureau-shopify-theme/theme'
shutil.rmtree(OUT, ignore_errors=True)
for d in ['layout','templates','sections','snippets','assets','config','locales']: os.makedirs(f'{OUT}/{d}')
html=open(f'{SRC}/index.html',encoding='utf-8').read()
assert '{{' not in html and '{%' not in html
ext={'image/png':'png','image/jpeg':'jpg','image/svg+xml':'svg','image/webp':'webp','image/gif':'gif'}
seen={}
def rep(m):
    mime,b=m.group(1),m.group(2)
    data=base64.b64decode(b)
    name=f"pz-{hashlib.sha1(data).hexdigest()[:10]}.{ext[mime]}"
    if name not in seen:
        open(f'{OUT}/assets/{name}','wb').write(data); seen[name]=len(data)
    return "{{ '%s' | asset_url }}"%name
html=re.sub(r'data:(image/[a-z+]+);base64,([A-Za-z0-9+/=]+)',rep,html)
assert html.count('data:image')==1 and 'data:image/png;base64,"' in html
for f in os.listdir(f'{SRC}/web/hero'): shutil.copy(f'{SRC}/web/hero/{f}',f'{OUT}/assets/{f}')
html=html.replace('src="web/hero/burragorang.webp"',"src=\"{{ 'burragorang.webp' | asset_url }}\"")
html=html.replace('src="web/hero/hand-bottle.webp"',"src=\"{{ 'hand-bottle.webp' | asset_url }}\"")
old='im.src="web/hero/"+h[0]+".webp"'
assert html.count(old)==1
html=html.replace(old,"im.src=\"{{ 'burragorang.webp' | asset_url | split: 'burragorang.webp' | first }}\"+h[0]+\".webp\"")
assert 'web/' not in html, re.findall(r'.{60}web/.{60}',html)
# --- shared links: keep shoppers on this storefront (works on preview + live) ---
html=html.replace('https://pureau.com.au/collections/products',"{{ routes.collections_url }}/products")
html=html.replace('<a href="https://pureau.com.au/pages/contact" target="_blank" rel="noopener">Contact</a>','<a href="/pages/contact">Contact</a>')
# --- head: home keeps its SEO block; other templates get Shopify page titles ---
t0=html.index('<title>'); t1=html.index('<link rel="icon"')
seo=html[t0:t1]
generic=('<title>{{ page_title }}{% if current_page != 1 %} – Page {{ current_page }}{% endif %} – Pureau</title>\n'
  '{% if page_description %}<meta name="description" content="{{ page_description | escape }}">{% endif %}\n'
  '<link rel="canonical" href="{{ canonical_url }}">\n')
html=html[:t0]+"{% if template.name == 'index' %}"+seo+"{% else %}"+generic+"{% endif %}\n"+html[t1:]
head_end=html.index('</head>'); body_start=html.index('<body>')+len('<body>'); body_end=html.rindex('</body>')
head=html[:head_end]; body=html[body_start:body_end]
# --- split header / footer out of the home body into shared snippets ---
h_end=body.index('<!-- ===== HERO')
header=body[:h_end]; body=body[h_end:]
f0=body.index('<div class="band"><i></i><i></i></div>\n<footer>'); f1=body.index('</footer>')+len('</footer>')
footer=body[f0:f1]; body=body[:f0]+body[f1:]
# hamburger script moves with the header
hs=body.index("<script>\n(function(){\n  var ham = document.getElementById('ham');")
he=body.index('</script>',hs)+len('</script>')
hamjs=body[hs:he]; body=body[:hs]+body[he:]
def anchors(x):
    return re.sub(r'href="#([A-Za-z0-9_-]+)"', r'href="{{ hp }}#\1"', x)
hp="{%- liquid\n  assign hp = ''\n  unless template.name == 'index'\n    assign hp = routes.root_url\n  endunless\n-%}\n"
cart_icon=('<a class="cartbtn" href="{{ routes.cart_url }}" aria-label="Cart ({{ cart.item_count }})">'
  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 4h2l2.4 11.2a2 2 0 0 0 2 1.6h7.7a2 2 0 0 0 2-1.5L21 8H6.2"/><circle cx="10" cy="20.5" r="1.2"/><circle cx="17" cy="20.5" r="1.2"/></svg>'
  '<b id="cartcount"{% if cart.item_count == 0 %} hidden{% endif %}>{{ cart.item_count }}</b></a>')
shop='<a class="shopbtn" href="{{ routes.collections_url }}/products">Shop</a>'
assert header.count(shop)==1
header=anchors(header).replace(shop, shop+cart_icon)
scrolljs="<script>(function(){var n=document.getElementById('nav');if(!n)return;addEventListener('scroll',function(){n.classList.toggle('scrolled',scrollY>10)},{passive:true});})();</script>\n"
from PIL import Image
def wh(x):
    # logos are sized by CSS (height:Npx; width:auto) so intrinsic width/height attrs are safe here
    def f(m):
        n=m.group(1); w,h=Image.open(f'{OUT}/assets/{n}').size
        return m.group(0)+f' width="{w}" height="{h}"'
    return re.sub(r"<img(?: class=\"fl\")? src=\"\{\{ '(pz-[0-9a-f]+\.png)' \| asset_url \}\}\"",f,x)
header=wh(header); footer=wh(footer)
open(f'{OUT}/snippets/site-header.liquid','w',encoding='utf-8').write(hp+header+hamjs+"\n"+scrolljs)
open(f'{OUT}/snippets/site-footer.liquid','w',encoding='utf-8').write(hp+anchors(footer)+"\n")
css="{{ 'pureau-store.css' | asset_url | stylesheet_tag }}\n"
layout=head+css+"{{ content_for_header }}\n</head>\n<body class=\"tpl-{{ template.name }}\">\n{% render 'site-header' %}\n<main id=\"MainContent\" role=\"main\">\n{{ content_for_layout }}\n</main>\n{% render 'site-footer' %}\n</body>\n</html>\n"
open(f'{OUT}/layout/theme.liquid','w',encoding='utf-8').write(layout)
open(f'{OUT}/layout/password.liquid','w',encoding='utf-8').write(head+css+"{{ content_for_header }}\n</head>\n<body class=\"tpl-password\">\n<main id=\"MainContent\" role=\"main\">\n{{ content_for_layout }}\n</main>\n</body>\n</html>\n")
open(f'{OUT}/sections/pureau-home.liquid','w',encoding='utf-8').write("{% # theme-check-disable ImgWidthAndHeight %}\n{%- comment -%} Concept-site images are sized by its own CSS; adding intrinsic width/height would distort them. {%- endcomment -%}\n"+body+'\n{% schema %}{"name":"Pureau home","settings":[]}{% endschema %}\n')
open(f'{OUT}/sections/apps.liquid','w').write('<div style="max-width:1100px;margin:0 auto">{% for block in section.blocks %}{% render block %}{% endfor %}</div>\n{% schema %}{"name":"Apps","tag":"section","blocks":[{"type":"@app"}],"presets":[{"name":"Apps"}]}{% endschema %}\n')
json.dump({"sections":{"main":{"type":"pureau-home","settings":{}},"apps":{"type":"apps","settings":{}}},"order":["main","apps"]},open(f'{OUT}/templates/index.json','w'),indent=2)
# --- storefront templates/sections/snippets/assets live in extra/ (single source, copied in) ---
EXTRA='/workspace/pureau-shopify-theme/extra'
shutil.copytree(EXTRA, OUT, dirs_exist_ok=True)
# NOTE: config/settings_data.json below is a local placeholder only. Always push with
# --ignore config/settings_data.json so the theme editor's App embeds (Instafeed) are kept.
json.dump([{"name":"theme_info","theme_name":"Pureau new","theme_version":"1.0.0","theme_author":"ABH / Pureau","theme_documentation_url":"https://github.com/rharris008/pureau-concept-site","theme_support_url":"https://github.com/rharris008/pureau-concept-site"}],open(f'{OUT}/config/settings_schema.json','w'),indent=2)
json.dump({"current":"Default","presets":{"Default":{}}},open(f'{OUT}/config/settings_data.json','w'),indent=2)
json.dump({"general":{"404":"Page not found"}},open(f'{OUT}/locales/en.default.json','w'),indent=2)
print('extracted',len(seen),'images', sum(seen.values()),'bytes')
for p in ['layout/theme.liquid','snippets/site-header.liquid','snippets/site-footer.liquid','sections/pureau-home.liquid']: print(p, os.path.getsize(f'{OUT}/{p}'))
