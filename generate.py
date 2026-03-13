#!/usr/bin/env python3
import sys, os, json
sys.path.insert(0, '/home/claude')
sys.path.insert(0, '/home/claude/leclubsansgluten')

from imgs import IMG_GUIDE, IMG_BIBLE
from articles_data import ARTICLES
from article_bodies import get_body
from components import (header, footer, share_bar, disclaimer, cta_box,
    popup_html, faq_block, read_progress, testimonials_block,
    head_tags, set_search_data, SALE_URL, GUIDE_URL, DOMAIN, CAT_LABELS, CAT_EMOJI)

BASE = '/home/claude/leclubsansgluten'

def date_str(offset=0):
    from datetime import datetime, timedelta
    d = datetime.now() - timedelta(days=offset)
    months=['janvier','fevrier','mars','avril','mai','juin','juillet','aout','septembre','octobre','novembre','decembre']
    return f"{d.day} {months[d.month-1]} {d.year}"

set_search_data(ARTICLES)

def card_html(a, depth=""):
    return f"""<a href="{depth}{a['cat']}/{a['id']}.html" class="card">
  <div class="card-img-wrap"><img class="card-img" src="{a['img']}" alt="{a['title']}" loading="lazy"/></div>
  <div class="card-body">
    <div class="card-cat">{CAT_EMOJI.get(a['cat'],'')} {CAT_LABELS.get(a['cat'],'')}</div>
    <div class="card-title">{a['title']}</div>
    <div class="card-meta"><span>📅 {date_str()}</span><span>⏱ {a['rt']}</span></div>
  </div>
</a>"""

def related_articles(current_id, cat, count=3):
    related = [a for a in ARTICLES if a['id'] != current_id and a['cat'] == cat][:count]
    if len(related) < count:
        related += [a for a in ARTICLES if a['id'] != current_id and a['cat'] != cat][:count-len(related)]
    return related[:count]

FAQS = {
    "recettes": [
        {"q":"Peut-on utiliser ces recettes si on a la maladie coeliaque ?","a":"Oui, toutes nos recettes sont concues sans gluten. Veillez cependant a verifier que vos ingredients portent la mention sans gluten, car certains produits peuvent contenir des traces."},
        {"q":"Puis-je remplacer une farine par une autre dans ces recettes ?","a":"Chaque farine a des proprietes differentes. Consultez notre guide des farines pour comprendre les substitutions possibles. En general, un mix de farines donne de meilleurs resultats."},
        {"q":"Pourquoi mon pain sans gluten ne leve pas ?","a":"Le pain sans gluten necessite souvent du psyllium pour remplacer le gluten. Verifiez aussi que votre levure est active et que l'eau n'est pas trop chaude (max 40°C)."},
    ],
    "sante": [
        {"q":"Comment savoir si je suis intolérante au gluten ?","a":"Consultez votre medecin generaliste qui prescrira un dosage des anticorps anti-transglutaminase IgA. Ne supprimez pas le gluten avant ce test."},
        {"q":"La sensibilite au gluten non-coeliaque existe-t-elle vraiment ?","a":"Oui, la communaute scientifique reconnait ce syndrome. Il se distingue de la maladie coeliaque par l'absence de lesions intestinales et d'anticorps specifiques."},
        {"q":"Combien de temps pour ressentir les effets du regime sans gluten ?","a":"La plupart des personnes ressentent une amelioration en 2 a 4 semaines. La guerison intestinale complete peut prendre 1 a 2 ans pour les coeliaquees."},
    ],
    "farines": [
        {"q":"Quelle est la meilleure farine sans gluten pour debuter ?","a":"La farine de riz est la plus polyvalente et la plus accessible. Associez-la a de la fecule de mais pour de meilleurs resultats en patisserie."},
        {"q":"Peut-on utiliser une seule farine dans les recettes sans gluten ?","a":"La plupart du temps, non. Les melanges de farines donnent de bien meilleurs resultats car chaque farine apporte des proprietes complementaires."},
        {"q":"Ou acheter des farines sans gluten pas cheres ?","a":"Les grandes surfaces proposent de plus en plus de farines sans gluten a prix raisonnable. Les boutiques bio et les achats en ligne en vrac sont aussi de bonnes options."},
    ],
    "guides": [
        {"q":"Par ou commencer quand on decouvre son intolerance au gluten ?","a":"Commencez par lire les etiquettes et eliminer les sources evidentes de gluten. Notre guide de survie gratuit vous detaille toutes les etapes."},
        {"q":"Le sans gluten est-il vraiment plus cher ?","a":"Les produits transformes sans gluten coutent plus cher, mais une alimentation basee sur des produits naturellement sans gluten (riz, legumes, viandes) n'est pas plus onereuse."},
        {"q":"Peut-on manger sans gluten au restaurant ?","a":"Oui, de plus en plus de restaurants proposent des options sans gluten. Posez toujours des questions sur la contamination croisee et privilegiez les cuisines naturellement sans gluten."},
    ],
}

