import sys, json
sys.path.insert(0, '/home/claude')
from imgs import IMG_GUIDE, IMG_BIBLE

SALE_URL = "https://www.whynottraining.fr/ed790464"
GUIDE_URL = "https://www.whynottraining.fr/08c32d2c-1fbf916c-b0fd38be-d95c800f-ee160319-0993e605"
DOMAIN = "https://leclubsansgluten.com"
GA_ID = "G-XXXXXXXXXX"
FB_PIXEL = "XXXXXXXXXXXXXXXXX"

CAT_LABELS = {
    "recettes": "Recettes",
    "sante": "Sante",
    "farines": "Farines",
    "guides": "Conseils"
}
CAT_EMOJI = {
    "recettes": "🍞",
    "sante": "🌿",
    "farines": "⚖️",
    "guides": "📖"
}

TESTIMONIALS = [
    {"name":"Marie L.","text":"J'ai enfin trouve des recettes qui fonctionnent vraiment ! Mon pain sans gluten est devenu ma fierte.","stars":5},
    {"name":"Sophie M.","text":"Ce site m'a sauve la mise quand j'ai decouvert mon intolerance. Clair, complet, fiable.","stars":5},
    {"name":"Celine R.","text":"La Bible des Farines a tout change pour moi. Je ne rate plus mes gateaux depuis.","stars":5},
    {"name":"Isabelle T.","text":"Enfin un site serieux sur le sans gluten, avec de vraies recettes testees. Merci !","stars":5},
]

_SEARCH_DATA = "[]"

def set_search_data(articles):
    global _SEARCH_DATA
    data = [{"id":a["id"],"cat":a["cat"],"title":a["title"],"excerpt":a["excerpt"]} for a in articles]
    _SEARCH_DATA = json.dumps(data, ensure_ascii=False)

def head_tags(title, description, img_url="", canonical="", depth=""):
    return f"""<title>{title}</title>
<meta name="description" content="{description}"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{description}"/>
<meta property="og:type" content="website"/>
<meta property="og:site_name" content="Le Club Sans Gluten"/>
{('<meta property="og:image" content="'+img_url+'"/>') if img_url else ''}
{('<link rel="canonical" href="'+canonical+'"/>') if canonical else ''}
<meta name="twitter:card" content="summary_large_image"/>
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','{GA_ID}');</script>"""

def header(active_cat="", depth=""):
    nav_items = ""
    for cat, label in CAT_LABELS.items():
        emoji = CAT_EMOJI.get(cat,"")
        active = ' class="active"' if cat == active_cat else ""
        nav_items += f'<a href="{depth}/{cat}/"{active}>{emoji} {label}</a>'
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Lora:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="{depth}/assets/style.css"/>
</head>
<body>
<div class="top-bar">📚 <a href="{SALE_URL}" target="_blank">La Bible des Farines Sans Gluten</a> — Maitrise les farines sans gluten facilement → <a href="{SALE_URL}" target="_blank">Je le veux</a></div>
<header class="site-header">
  <a href="{depth}/" class="logo-wrap">
    <div class="logo">Le Club<em> Sans Gluten</em></div>
    <span class="logo-sub">Le site info sans gluten N°1</span>
  </a>
  <div class="header-search-wrap">
    <input type="text" class="header-search" placeholder="🔍 Rechercher..." id="headerSearch" autocomplete="off"/>
    <div class="search-results" id="searchResults"></div>
  </div>
</header>
<nav class="site-nav"><div class="site-nav-inner">{nav_items}</div></nav>"""

def footer(depth=""):
    return f"""<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-logo">Le Club <span>Sans Gluten</span></div>
    <p class="footer-desc">Le site d'information sans gluten N°1 en France. Recettes testees, conseils sante, comparatifs de farines.</p>
    <div class="footer-links">
      <a href="{GUIDE_URL}" target="_blank">🎁 Guide gratuit</a>
      <a href="{SALE_URL}" target="_blank">📚 La Bible des Farines</a>
      <a href="{depth}/a-propos.html">A propos</a>
      <a href="{depth}/glossaire.html">Glossaire</a>
      <a href="{depth}/calculateur.html">Convertisseur</a>
    </div>
    <p class="footer-legal">© 2025 Le Club Sans Gluten · Tous droits reserves</p>
    <p class="footer-disclaimer">Les informations de ce site sont donnees a titre informatif et ne remplacent pas un avis medical professionnel.</p>
  </div>
</footer>
<div class="sticky-cta" id="stickyCta">
  <a href="{GUIDE_URL}" target="_blank" class="sticky-cta-btn">🎁 Guide gratuit — Je le veux !</a>
  <button class="sticky-cta-close" onclick="document.getElementById('stickyCta').style.display='none'">✕</button>