# ── ARTICLE PAGES ──────────────────────────────────────────────────
for i, a in enumerate(ARTICLES):
    cat, aid, title = a['cat'], a['id'], a['title']
    os.makedirs(f"{BASE}/{cat}", exist_ok=True)

    body = get_body(aid, title, a['excerpt'], cat)
    related = related_articles(aid, cat)
    url = f"{DOMAIN}/{cat}/{aid}.html"
    faqs = FAQS.get(cat, [])
    cta_type = "guide" if cat == "sante" else "bible"

    related_html = "\n".join([f"""<a href="../{r['cat']}/{r['id']}.html" class="related-card">
  <img src="{r['img']}" alt="{r['title']}" loading="lazy"/>
  <div class="related-card-body">
    <div class="related-card-cat">{CAT_EMOJI.get(r['cat'],'')} {CAT_LABELS.get(r['cat'],'')}</div>
    <div class="related-card-title">{r['title']}</div>
  </div>
</a>""" for r in related])

    schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": a['excerpt'],
        "image": a['img'],
        "datePublished": "2025-01-01",
        "publisher": {"@type":"Organization","name":"Le Club Sans Gluten","url": DOMAIN}
    }, ensure_ascii=False)

    html = header(cat, depth="..") + f"""
{head_tags(title + " — Le Club Sans Gluten", a['excerpt'], a['img'], url, depth="..")}
<script type="application/ld+json">{schema}</script>
{read_progress()}
<div class="breadcrumb">
  <a href="/">Accueil</a><span>›</span>
  <a href="/{cat}/">{CAT_EMOJI.get(cat,'')} {CAT_LABELS.get(cat,'')}</a><span>›</span>
  <span>{title}</span>
</div>
<article class="article-wrap">
  <div class="article-cat">{CAT_EMOJI.get(cat,'')} {CAT_LABELS.get(cat,'')}</div>
  <h1 class="article-title">{title}</h1>
  <div class="article-meta">
    <span>📅 {date_str(i%7)}</span>
    <span>⏱ {a['rt']} de lecture</span>
    <span>✍️ Equipe Le Club Sans Gluten</span>
  </div>
  <img class="article-hero" src="{a['img']}" alt="{title}"/>
  <div class="article-body">{body}</div>
  {cta_box(cta_type)}
  {share_bar(title, url)}
  {disclaimer() if cat == 'sante' else ''}
  {faq_block(faqs) if faqs else ''}
  {testimonials_block()}
  <div class="related">
    <h2>Tu pourrais aussi aimer</h2>
    <div class="related-grid">{related_html}</div>
  </div>
</article>
{popup_html()}
""" + footer(depth="..")

    with open(f"{BASE}/{cat}/{aid}.html", 'w', encoding='utf-8') as f:
        f.write(html)

print(f"Generated {len(ARTICLES)} article pages")