</div>
<button class="back-to-top" id="backToTop" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">↑</button>
<script>
var SEARCH_DATA={_SEARCH_DATA};
var DEPTH="{depth}";
window.addEventListener('scroll',function(){{
  var s=window.scrollY;
  var btn=document.getElementById('backToTop');
  var cta=document.getElementById('stickyCta');
  if(btn)btn.classList.toggle('visible',s>400);
  if(cta)cta.classList.toggle('visible',s>600);
}});
var inp=document.getElementById('headerSearch');
var res=document.getElementById('searchResults');
if(inp&&SEARCH_DATA.length){{
  inp.addEventListener('input',function(){{
    var q=this.value.toLowerCase().trim();
    if(q.length<2){{res.style.display='none';return;}}
    var matches=SEARCH_DATA.filter(function(a){{return a.title.toLowerCase().indexOf(q)>-1||a.excerpt.toLowerCase().indexOf(q)>-1;}}).slice(0,6);
    if(!matches.length){{res.style.display='none';return;}}
    res.innerHTML=matches.map(function(a){{return '<a href="'+DEPTH+'/'+a.cat+'/'+a.id+'.html" class="search-result-item"><span class="search-result-cat">'+a.cat+'</span><span class="search-result-title">'+a.title+'</span></a>';}}).join('');
    res.style.display='block';
  }});
  document.addEventListener('click',function(e){{if(!inp.contains(e.target))res.style.display='none';}});
}}
</script>
</body></html>"""

def share_bar(title, url):
    t = title.replace("'","%27").replace('"','%22')
    u = url.replace(":","__COLON__").replace("/","__SLASH__")
    return f"""<div class="share-bar">
  <p>Partager :</p>
  <a class="share-btn share-fb" href="https://www.facebook.com/sharer/sharer.php?u={url}" target="_blank">📘 Facebook</a>
  <a class="share-btn share-wa" href="https://wa.me/?text={t}%20{url}" target="_blank">💬 WhatsApp</a>
  <button class="share-btn share-copy" onclick="(function(b){{navigator.clipboard.writeText(b.dataset.url).then(function(){{b.textContent='Copie!';setTimeout(function(){{b.textContent='Copier'}},2000)}})}})(this)" data-url="{url}">🔗 Copier</button>
</div>"""

def disclaimer():
    return """<div class="disclaimer"><strong>Avis medical :</strong> Les informations de cet article sont a titre informatif uniquement. En cas de symptomes, consultez votre medecin.</div>"""

def cta_box(type="bible"):
    if type == "guide":
        return f"""<div class="cta-box">
  <h3>🎁 Telecharge ton guide de survie GRATUIT</h3>
  <p>Telecharge par plus de 20 000 femmes intolérantes pour vivre sans gluten en toute confiance.</p>
  <a class="cta-btn" href="{GUIDE_URL}" target="_blank">Je veux mon guide gratuit →</a>
</div>"""
    return f"""<div class="cta-box">
  <h3>📚 La Bible des Farines Sans Gluten</h3>
  <p>27 farines decryptees, 3 mix magiques, le convertisseur de recettes. Tout ce qu'il te faut.</p>
  <a class="cta-btn" href="{SALE_URL}" target="_blank">Je veux La Bible des Farines →</a>
</div>"""

def faq_block(faqs):
    items = ""
    for faq in faqs:
        items += f"""<div class="faq-item">
  <button class="faq-q" onclick="this.parentElement.classList.toggle('open')">{faq['q']}<span class="faq-icon">+</span></button>
  <div class="faq-a"><p>{faq['a']}</p></div>
</div>"""
    return f'<div class="faq-block"><h2>Questions frequentes</h2>{items}</div>'

def read_progress():
    return """<div class="read-progress" id="readProgress"></div>
<script>window.addEventListener('scroll',function(){{var a=document.querySelector('.article-body');if(!a)return;var pct=Math.min(100,Math.max(0,Math.round(-a.getBoundingClientRect().top/a.offsetHeight*100)));document.getElementById('readProgress').style.width=pct+'%';}});</script>"""

def testimonials_block():
    items = ""
    for t in TESTIMONIALS:
        stars = "★" * t["stars"]
        items += f"""<div class="testimonial-card">
  <div class="testimonial-stars">{stars}</div>
  <p class="testimonial-text">{t['text']}</p>
  <p class="testimonial-name">— {t['name']}</p>
</div>"""
    return f'<div class="testimonials-section"><h2 class="testimonials-title">Ce que dit notre communaute</h2><div class="testimonials-grid">{items}</div></div>'

def popup_html():
    return f"""<div class="popup-overlay" id="popup">
  <div class="popup-box">
    <div class="popup-box-inner">
      <button class="popup-close" onclick="document.getElementById('popup').classList.remove('open')">✕</button>
      <img src="/assets/guide.png" alt="Guide gratuit sans gluten" style="width:100%;display:block"/>
      <div class="popup-content">
        <h3>🎁 Ton guide de survie OFFERT</h3>
        <p>Rejoins 20 000 femmes qui vivent sans gluten sans se priver.</p>
        <a href="{GUIDE_URL}" target="_blank" style="display:block;text-align:center;padding:.9rem;background:var(--gold);color:var(--ink);font-weight:700;border-radius:6px;font-size:.95rem">Je veux mon guide gratuit →</a>
      </div>
    </div>
  </div>
</div>
<script>setTimeout(function(){{if(!localStorage.getItem('popup_shown')){{document.getElementById('popup').classList.add('open');localStorage.setItem('popup_shown','1');}}}},8000);</script>"""