# ── CATEGORY PAGES ─────────────────────────────────────────────────
for cat, label in CAT_LABELS.items():
    emoji = CAT_EMOJI.get(cat,'')
    cat_articles = [a for a in ARTICLES if a['cat'] == cat]
    cards = "\n".join([card_html(a, depth="../") for a in cat_articles])
    subcat_html = ""
    if cat == 'recettes':
        subcat_html = """<div class="subcats">
      <button class="subcat active" onclick="filterCat('toutes',this)">Toutes</button>
      <button class="subcat" onclick="filterCat('pain',this)">🍞 Pain</button>
      <button class="subcat" onclick="filterCat('gateaux',this)">🎂 Gateaux</button>
      <button class="subcat" onclick="filterCat('crepes',this)">🥞 Crepes</button>
      <button class="subcat" onclick="filterCat('plats',this)">🍽️ Plats</button>
      <button class="subcat" onclick="filterCat('soupes',this)">🍲 Soupes</button>
    </div>
    <script>
    function filterCat(cat,btn){
      document.querySelectorAll('.subcat').forEach(function(b){b.classList.remove('active')});
      btn.classList.add('active');
      document.querySelectorAll('.cat-search-input').forEach(function(i){i.value=''});
      // Filter would need JS data - show all for now
    }
    </script>"""

    # Category search bar
    search_bar = f"""<div class="cat-search-bar">
    <input type="text" class="cat-search-input" placeholder="🔍 Rechercher dans {label}..." id="catSearch" autocomplete="off"/>
  </div>
  <script>
  var allCards=document.querySelectorAll('.card');
  document.getElementById('catSearch').addEventListener('input',function(){{
    var q=this.value.toLowerCase();
    allCards.forEach(function(c){{
      var t=c.querySelector('.card-title');
      if(t)c.style.display=t.textContent.toLowerCase().indexOf(q)>-1?'':'none';
    }});
  }});
  </script>"""

    html = header(cat, depth="..") + f"""
{head_tags(emoji + " " + label + " sans gluten — Le Club Sans Gluten", "Toutes nos " + label.lower() + " sans gluten testees et approuvees par notre communaute de 100 000 membres.", depth="..")}
<div class="breadcrumb"><a href="/">Accueil</a><span>›</span><span>{emoji} {label}</span></div>
<div class="home-wrap">
  <div class="section-head" style="margin-top:1.5rem">
    <h1 class="section-title">{emoji} {label}</h1>
    <span style="font-size:.78rem;color:var(--gray)">{len(cat_articles)} articles</span>
  </div>
  {subcat_html}
  {search_bar}
  <div class="articles-grid">{cards}</div>
</div>
{popup_html()}
""" + footer(depth="..")

    os.makedirs(f"{BASE}/{cat}", exist_ok=True)
    with open(f"{BASE}/{cat}/index.html", 'w', encoding='utf-8') as f:
        f.write(html)

print("Generated 4 category pages")

# ── HOME PAGE ──────────────────────────────────────────────────────
recettes = [a for a in ARTICLES if a['cat'] == 'recettes'][:6]
sante = [a for a in ARTICLES if a['cat'] == 'sante'][:4]
farines = [a for a in ARTICLES if a['cat'] == 'farines'][:4]
guides = [a for a in ARTICLES if a['cat'] == 'guides'][:4]

def section(title_str, articles_list, cat_id, show_subcats=False):
    emoji = CAT_EMOJI.get(cat_id,'')
    cards = "\n".join([card_html(a) for a in articles_list])
    subcat_html = ""
    if show_subcats:
        subcat_html = """<div class="subcats">
      <button class="subcat active">Toutes</button>
      <button class="subcat">🍞 Pain</button>
      <button class="subcat">🎂 Gateaux</button>
      <button class="subcat">🥞 Crepes</button>
      <button class="subcat">🍽️ Plats</button>
      <button class="subcat">🍲 Soupes</button>
    </div>"""
    return f"""<div>
  <div class="section-head">
    <h2 class="section-title">{emoji} {title_str}</h2>
    <a class="section-link" href="/{cat_id}/">Tout voir →</a>
  </div>
  {subcat_html}
  <div class="articles-grid">{cards}</div>
</div>"""

# Ticker items
ticker_items = "✅ Informations verifiees · 👥 100 000 membres · 🔄 Mis a jour chaque jour · 🎁 Guide de survie GRATUIT · 🏆 Site N°1 sans gluten en France · 🍞 Recettes approuvees par la communaute"
ticker_double = ticker_items + " · " + ticker_items
ticker_spans = "".join([f"<span>{item.strip()}</span>" for item in ticker_double.split("·")])

home_html = header(depth="") + f"""
{head_tags("Le Club Sans Gluten — Recettes et conseils sans gluten N°1 en France", "Recettes sans gluten testees, conseils sante, comparatifs de farines. Rejoins 100 000 femmes qui vivent sans gluten sans se priver.", depth="")}
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"WebSite","name":"Le Club Sans Gluten","url":DOMAIN,"description":"Le site d'information sans gluten N1 en France","potentialAction":{"@type":"SearchAction","target":DOMAIN+"/recettes/?q={{search_term_string}}","query-input":"required name=search_term_string"}}, ensure_ascii=False)}</script>

<div class="welcome-hero">
  <div class="welcome-inner">
    <span class="welcome-eyebrow">🌿 Le site sans gluten N°1 en France</span>
    <h1 class="welcome-title">Vis sans gluten,<br/>sans te priver.</h1>
    <p class="welcome-sub">Recettes testees, conseils sante, comparatifs de farines. Tout ce qu'il faut pour vivre sans gluten en toute confiance. Rejoins 100 000 femmes de notre communaute.</p>
    <div class="welcome-img-cards">
      <a class="welcome-img-card" href="{GUIDE_URL}" target="_blank">
        <img src="/assets/guide.png" alt="Guide de survie de l'intolérante au gluten"/>
        <div class="welcome-img-card-label">🎁 Guide gratuit — Je le veux</div>
      </a>
      <a class="welcome-img-card" href="{SALE_URL}" target="_blank">
        <img src="/assets/bible.png" alt="La Bible des Farines Sans Gluten"/>
        <div class="welcome-img-card-label">📚 La Bible des Farines — Decouvrir</div>
      </a>
    </div>
  </div>
</div>

<div class="reassurance">
  <div class="reassurance-track">{ticker_spans}</div>
</div>

<div class="home-wrap">
  {section("Recettes du moment", recettes, "recettes", show_subcats=True)}
  <div style="margin:3rem 0">{testimonials_block()}</div>
  {section("Sante et Intolerances", sante, "sante")}
  {section("Comparatifs Farines", farines, "farines")}
  {section("Conseils Pratiques", guides, "guides")}
</div>

{popup_html()}
""" + footer(depth="")

with open(f"{BASE}/index.html", 'w', encoding='utf-8') as f:
    f.write(home_html)

print("Generated home page")

# ── A PROPOS PAGE ──────────────────────────────────────────────────
apropos_html = header(depth="") + f"""
{head_tags("A propos — Le Club Sans Gluten", "Decouvrez l'histoire du Club Sans Gluten et notre mission pour aider les femmes intolérantes au gluten.", depth="")}
<div class="breadcrumb"><a href="/">Accueil</a><span>›</span><span>A propos</span></div>
<div class="page-wrap">
  <h1 class="page-title">Notre histoire</h1>
  <img class="page-hero-img" src="https://images.unsplash.com/photo-1556909211-36987daf7b4d?w=1200&q=80" alt="Cuisine sans gluten"/>
  <div class="page-body">
    <p>Le Club Sans Gluten est ne d'une conviction simple : <strong>vivre sans gluten ne devrait pas signifier renoncer au plaisir de manger.</strong> Fonde par une passionnee de nutrition et d'alimentation saine, ce site rassemble aujourd'hui plus de 100 000 femmes en France qui vivent sans gluten au quotidien.</p>
    <h2>Notre mission</h2>
    <p>Nous croyons que l'information de qualite change des vies. Trop de femmes passent des annees a chercher des reponses a leurs symptomes, a rater leurs recettes, a se sentir isolees face aux tables de famille ou aux repas de restaurant.</p>
    <p>Notre mission est de fournir des ressources claires, testees et accessibles pour que chaque femme puisse vivre sans gluten en toute confiance, sans sacrifier le plaisir ni le budget.</p>
    <h2>Ce que nous faisons</h2>
    <p>Chaque recette publiee sur ce site a ete testee dans notre cuisine. Chaque article sur la sante est base sur des sources scientifiques serieuses. Chaque comparatif de farines est le resultat de tests reels, pas de simples specifications fabricant.</p>
    <p>Nous gerons aussi une communaute Facebook de 100 000 membres actives — un espace d'entraide, de partage de recettes et de soutien mutuel.</p>
    <h2>Nos ressources</h2>
    <p>Pour aller plus loin, decouvrez notre <a href="{GUIDE_URL}" target="_blank" style="color:var(--gold);font-weight:700">Guide de Survie de l'Intolérante au Gluten</a> (offert gratuitement) et <a href="{SALE_URL}" target="_blank" style="color:var(--gold);font-weight:700">La Bible des Farines Sans Gluten</a>, notre ressource complete pour maitriser la patisserie sans gluten.</p>
  </div>
</div>
{popup_html()}
""" + footer(depth="")

with open(f"{BASE}/a-propos.html", 'w', encoding='utf-8') as f:
    f.write(apropos_html)

# ── GLOSSAIRE PAGE ─────────────────────────────────────────────────
glossaire_terms = {
    "A": [
        ("Amidon modifie","Ingredient present dans de nombreux produits transformes. Peut etre derive du ble et donc contenir du gluten. Toujours verifier la source."),
        ("Arrow-root","Fecule extraite d'une plante tropicale, naturellement sans gluten. Excellent epaississant transparent pour les sauces."),
    ],
    "C": [
        ("Contamination croisee","Contact accidentel entre aliments sans gluten et sources de gluten. La principale cause de reactions chez les personnes coeliaques."),
        ("Coeliaque","Personne atteinte de la maladie coeliaque, une maladie auto-immune declenchee par l'ingestion de gluten."),
    ],
    "F": [
        ("Farine de riz","Farine naturellement sans gluten, la plus polyvalente pour la patisserie. Gout neutre, texture legere."),
        ("Farine de sarrasin","Farine sans gluten au gout prononce de noisette. Ideale pour les galettes bretonnes et les pains rustiques."),
        ("Fecule de mais","Appele aussi Maizena. Epaississant sans gluten ideal pour les sauces et pour allegerer les preparations."),
    ],
    "G": [
        ("Gluten","Proteine presente dans le ble, le seigle et l'orge. Donne l'elasticite aux pates et du moelleux aux preparations."),
        ("Gomme xanthane","Agent liant sans gluten qui remplace partiellement les proprietes du gluten dans les preparations."),
    ],
    "M": [
        ("Maladie coeliaque","Maladie auto-immune ou l'ingestion de gluten provoque une reaction immunitaire endommageant l'intestin grele. Touche environ 1% de la population."),
        ("Malt","Derive de l'orge, le malt contient du gluten. Present dans certaines cereales de petit-dejeuner, biscuits et boissons."),
    ],
    "P": [
        ("Psyllium","Fibre soluble qui agit comme liant dans les preparations sans gluten. Indispensable pour la boulangerie sans gluten."),
    ],
    "S": [
        ("Sans gluten","Designation qui indique qu'un produit contient moins de 20 ppm de gluten, le seuil tolere par la plupart des personnes coeliaques."),
        ("Sensibilite au gluten non-coeliaque","Condition ou le gluten provoque des symptomes sans les marqueurs biologiques ou les lesions intestinales de la maladie coeliaque."),
    ],
    "T": [
        ("Tapioca","Fecule extraite du manioc, naturellement sans gluten. Donne de la moelleux et de l'elasticite aux preparations."),
    ],
}

glossaire_html = header(depth="") + f"""
{head_tags("Glossaire du sans gluten — Le Club Sans Gluten", "Tous les termes du sans gluten expliques simplement. De la contamination croisee au psyllium.", depth="")}
<div class="breadcrumb"><a href="/">Accueil</a><span>›</span><span>Glossaire</span></div>
<div class="page-wrap">
  <h1 class="page-title">Glossaire du sans gluten</h1>
  <p style="color:var(--gray);margin-bottom:2rem">Tous les termes importants expliques simplement pour mieux comprendre le monde du sans gluten.</p>
  <div class="page-body">
"""
for letter, terms in glossaire_terms.items():
    glossaire_html += f'<div class="glossary-letter">{letter}</div>'
    for term, defn in terms:
        glossaire_html += f'<p class="glossary-term">{term}</p><p class="glossary-def">{defn}</p>'

glossaire_html += f"""
  </div>
  {cta_box("guide")}
</div>
{popup_html()}
""" + footer(depth="")

with open(f"{BASE}/glossaire.html", 'w', encoding='utf-8') as f:
    f.write(glossaire_html)

# ── CALCULATEUR PAGE ───────────────────────────────────────────────
calc_html = header(depth="") + f"""
{head_tags("Convertisseur de farines sans gluten — Le Club Sans Gluten", "Convertissez facilement vos recettes en remplacant la farine de ble par des farines sans gluten.", depth="")}
<div class="breadcrumb"><a href="/">Accueil</a><span>›</span><span>Convertisseur de farines</span></div>
<div class="page-wrap">
  <h1 class="page-title">Convertisseur de farines sans gluten</h1>
  <p style="color:var(--gray);margin-bottom:2rem">Remplacez la farine de ble par des farines sans gluten dans n'importe quelle recette.</p>

  <div class="calc-wrap">
    <h2 class="calc-title">🔄 Je veux remplacer...</h2>
    <div class="calc-row">
      <div class="calc-field">
        <label>Quantite (en grammes)</label>
        <input type="number" id="qty" placeholder="ex: 200" min="1" max="2000"/>
      </div>
      <div class="calc-field">
        <label>Farine de depart</label>
        <select id="fromFlour">
          <option value="ble">Farine de ble</option>
          <option value="riz">Farine de riz</option>
          <option value="sarrasin">Farine de sarrasin</option>
        </select>
      </div>
      <div class="calc-field">
        <label>Profil recette</label>
        <select id="profile">
          <option value="moelleux">Moelleux (gateaux)</option>
          <option value="rustique">Rustique (pain)</option>
          <option value="croustillant">Croustillant (tartes)</option>
        </select>
      </div>
    </div>
    <button class="calc-btn" onclick="calculate()">Calculer mon mix →</button>
    <div class="calc-result" id="calcResult">
      <h3>Ton mix recommande :</h3>
      <div id="calcItems"></div>
      <p style="font-size:.78rem;color:var(--gray);margin-top:.75rem">+ Ajoute 1 a 2 cuilleres a cafe de psyllium pour lier le tout.</p>
    </div>
  </div>

  <script>
  var MIXES = {{
    moelleux: [["Farine de riz",0.6],["Fecule de mais",0.25],["Farine d'amande",0.15]],
    rustique: [["Farine de sarrasin",0.5],["Farine de riz",0.35],["Fecule de tapioca",0.15]],
    croustillant: [["Farine de riz",0.55],["Fecule de mais",0.3],["Farine de coco",0.15]]
  }};
  function calculate(){{
    var qty=parseFloat(document.getElementById('qty').value);
    var profile=document.getElementById('profile').value;
    if(!qty||qty<=0){{alert('Entre une quantite valide');return;}}
    var mix=MIXES[profile];
    var html=mix.map(function(m){{
      return '<div class="calc-result-item"><span>'+m[0]+'</span><span>'+Math.round(qty*m[1])+'g</span></div>';
    }}).join('');
    document.getElementById('calcItems').innerHTML=html;
    document.getElementById('calcResult').classList.add('show');
  }}
  </script>

  <div style="margin-top:2rem;padding:1.25rem;background:var(--gray-light);border-radius:var(--radius)">
    <p style="font-size:.85rem;color:var(--gray);line-height:1.7"><strong>💡 Conseil :</strong> Ces ratios sont des points de depart. Chaque farine reagit differemment selon les recettes. N'hesite pas a ajuster la quantite de liquide selon la consistance obtenue. Pour aller plus loin, <a href="{SALE_URL}" target="_blank" style="color:var(--gold);font-weight:700">La Bible des Farines</a> contient tous les ratios de substitution testes.</p>
  </div>

  {cta_box("bible")}
</div>
{popup_html()}
""" + footer(depth="")

with open(f"{BASE}/calculateur.html", 'w', encoding='utf-8') as f:
    f.write(calc_html)

print("Generated bonus pages (a-propos, glossaire, calculateur)")

# ── SITEMAP ────────────────────────────────────────────────────────
from datetime import datetime
today = datetime.now().strftime('%Y-%m-%d')
urls = [DOMAIN+"/", DOMAIN+"/a-propos.html", DOMAIN+"/glossaire.html", DOMAIN+"/calculateur.html"]
for cat in CAT_LABELS:
    urls.append(f"{DOMAIN}/{cat}/")
for a in ARTICLES:
    urls.append(f"{DOMAIN}/{a['cat']}/{a['id']}.html")

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in urls:
    sitemap += f"  <url><loc>{url}</loc><lastmod>{today}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>\n"
sitemap += "</urlset>"

with open(f"{BASE}/sitemap.xml", 'w') as f:
    f.write(sitemap)

print(f"Sitemap: {len(urls)} URLs")
print(f"\nDONE — {len(ARTICLES)} articles + a-propos + glossaire + calculateur")
