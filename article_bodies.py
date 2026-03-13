def get_body(aid, title, excerpt, cat):
    fn = BODIES.get(aid)
    if fn:
        return fn()
    return default_body(title, excerpt, cat)

def default_body(title, excerpt, cat):
    return f"""<p class="article-intro">{excerpt}</p>
<p>Cet article est en cours de rédaction. Revenez bientôt pour découvrir notre contenu complet sur ce sujet.</p>"""

def pain_chataigne():
    return """
<p class="article-intro">Le pain sans gluten a longtemps été synonyme de déception — des tranches friables, une mie compacte, un goût fade qui rappelle vaguement le carton. Si tu te reconnais dans cette description, c'est que tu n'as pas encore essayé la farine de châtaigne. Ce trésor de nos forêts françaises transforme complètement l'expérience du pain sans gluten, en apportant une saveur douce et légèrement sucrée, une couleur dorée appétissante, et une mie qui ressemble enfin à du vrai pain.</p>

<p>Cette recette a été testée par plus de 2 300 membres de notre communauté. Elle est devenue la plus partagée sur notre groupe Facebook. Et la raison est simple : elle fonctionne vraiment, même pour les débutantes.</p>

<h2>Pourquoi la farine de châtaigne est-elle si exceptionnelle ?</h2>

<p>La farine de châtaigne est naturellement sans gluten, ce qui en fait une alliée précieuse pour toutes celles qui vivent avec une maladie cœliaque ou une sensibilité au gluten. Mais au-delà de cette caractéristique essentielle, elle possède des qualités nutritionnelles et gustatives qui la placent bien au-dessus de la simple farine de riz.</p>

<p>Côté nutrition, la châtaigne est l'un des rares fruits à contenir des glucides complexes en grande quantité, ce qui en fait une excellente source d'énergie durable. Elle apporte également des fibres, du potassium, du magnésium et des vitamines du groupe B. Son index glycémique est modéré, ce qui évite les pics de glycémie souvent associés aux farines sans gluten ultra-raffinées.</p>

<p>Côté saveur, la châtaigne apporte une douceur naturelle, légèrement sucrée, avec des notes de noisette. Cette richesse aromatique fait que le pain à la farine de châtaigne n'a pas besoin d'être accompagné de grand-chose pour être délicieux — une simple tranche avec du beurre ou une huile d'olive de qualité suffit.</p>

<p>Enfin, côté texture, la farine de châtaigne a une bonne capacité à absorber l'humidité, ce qui aide à obtenir une mie moins sèche et moins friable que la plupart des pains sans gluten. Combinée correctement avec d'autres farines et du psyllium, elle donne un pain qui se tient vraiment bien au tranchage.</p>

<h2>Les ingrédients — ce qu'il faut vraiment utiliser</h2>

<p>Avant de te donner la liste, parlons de quelque chose d'important : la qualité des ingrédients. En boulangerie sans gluten encore plus qu'en boulangerie classique, chaque ingrédient joue un rôle précis. Substituer au hasard peut complètement changer le résultat.</p>

<p><strong>La farine de châtaigne (150g)</strong> — Choisis une farine de châtaigne pure, sans mélange, idéalement issue de l'agriculture biologique. Les marques françaises comme Moulin de la Veyssière ou Celnat proposent d'excellentes farines. Vérifie toujours que la mention "sans gluten" ou "fabriqué dans un atelier sans gluten" apparaît sur l'emballage.</p>

<p><strong>La farine de riz (200g)</strong> — La farine de riz complète donne plus de goût que la farine de riz blanc, mais les deux fonctionnent. La farine de riz apporte la structure de base du pain, sa légèreté.</p>

<p><strong>La fécule de tapioca (50g)</strong> — Ne la remplace pas par de la fécule de maïs dans cette recette. La fécule de tapioca apporte l'élasticité et ce côté légèrement chewy qui manque souvent aux pains sans gluten. C'est elle qui donne cette texture qui "résiste" légèrement sous la dent.</p>

<p><strong>Le psyllium (15g)</strong> — Ingrédient indispensable. Le psyllium est une fibre soluble qui, au contact de l'eau, forme un gel visqueux qui imite le rôle du gluten. Sans lui, ton pain s'effondrera. Utilise du psyllium blond en poudre fine (pas en coques entières).</p>

<p><strong>La levure de boulanger sèche (7g)</strong> — Assure-toi qu'elle est fraîche et active. Pour tester, dissous-la dans de l'eau tiède avec une pincée de sucre — si elle mousse en 10 minutes, elle est bonne.</p>

<p><strong>L'eau tiède (350ml)</strong> — La température de l'eau est cruciale. Trop froide, la levure ne s'active pas. Trop chaude (au-delà de 40°C), tu la tues. La température idéale est entre 35°C et 38°C — agréable au poignet, comme un bain de bébé.</p>

<p><strong>L'huile d'olive (3 cuillères à soupe)</strong> — Elle apporte du moelleux et de la saveur. Tu peux la remplacer par de l'huile de tournesol ou de colza pour un goût plus neutre.</p>

<p><strong>Le sel (1 cuillère à café et demie)</strong> — Le sel renforce la saveur et régule l'activité de la levure. Ne l'oublie pas, mais ne le mets pas en contact direct avec la levure lors de la préparation.</p>

<p><strong>Le sucre (1 cuillère à café)</strong> — Il nourrit la levure et aide à la coloration de la croûte. Tu peux utiliser du sucre blanc, du sucre de canne ou même du miel.</p>

<h2>La recette étape par étape</h2>

<h3>Étape 1 : Activer la levure (10 minutes)</h3>
<p>Dans un petit bol, mélange la levure sèche avec le sucre et 100ml d'eau tiède. Laisse reposer 10 minutes. Tu dois voir apparaître une mousse en surface — c'est le signe que ta levure est active et que ton pain va lever. Si rien ne se passe après 15 minutes, ta levure est morte et il faut en recommencer avec une nouvelle dose.</p>

<h3>Étape 2 : Mélanger les ingrédients secs</h3>
<p>Dans un grand saladier, mélange les farines, la fécule de tapioca, le psyllium et le sel. Mélange bien à la fourchette ou au fouet pour que tout soit homogène. Il est important que le psyllium soit bien réparti dans les farines pour qu'il joue correctement son rôle.</p>

<h3>Étape 3 : Former la pâte</h3>
<p>Ajoute le mélange levure-eau aux ingrédients secs, puis l'huile d'olive et le reste de l'eau tiède. Mélange d'abord à la cuillère en bois, puis travaille la pâte avec les mains pendant 3 à 4 minutes. La pâte à pain sans gluten ne ressemble pas à une pâte classique — elle est plus collante, plus dense. C'est normal. Résiste à l'envie d'ajouter plus de farine.</p>

<p>Si tu as un robot pâtissier avec crochet pétrisseur, tu peux l'utiliser à vitesse moyenne pendant 5 minutes. C'est encore plus facile.</p>

<h3>Étape 4 : La première levée (1h à 1h30)</h3>
<p>Forme une boule avec la pâte et place-la dans le saladier légèrement huilé. Couvre avec un torchon propre humide ou du film alimentaire. Laisse lever dans un endroit chaud (près d'un radiateur, dans un four éteint avec juste la lumière allumée) pendant 1 heure à 1h30. La pâte doit doubler de volume.</p>

<h3>Étape 5 : Façonnage</h3>
<p>Transfère la pâte sur un plan de travail légèrement huilé (pas fariné — la farine extra modifierait l'équilibre de la recette). Façonne-la en forme ovale ou ronde selon ta préférence. Dépose-la dans un moule à cake ou sur une plaque recouverte de papier cuisson. Si tu veux une belle croûte fendue, fais des entailles sur le dessus avec un couteau aiguisé.</p>

<h3>Étape 6 : Deuxième levée (45 minutes)</h3>
<p>Couvre à nouveau et laisse lever 45 minutes supplémentaires. Pendant ce temps, préchauffe ton four à 220°C (chaleur traditionnelle, pas chaleur tournante) avec un plat vide placé sur la sole du four.</p>

<h3>Étape 7 : La cuisson — le moment crucial</h3>
<p>Juste avant d'enfourner, verse un verre d'eau dans le plat vide sur la sole du four. La vapeur créée est le secret de la croûte croustillante. Enfourne ton pain et laisse cuire 35 à 40 minutes. Le pain est cuit quand il sonne creux quand tu tapes sur le dessous.</p>

<p>Laisse refroidir sur une grille au moins 30 minutes avant de trancher. C'est une étape souvent négligée mais cruciale — si tu tranches trop tôt, la mie n'a pas fini de "se fixer" et sera compacte et gommée.</p>

<h2>Les erreurs les plus fréquentes (et comment les éviter)</h2>

<p><strong>Pain qui ne lève pas</strong> — La cause la plus courante est une levure inactive. Toujours tester la levure avant de commencer. Deuxième cause possible : une eau trop chaude qui a tué la levure lors du mélange.</p>

<p><strong>Mie compacte et dense</strong> — Soit la pâte n'a pas assez levé, soit le psyllium n'était pas assez frais. Le psyllium périmé perd sa capacité gélifiante. Vérifie la date de péremption.</p>

<p><strong>Croûte qui ramollit après refroidissement</strong> — Le pain contient encore trop d'humidité. Laisse-le refroidir complètement sur une grille, à l'air libre, sans le couvrir.</p>

<p><strong>Pain qui s'effondre au tranchage</strong> — Pas assez de psyllium, ou psyllium de mauvaise qualité, ou pain tranché trop chaud.</p>

<p><strong>Goût trop prononcé de châtaigne</strong> — Réduis la quantité de farine de châtaigne à 100g et augmente la farine de riz à 250g.</p>

<h2>Variantes et personnalisations</h2>

<p>Une fois que tu maîtrises la recette de base, les possibilités sont infinies. Voici quelques variantes testées et approuvées par notre communauté.</p>

<p><strong>Version aux noix et aux raisins</strong> — Ajoute 80g de noix grossièrement concassées et 60g de raisins secs à la pâte lors du façonnage. Le résultat est un pain rustique parfait pour le petit-déjeuner avec du fromage.</p>

<p><strong>Version aux herbes de Provence</strong> — Incorpore 2 cuillères à soupe d'herbes de Provence et une cuillère à café d'ail en poudre à la pâte. Idéal pour accompagner les soupes et les salades.</p>

<p><strong>Version sucrée</strong> — Ajoute 3 cuillères à soupe de miel, une cuillère à café de cannelle et une pincée de vanille. Tu obtiens un pain sucré parfait pour le goûter des enfants.</p>

<p><strong>Version aux olives et au romarin</strong> — Incorpore 80g d'olives noires dénoyautées et coupées en deux, et une cuillère à soupe de romarin frais haché. Un délice méditerranéen.</p>

<h2>Conservation et congélation</h2>

<p>Le pain sans gluten rassit plus vite que le pain classique, en raison de l'absence de gluten qui retient l'humidité. Voici les meilleures méthodes de conservation.</p>

<p>À température ambiante, ce pain se conserve 2 jours dans un sachet en tissu ou enveloppé dans un torchon propre. Évite les sacs plastiques hermétiques qui favorisent la moisissure.</p>

<p>Au réfrigérateur, tu peux le garder jusqu'à 5 jours, mais il aura tendance à devenir plus dense. Passe-le quelques secondes au grille-pain pour lui redonner vie.</p>

<p>La congélation est la meilleure option pour éviter le gaspillage. Tranche le pain dès qu'il est refroidi, place les tranches sur une plaque et congèle-les individuellement avant de les mettre dans un sac de congélation. Tu peux ainsi sortir exactement le nombre de tranches dont tu as besoin, directement du congélateur au grille-pain.</p>

<h2>Questions fréquentes de notre communauté</h2>

<p><strong>Peut-on remplacer le psyllium par des graines de chia ou de lin ?</strong> — Les graines de chia et de lin moulues peuvent partiellement remplacer le psyllium, mais le résultat sera différent. Utilise environ 20g de graines moulues pour 15g de psyllium. La texture sera légèrement plus lourde.</p>

<p><strong>Peut-on faire cette recette sans robot ?</strong> — Absolument. Les mains fonctionnent très bien pour travailler la pâte sans gluten, qui est moins élastique et moins exigeante physiquement que la pâte classique.</p>

<p><strong>La recette fonctionne-t-elle en machine à pain ?</strong> — Oui, avec le programme "pain sans gluten" si ta machine en possède un. Sinon, utilise le programme le plus court avec une seule levée.</p>

<p><strong>Peut-on utiliser de la levure fraîche ?</strong> — Oui. Remplace 7g de levure sèche par 20g de levure fraîche. Le résultat est souvent encore meilleur, avec une levée plus régulière.</p>

<h2>L'avis de notre communauté</h2>

<p>Cette recette a généré des centaines de retours dans notre groupe Facebook. Ce qui revient le plus souvent : la surprise face à la vraie texture de pain, le fait que même les membres de la famille sans intolérance le trouvent délicieux, et la satisfaction de faire son propre pain maison sans gluten.</p>

<p>Marie-Claire, membre depuis 3 ans, témoigne : "Je faisais du pain sans gluten depuis des années avec des résultats moyens. Cette recette a tout changé. Maintenant je fais deux pains par semaine et mon mari qui n'est pas intolérant en mange autant que moi."</p>

<p>Avec la pratique, tu adapteras les quantités et les variantes à tes préférences. C'est ça la beauté de la boulangerie maison — chaque fournée devient un peu plus "la tienne".</p>"""

def crepes():
    return """
<p class="article-intro">Les crêpes sans gluten, c'est souvent la première recette qu'on essaie quand on découvre son intolérance. Et c'est souvent la première déception. Une pâte qui colle à la poêle, des crêpes qui se déchirent au retournage, une texture élastique qui rappelle la gomme… Si tu as vécu ça, tu n'étais pas seule. Et cette recette va tout changer.</p>

<p>Après avoir testé des dizaines de combinaisons de farines avec notre communauté de 100 000 membres, nous avons trouvé la formule parfaite. Le secret : un duo farine de riz et fécule de maïs, dans les bonnes proportions, avec une astuce de repos qui fait toute la différence.</p>

<h2>Pourquoi les crêpes sans gluten ratent-elles si souvent ?</h2>

<p>Avant de te donner la recette, comprendre pourquoi les crêpes sans gluten posent problème t'aidera à mieux maîtriser la technique. Le gluten, dans une crêpe classique, joue un rôle important : il crée un réseau élastique dans la pâte qui lui permet de s'étaler finement sans se déchirer et de se détacher facilement de la poêle.</p>

<p>Sans gluten, ce réseau n'existe pas. La pâte est plus fragile, plus susceptible de coller et de se déchirer au retournage. Pour y remédier, il faut jouer sur trois leviers : le choix des farines, le repos de la pâte et la technique de cuisson.</p>

<p>Le premier levier, le choix des farines, est le plus important. Certaines farines sans gluten sont trop lourdes (farine de sarrasin pure, farine de coco) pour faire de bonnes crêpes fines. D'autres sont trop fragiles (farine de châtaigne pure). Le mélange farine de riz et fécule de maïs offre le meilleur équilibre entre légèreté et tenue.</p>

<p>Le deuxième levier est le repos. La pâte à crêpes sans gluten bénéficie encore plus que la pâte classique d'un temps de repos. Pendant ce temps, les farines absorbent le liquide et gonflent, créant une pâte plus homogène qui s'étale mieux.</p>

<p>Le troisième levier est la cuisson. Une poêle bien chaude, légèrement huilée avec un papier absorbant, est la clé d'une crêpe qui se décolle facilement.</p>

<h2>Les ingrédients pour des crêpes parfaites</h2>

<p><strong>Farine de riz (150g)</strong> — C'est la base. La farine de riz blanc est plus légère et donne des crêpes plus fines. La farine de riz complet apporte plus de goût et de nutriments. Les deux fonctionnent. Pour une première fois, commence avec la farine de riz blanc pour un résultat plus prévisible.</p>

<p><strong>Fécule de maïs (50g)</strong> — La fécule de maïs (Maïzena) est ce qui donne aux crêpes leur légèreté et leur texture dorée caractéristique. Elle remplace en partie la farine et allège l'ensemble. Ne la remplace pas par de la fécule de pomme de terre qui donnerait une texture trop collante.</p>

<p><strong>Œufs (3)</strong> — Les œufs sont le liant principal dans cette recette. C'est eux qui compensent l'absence de gluten et donnent à la crêpe sa cohésion. Utilise des œufs à température ambiante — sortis du réfrigérateur 30 minutes avant.</p>

<p><strong>Lait (500ml)</strong> — Tu peux utiliser du lait de vache, du lait d'avoine sans gluten certifié, du lait de riz, du lait d'amande ou du lait de soja. Chaque alternative donnera un léger goût différent. Pour des crêpes classiques, le lait de vache reste le meilleur. Pour une version végane, le lait d'avoine sans gluten certifié est excellent.</p>

<p><strong>Beurre fondu (30g)</strong> — Le beurre apporte de la saveur et aide à la cuisson. Pour une version sans lactose, remplace par de l'huile de coco fondue ou de l'huile de tournesol.</p>

<p><strong>Sel (une pincée)</strong> — Même pour des crêpes sucrées, une pincée de sel rehausse les saveurs.</p>

<p><strong>Sucre vanillé (1 sachet)</strong> — Pour des crêpes sucrées. Omets-le pour des crêpes salées.</p>

<h2>La recette pas à pas</h2>

<h3>Étape 1 : Préparer la pâte</h3>
<p>Dans un grand bol, mélange la farine de riz et la fécule de maïs. Creuse un puits au centre et casse-y les œufs. Commence à mélanger en incorporant progressivement les farines depuis les bords vers le centre. Cette technique évite les grumeaux.</p>

<p>Ajoute le lait petit à petit, en continuant à mélanger. Tu peux utiliser un fouet, un mixeur plongeant ou un blender — le mixeur plongeant donne une pâte particulièrement lisse. Ajoute le beurre fondu (refroidi, pas chaud), le sel et le sucre vanillé si tu utilises la version sucrée. Mélange jusqu'à obtenir une pâte parfaitement lisse.</p>

<h3>Étape 2 : Le repos — étape indispensable</h3>
<p>Couvre le bol avec un film alimentaire ou une assiette et place au réfrigérateur pendant au moins 30 minutes. Pour des résultats encore meilleurs, laisse reposer 2 heures ou même toute la nuit. Tu peux préparer la pâte la veille au soir pour des crêpes parfaites le lendemain matin.</p>

<p>Pendant le repos, les amidons des farines absorbent le liquide et gonflent. La pâte devient plus homogène et plus facile à travailler. Si la pâte te semble trop épaisse après le repos, ajoute un peu de lait et mélange.</p>

<h3>Étape 3 : La cuisson</h3>
<p>Fais chauffer une poêle à crêpes antiadhésive (ou une crêpière) à feu moyen-vif. La poêle doit être bien chaude avant de commencer — une goutte d'eau doit "danser" à la surface et s'évaporer immédiatement.</p>

<p>Huile très légèrement la poêle avec un papier absorbant imprégné d'un peu d'huile neutre ou de beurre. L'excès de matière grasse empêche la crêpe de dorer correctement.</p>

<p>Verse une petite louche de pâte (environ 80ml pour une crêpe de 28cm) au centre de la poêle. Immédiatement, incline la poêle dans tous les sens pour étaler la pâte en un disque le plus fin et uniforme possible. Plus tu es rapide dans ce mouvement, plus la crêpe sera fine.</p>

<p>Laisse cuire 1 minute 30 à 2 minutes. La crêpe est prête à être retournée quand les bords commencent à se soulever légèrement et que la surface n'est plus brillante. Glisse une spatule fine sous la crêpe et retourne-la d'un geste vif. Laisse cuire encore 30 secondes à 1 minute.</p>

<h2>L'astuce du premier test</h2>

<p>La première crêpe est toujours sacrifiée — c'est une règle universelle en cuisine. Elle sert à régler la température de la poêle et la quantité d'huile. Ne te décourage pas si elle est ratée. À partir de la deuxième, tu trouveras le bon rythme.</p>

<p>Si tes crêpes collent : la poêle n'est pas assez chaude ou pas assez huilée.</p>
<p>Si tes crêpes brûlent avant d'être cuites : le feu est trop fort, baisse légèrement.</p>
<p>Si tes crêpes sont trop épaisses : ajoute un peu de lait à la pâte.</p>
<p>Si tes crêpes se déchirent au retournage : la pâte manque peut-être d'œufs, ou la crêpe n'est pas encore assez cuite.</p>

<h2>Garnitures sucrées — nos 10 préférées</h2>

<p>La crêpe sans gluten est aussi polyvalente que la crêpe classique. Voici nos garnitures sucrées préférées, toutes naturellement sans gluten ou facilement adaptables.</p>

<p><strong>Beurre-sucre</strong> — La classique indétrônable. Une noisette de beurre, une cuillère de sucre blanc ou de sucre de canne. Simple, parfait.</p>

<p><strong>Nutella maison sans gluten</strong> — Mélange 200g de noisettes torréfiées et mixées, 3 cuillères à soupe de cacao non sucré, 4 cuillères à soupe de sirop d'érable, et 2 cuillères à soupe d'huile de coco. Bien meilleur que l'original.</p>

<p><strong>Compote de pommes maison</strong> — Fais revenir 3 pommes épluchées et coupées en dés avec une cuillère à café de cannelle et une cuillère à soupe de sirop d'érable. 15 minutes à feu doux. Parfait pour le petit-déjeuner.</p>

<p><strong>Citron-sucre</strong> — Un filet de jus de citron frais et une pincée de sucre. La fraîcheur absolue.</p>

<p><strong>Crème de marrons</strong> — Vérifier qu'elle est sans gluten (la plupart le sont), et c'est un accord parfait avec la légère saveur de riz de la crêpe.</p>

<h2>Garnitures salées — pour un repas complet</h2>

<p>Les crêpes salées sans gluten sont parfaites pour un dîner rapide et équilibré. Quelques idées :</p>

<p><strong>Champignons-fromage de chèvre</strong> — Poêle des champignons de Paris avec de l'ail et du persil, ajoute des tranches de fromage de chèvre sur la crêpe chaude. Ferme en quatre. Délicieux.</p>

<p><strong>Épinards-ricotta</strong> — Mélange des épinards cuits égouttés avec de la ricotta, du sel, du poivre et une pincée de noix de muscade. Garnit la crêpe et roule-la.</p>

<p><strong>Saumon fumé-crème fraîche</strong> — Étale une cuillère de crème fraîche, pose 2 tranches de saumon fumé, quelques câpres et de l'aneth frais. Une entrée élégante.</p>

<p><strong>Œuf-jambon-fromage</strong> — Pour une version galette bretonne : casse un œuf directement sur la crêpe dans la poêle, ajoute une tranche de jambon et du comté râpé. Replie les bords.</p>

<h2>Conservation et réchauffage</h2>

<p>Les crêpes sans gluten se conservent bien. Empile-les avec une feuille de papier cuisson entre chaque crêpe pour éviter qu'elles collent. Conserve-les enveloppées dans du film alimentaire au réfrigérateur pendant 2 jours.</p>

<p>Pour les congeler, même technique : papier cuisson entre chaque crêpe, puis dans un sac de congélation. Elles se conservent jusqu'à 2 mois. Pour les réchauffer, passe-les quelques secondes dans une poêle chaude sans matière grasse, ou au micro-ondes 20 secondes entre deux feuilles de papier absorbant humide.</p>

<h2>Version vegan des crêpes sans gluten</h2>

<p>Pour une version sans œufs ni produits laitiers, voici les substitutions qui fonctionnent le mieux. Remplace chaque œuf par une cuillère à soupe de graines de lin moulues mélangées à 3 cuillères à soupe d'eau, et laisse reposer 10 minutes avant d'ajouter à la pâte. Remplace le lait par du lait de riz ou d'avoine sans gluten certifié. Remplace le beurre par de l'huile de coco fondue.</p>

<p>Le résultat est légèrement moins souple que la version avec œufs, mais tout à fait satisfaisant et apprécié dans notre communauté.</p>"""

def gateau_chocolat():
    return """
<p class="article-intro">Il existe des recettes qui font taire tous les sceptiques. Ce gâteau au chocolat sans gluten est l'une d'elles. Moelleux à l'intérieur, légèrement croustillant en surface, avec une intensité chocolatée qui n'a rien à envier aux meilleures pâtisseries parisiennes — et même les membres de la famille sans intolérance en redemandent. Voilà pourquoi c'est notre recette la plus partagée.</p>

<p>Le secret de ce gâteau, c'est d'abord ce qu'il ne contient pas : pas de farine de riz qui donne parfois une texture granuleuse, pas de mélange de farines compliqué à doser. Sa base ? De la poudre d'amande, qui apporte naturellement du moelleux, de la richesse et une légère saveur de noisette qui se marie parfaitement avec le chocolat.</p>

<h2>La poudre d'amande : le secret du moelleux parfait</h2>

<p>La poudre d'amande est naturellement sans gluten et constitue une excellente base pour la pâtisserie sans gluten. Contrairement à la farine de riz ou à d'autres farines sans gluten, elle ne donne pas de texture granuleuse ou sableuse. Au contraire, elle apporte un moelleux naturel et une richesse en saveurs qui se marie parfaitement avec le chocolat.</p>

<p>Sur le plan nutritionnel, la poudre d'amande est bien plus intéressante que la farine de blé ou la plupart des farines sans gluten : riche en protéines végétales, en graisses saines (acides gras mono-insaturés), en vitamine E et en magnésium. Ce gâteau est non seulement délicieux, mais aussi nutritionnellement solide.</p>

<p>La seule chose à savoir : la poudre d'amande ne crée pas de réseau élastique comme la farine. C'est pourquoi cette recette utilise plus d'œufs qu'un gâteau classique — ce sont eux qui assurent la structure.</p>

<h2>Les ingrédients, décryptés</h2>

<p><strong>Chocolat noir 70% (200g)</strong> — La qualité du chocolat fait toute la différence. Utilise un chocolat avec minimum 70% de cacao, naturellement sans gluten (vérifie quand même l'étiquette pour les traces). Un bon Valrhona, Lindt Excellence 70% ou Barry est parfait.</p>

<p><strong>Beurre (150g) ou huile de coco (120g)</strong> — Le beurre donne un résultat plus riche et plus fondant. L'huile de coco est parfaite pour une version sans lactose. Si tu utilises l'huile de coco, la saveur sera légèrement différente mais délicieuse.</p>

<p><strong>Œufs (4)</strong> — Ils sont la structure du gâteau. Utilise des œufs de bonne qualité, à température ambiante. Sépare les blancs des jaunes — les blancs montés en neige sont ce qui donnera de la légèreté au gâteau.</p>

<p><strong>Sucre (150g)</strong> — Tu peux réduire à 120g si tu préfères un gâteau moins sucré, ou utiliser du sucre de coco pour un index glycémique plus bas et une saveur légèrement caramélisée.</p>

<p><strong>Poudre d'amande (150g)</strong> — Préfère la poudre d'amande émondée (sans la peau brune) pour une texture plus fine. Vérifie qu'elle est fabriquée dans un atelier sans gluten.</p>

<p><strong>Cacao en poudre non sucré (2 cuillères à soupe)</strong> — Pour intensifier le goût chocolaté. Le cacao cru est encore mieux nutritionnellement.</p>

<p><strong>Sel (une pincée)</strong> — Le sel intensifie la saveur du chocolat. Ne le néglige pas.</p>

<p><strong>Extrait de vanille (1 cuillère à café)</strong> — Il arrondit les saveurs et complète merveilleusement le chocolat.</p>

<h2>La recette étape par étape</h2>

<h3>Étape 1 : Faire fondre le chocolat</h3>
<p>Casse le chocolat en morceaux et place-le dans un bol avec le beurre coupé en dés. Fais fondre au bain-marie (bol posé sur une casserole d'eau frémissante, sans que le fond du bol touche l'eau) en remuant régulièrement. Tu peux aussi utiliser le micro-ondes par tranches de 30 secondes, en mélangeant entre chaque. Laisse tiédir.</p>

<h3>Étape 2 : Préparer la base</h3>
<p>Dans un grand bol, fouette les jaunes d'œufs avec le sucre jusqu'à ce que le mélange blanchisse et double de volume (environ 3 minutes au fouet électrique). Ajoute le mélange chocolat-beurre tiédi, l'extrait de vanille, le sel et le cacao. Mélange bien. Incorpore ensuite la poudre d'amande et mélange jusqu'à obtenir une pâte homogène.</p>

<h3>Étape 3 : Monter les blancs en neige</h3>
<p>Dans un bol parfaitement propre et sec (la moindre trace de gras empêche les blancs de monter), monte les blancs d'œufs en neige ferme avec une pincée de sel. Les blancs doivent former des pics fermes qui tiennent quand tu retournes le bol.</p>

<h3>Étape 4 : Incorporer les blancs</h3>
<p>C'est l'étape la plus délicate. Incorpore les blancs en neige à la pâte chocolatée en trois fois, avec une spatule souple, par des mouvements amples de bas en haut qui conservent l'air emprisonné dans les blancs. Ne mélange pas vigoureusement — tu perdrais toute la légèreté. La pâte finale doit être aérienne et mousseuse.</p>

<h3>Étape 5 : Cuisson</h3>
<p>Préchauffe le four à 180°C. Beurre et farine (avec de la poudre d'amande ou de la farine de riz) un moule de 22-24cm de diamètre. Verse la pâte et enfourne pour 25 à 30 minutes. Le gâteau est prêt quand une lame de couteau plantée au centre ressort avec quelques miettes humides — pas complètement propre, c'est ce qui garantit le fondant.</p>

<p>Attention : ne cuits pas trop longtemps. Un gâteau au chocolat qui ressort avec une lame parfaitement propre sera sec. L'objectif est un centre encore légèrement fondant.</p>

<h3>Étape 6 : Refroidissement</h3>
<p>Laisse refroidir dans le moule 15 minutes avant de démouler sur une grille. Ce gâteau est meilleur légèrement tiède ou à température ambiante. Il s'améliore même le lendemain, une fois que les saveurs ont eu le temps de se développer.</p>

<h2>La ganache pour aller plus loin</h2>

<p>Pour transformer ce gâteau en dessert de restaurant, prépare une ganache simple. Fais chauffer 150ml de crème entière jusqu'au premier frémissement. Verse sur 150g de chocolat noir haché. Attends 2 minutes, puis mélange jusqu'à obtenir une ganache lisse et brillante. Laisse tiédir et verse sur le gâteau refroidi. Décore de quelques framboises fraîches ou d'éclats de noisettes torréfiées.</p>

<h2>Variantes testées par notre communauté</h2>

<p><strong>Version fondant intense</strong> — Réduis la cuisson à 20 minutes pour un cœur encore plus coulant. Parfait servi tiède avec une boule de glace à la vanille.</p>

<p><strong>Version orange-chocolat</strong> — Ajoute le zeste d'une orange bio et une cuillère à café de Grand Marnier (ou d'extrait d'orange) à la pâte. L'accord orange-chocolat est un classique indémodable.</p>

<p><strong>Version moka</strong> — Ajoute une cuillère à café de café soluble dissous dans une cuillère à soupe d'eau chaude. Le café intensifie le goût du chocolat sans se faire remarquer.</p>

<p><strong>Version menthe-chocolat</strong> — Quelques gouttes d'huile essentielle de menthe alimentaire ou une cuillère à café d'extrait de menthe. Pour les fans de l'association menthe-chocolat.</p>

<h2>Conservation</h2>

<p>Ce gâteau se conserve jusqu'à 4 jours à température ambiante sous une cloche ou dans une boîte hermétique. Au réfrigérateur, il se garde une semaine mais perd un peu de son fondant — pense à le sortir 30 minutes avant dégustation. Il se congèle très bien, en tranches individuelles emballées dans du film alimentaire.</p>"""

def symptomes_gluten():
    return """
<p class="article-intro">Tu te sens souvent fatiguée sans raison apparente ? Tu as des douleurs articulaires qui vont et viennent ? Des éruptions cutanées inexpliquées ? Des maux de tête récurrents ? Ces symptômes, pris individuellement, semblent anodins. Ensemble, ils peuvent signaler une intolérance au gluten que trop de médecins diagnostiquent en moyenne après 6 à 10 ans de symptômes ignorés.</p>

<p>Cet article ne remplace pas un avis médical — seuls des examens biologiques peuvent confirmer une maladie cœliaque ou une sensibilité au gluten. Mais il peut t'aider à mettre des mots sur ce que tu vis et à prendre les bonnes décisions pour ta santé.</p>

<h2>Pourquoi le diagnostic prend-il autant de temps ?</h2>

<p>La maladie cœliaque est paradoxalement l'une des maladies génétiques les plus fréquentes en Europe (elle touche environ 1% de la population), mais aussi l'une des plus mal diagnostiquées. On estime qu'en France, 80% des personnes atteintes ne sont pas diagnostiquées.</p>

<p>Plusieurs raisons expliquent ce retard diagnostique. D'abord, les symptômes sont extrêmement variables d'une personne à l'autre. Contrairement à l'idée reçue, la diarrhée chronique n'est plus le symptôme principal — dans de nombreux cas, surtout chez l'adulte, les symptômes digestifs sont absents ou discrets. Ensuite, les médecins reçoivent en moyenne très peu de formation sur la maladie cœliaque et la sensibilité au gluten. Enfin, les symptômes se chevauchent avec de nombreuses autres pathologies : syndrome du côlon irritable, fibromyalgie, dépression, hypothyroïdie...</p>

<h2>Les 7 symptômes souvent ignorés</h2>

<h3>1. La fatigue chronique inexpliquée</h3>
<p>C'est le symptôme le plus fréquemment rapporté, et le plus souvent ignoré. Une fatigue qui persiste malgré un sommeil suffisant, qui ne s'améliore pas avec le repos, qui touche aussi bien le corps que l'esprit. On parle parfois de "fatigue de plomb" — cette sensation d'avoir des membres lourds dès le matin.</p>

<p>Cette fatigue a une explication biologique claire : quand l'intestin est endommagé par le gluten (chez les coeliaques) ou simplement perturbé (chez les personnes sensibles), l'absorption des nutriments est altérée. Les carences en fer, en vitamine B12, en vitamine D et en magnésium qui en résultent provoquent directement cette fatigue persistante.</p>

<p>Si tu te reconnais dans cette description et que tes bilans sanguins révèlent des carences récurrentes malgré une alimentation équilibrée, c'est un signal à ne pas ignorer.</p>

<h3>2. Le brouillard mental (brain fog)</h3>
<p>Le "brain fog" ou brouillard mental est une expression qui décrit parfaitement ce que de nombreuses personnes intolérantes au gluten ressentent : une difficulté à se concentrer, à trouver ses mots, une mémoire qui flanche, une impression d'avoir "la tête dans du coton". Ce n'est pas de la paresse intellectuelle — c'est un symptôme neurologique documenté.</p>

<p>Des études ont montré que le gluten peut provoquer une réponse inflammatoire qui affecte le fonctionnement du cerveau. Chez certaines personnes, cette réponse se manifeste par une démyélinisation légère des fibres nerveuses — ce qui ralentit la transmission des informations. Des chercheurs de l'Université de Sheffield ont mis en évidence ce phénomène chez des patients coeliaques.</p>

<p>La bonne nouvelle : le brouillard mental est souvent l'un des premiers symptômes à s'améliorer après le début du régime sans gluten, parfois en quelques semaines seulement.</p>

<h3>3. Les douleurs articulaires et musculaires</h3>
<p>Des douleurs aux genoux, aux coudes, aux épaules ou aux doigts qui semblent "migrer" d'une articulation à l'autre, sans cause rhumatologique identifiable — c'est un symptôme qui touche de nombreuses personnes intolérantes au gluten. Souvent diagnostiquées à tort comme de la fibromyalgie ou un rhumatisme, ces douleurs ont en réalité une origine inflammatoire liée au gluten.</p>

<p>Le mécanisme est le suivant : chez les personnes sensibles, la consommation de gluten déclenche une réponse immunitaire. Cette réponse produit des anticorps qui, par réaction croisée, peuvent attaquer d'autres tissus de l'organisme, dont le tissu articulaire. C'est ce qu'on appelle la réponse auto-immune.</p>

<h3>4. Les éruptions cutanées inexpliquées</h3>
<p>La dermatite herpétiforme est la manifestation cutanée de la maladie cœliaque. Elle se présente sous forme de petites cloques très prurigineuses, symétriques, qui apparaissent sur les coudes, les genoux, les épaules et le bas du dos. Elle est diagnostiquée par biopsie cutanée et répond spécifiquement au régime sans gluten.</p>

<p>Mais au-delà de la dermatite herpétiforme, le gluten peut provoquer d'autres manifestations cutanées : eczéma qui résiste aux traitements classiques, psoriasis, urticaire chronique. Ces liens ne sont pas toujours évidents à établir, mais de nombreux membres de notre communauté rapportent une amélioration significative de leur peau après l'éviction du gluten.</p>

<h3>5. Les maux de tête et migraines récurrents</h3>
<p>Des études ont montré une prévalence plus élevée de migraines chez les personnes atteintes de maladie cœliaque non traitée. Dans certains cas, les migraines sont déclenchées dans les heures suivant la consommation de gluten — une piste à explorer si tes migraines semblent liées à certains repas.</p>

<p>Le mécanisme exact n'est pas complètement élucidé, mais on soupçonne une implication de l'inflammation, de la perméabilité intestinale augmentée (qui laisserait passer des molécules inflammatoires dans la circulation sanguine) et des carences nutritionnelles associées à la malabsorption.</p>

<h3>6. Les troubles de l'humeur et l'anxiété</h3>
<p>Le lien entre intestin et cerveau — ce qu'on appelle l'axe intestin-cerveau — est aujourd'hui bien établi scientifiquement. L'intestin est souvent appelé "le deuxième cerveau" car il contient plus de 100 millions de neurones et produit plus de 90% de la sérotonine de l'organisme — le neurotransmetteur du bien-être.</p>

<p>Quand l'intestin est enflammé ou perturbé par le gluten, cette production de sérotonine peut être altérée. Des études ont mis en évidence des taux plus élevés d'anxiété et de dépression chez les personnes coeliaques non traitées. Et un fait remarquable : plusieurs études ont montré une amélioration significative de l'humeur et de l'anxiété après le début du régime sans gluten, même en l'absence d'amélioration des symptômes digestifs.</p>

<h3>7. Les aphtes récurrents et problèmes bucco-dentaires</h3>
<p>Les aphtes buccaux récurrents — ces petites ulcérations douloureuses à l'intérieur des joues, sous la langue ou sur les gencives — peuvent être un signe de malabsorption des nutriments liée à une intolérance au gluten. Notamment, des carences en fer, en zinc, en vitamine B12 et en folates (toutes associées à la maladie cœliaque non traitée) sont connues pour provoquer des aphtes.</p>

<p>L'émail dentaire peut également être affecté : une hypoplasie de l'émail (fragilité anormale de l'émail, taches blanches ou brunes, sillons) est significativement plus fréquente chez les personnes coeliaques. C'est souvent le signe d'une maladie cœliaque qui s'est développée pendant l'enfance, lors de la formation des dents.</p>

<h2>Comment faire le lien avec le gluten ?</h2>

<p>Si plusieurs de ces symptômes te parlent, voici les étapes à suivre — dans l'ordre.</p>

<p><strong>Étape 1 : Tenir un journal alimentaire</strong> — Pendant 2 semaines, note tout ce que tu manges et tous tes symptômes. Essaie d'identifier des corrélations entre la consommation de gluten et l'apparition des symptômes. Les symptômes peuvent survenir immédiatement après, ou 24 à 72 heures plus tard — ce délai complique l'identification.</p>

<p><strong>Étape 2 : Consulter votre médecin avant d'éliminer le gluten</strong> — C'est un point crucial. Pour diagnostiquer la maladie cœliaque, les tests biologiques (anticorps anti-transglutaminase IgA, anti-endomysium) et la biopsie intestinale doivent être réalisés alors que tu consommes encore du gluten. Si tu élimines le gluten avant les tests, les résultats seront faussés.</p>

<p><strong>Étape 3 : Demander un bilan complet</strong> — En plus du dosage des anticorps spécifiques, demande un bilan incluant : NFS (pour détecter une anémie), fer et ferritine, vitamines B12 et D, zinc, folates. Ces carences, si elles sont présentes, sont à la fois un signe de malabsorption et une explication directe de nombreux symptômes.</p>

<p><strong>Étape 4 : L'éviction-réintroduction</strong> — Si les tests biologiques sont négatifs mais que tu suspectes une sensibilité au gluten non-cœliaque, ton médecin pourra te recommander une période d'éviction du gluten (minimum 6 semaines), suivie d'une réintroduction pour observer la réapparition des symptômes. C'est le protocole de référence pour la sensibilité au gluten non-cœliaque.</p>

<h2>La maladie cœliaque vs la sensibilité au gluten : quelle différence ?</h2>

<p>Ce sont deux conditions distinctes qui partagent certains symptômes mais diffèrent sur des points importants.</p>

<p>La maladie cœliaque est une maladie auto-immune. Quand une personne cœliaque ingère du gluten, son système immunitaire attaque la muqueuse de l'intestin grêle, provoquant une destruction des villosités intestinales qui absorbent les nutriments. Cette destruction est mesurable (biopsie) et les anticorps spécifiques sont détectables dans le sang. Elle est permanente et nécessite une éviction totale et à vie du gluten.</p>

<p>La sensibilité au gluten non-cœliaque (SGNC) est une condition plus récemment reconnue. Les personnes qui en souffrent présentent des symptômes similaires à la maladie cœliaque, mais sans les marqueurs biologiques ni les lésions intestinales caractéristiques. La SGNC n'est pas auto-immune, son mécanisme est moins bien compris, et dans certains cas elle peut être réversible.</p>

<h2>Quand consulter en urgence</h2>

<p>Certains symptômes nécessitent une consultation rapide sans attendre : perte de poids non intentionnelle importante, diarrhées sévères prolongées, sang dans les selles, douleurs abdominales intenses. Ces signes peuvent indiquer une maladie cœliaque non traitée avec des complications, ou d'autres pathologies digestives qui nécessitent un avis médical rapide.</p>"""

def farines_riz_sarrasin():
    return """
<p class="article-intro">Farine de riz ou farine de sarrasin ? C'est souvent la première question qu'on se pose quand on passe au sans gluten. Ces deux farines sont les plus utilisées, les plus accessibles, et les plus polyvalentes. Mais elles n'ont pas du tout les mêmes propriétés, les mêmes saveurs, ni les mêmes applications. Ce guide complet va t'aider à comprendre laquelle utiliser, quand, et comment — pour ne plus jamais rater une recette.</p>

<h2>La farine de riz : la polyvalente incontournable</h2>

<p>La farine de riz est la farine sans gluten de référence dans le monde entier. En Asie, elle est utilisée depuis des millénaires pour préparer des nouilles, des gâteaux de riz, des crêpes de riz. En Europe, elle est devenue la base de la plupart des mélanges de farines sans gluten industriels et maison.</p>

<h3>Profil nutritionnel</h3>
<p>La farine de riz blanc est pauvre en fibres (environ 2g pour 100g) mais facile à digérer, ce qui en fait un excellent choix pour les personnes aux intestins sensibles. La farine de riz complet conserve le son et le germe du grain, ce qui lui confère plus de fibres (3-4g pour 100g), plus de vitamines B, plus de magnésium et un index glycémique légèrement plus bas.</p>

<p>Ni l'une ni l'autre n'est une source significative de protéines (environ 6-7g pour 100g) — un point à garder en tête quand on construit des repas équilibrés sans gluten.</p>

<h3>Saveur et texture</h3>
<p>La farine de riz blanc a un goût neutre, presque absent — ce qui est à la fois sa force et sa faiblesse. Sa force, c'est qu'elle ne domine pas les autres saveurs dans une recette. Sa faiblesse, c'est qu'elle peut donner des préparations qui manquent de caractère si elle est utilisée seule.</p>

<p>La farine de riz complet a un goût légèrement plus prononcé, avec une note de noisette douce. Elle apporte plus de complexité aromatique.</p>

<p>En termes de texture, la farine de riz peut avoir tendance à donner des préparations légèrement granuleuses ou "savelleuses" si mal dosée. Pour éviter cet écueil, il est recommandé de la tamiser avant utilisation et de la combiner avec des fécules qui adoucissent la texture.</p>

<h3>Meilleures applications</h3>
<p>La farine de riz excelle dans les préparations où l'on cherche légèreté et discrétion gustative : gâteaux moelleux, muffins, crêpes légères, pâtes à tarte, panes à la farine, béchamels, sauces. Elle est aussi très utilisée dans les mélanges de farines pour donner de la structure sans alourdir.</p>

<h2>La farine de sarrasin : la rustique au caractère</h2>

<p>La farine de sarrasin (ou farine de blé noir, malgré son nom) est l'une des plus anciennes farines utilisées en France, notamment en Bretagne pour les célèbres galettes. Elle est naturellement sans gluten, bien que son nom puisse prêter à confusion — elle n'est pas liée au blé.</p>

<h3>Profil nutritionnel</h3>
<p>La farine de sarrasin est nutritionnellement supérieure à la farine de riz sur presque tous les plans. Elle est plus riche en protéines (environ 13g pour 100g), avec un profil d'acides aminés plus complet qui inclut la lysine (un acide aminé souvent absent des céréales). Elle est riche en fibres (environ 10g pour 100g), en magnésium, en phosphore, en zinc et en rutine — un flavonoïde aux propriétés antioxydantes.</p>

<p>Son index glycémique est modéré à bas, ce qui en fait un choix intéressant pour les personnes qui surveillent leur glycémie.</p>

<h3>Saveur et texture</h3>
<p>La farine de sarrasin a une saveur très prononcée, terreuse, légèrement amère, avec des notes de noisette et de malt. C'est ce qui en fait une farine au "caractère" — certains l'adorent, d'autres la trouvent trop forte. Elle colore les préparations en brun grisé et leur donne une apparence rustique.</p>

<p>En termes de texture, la farine de sarrasin est dense et absorbe beaucoup d'eau. Elle donne des préparations plus épaisses et lourdes que la farine de riz. Seule, elle peut rendre les gâteaux compacts et friables.</p>

<h3>Meilleures applications</h3>
<p>La farine de sarrasin est souveraine dans les galettes bretonnes — sa saveur corsée et sa texture sont parfaites pour cette application. Elle excelle aussi dans les pains rustiques, les crackers, les blinis, les pâtes fraîches à la saveur prononcée, les pancakes épais, et dans les mélanges pour les recettes où on cherche du caractère et du goût.</p>

<h2>Tableau comparatif</h2>

<p>Pour résumer les différences principales entre ces deux farines :</p>

<p>La farine de riz est neutre en goût, fine en texture, légère, idéale pour la pâtisserie douce et les crêpes. Elle absorbe modérément l'eau et donne des préparations claires. La farine de sarrasin est puissante en goût, plus dense, rustique, idéale pour les galettes et les pains. Elle absorbe beaucoup d'eau et donne des préparations brun-grisé.</p>

<h2>Comment les combiner pour de meilleurs résultats</h2>

<p>La vraie maîtrise des farines sans gluten, c'est de comprendre comment les combiner pour tirer le meilleur de chacune. Voici les combinaisons les plus efficaces.</p>

<p><strong>Pain de campagne rustique</strong> — 40% sarrasin + 40% riz complet + 20% fécule de tapioca. Le sarrasin apporte le goût, le riz apporte la structure, le tapioca apporte l'élasticité.</p>

<p><strong>Galettes salées légères</strong> — 70% sarrasin + 30% riz blanc. Moins dense que la galette 100% sarrasin, mais avec le goût caractéristique.</p>

<p><strong>Gâteau moelleux neutre</strong> — 60% riz blanc + 40% fécule de maïs. Résultat léger, neutre, parfait pour les gâteaux à fruits ou les fondants chocolat.</p>

<p><strong>Pâte à tarte croustillante</strong> — 50% riz blanc + 30% fécule de maïs + 20% farine de sarrasin. Le sarrasin apporte un goût de noisette qui complète parfaitement les tartes salées.</p>

<p><strong>Crêpes légères</strong> — 75% riz blanc + 25% fécule de maïs. Neutre et parfait pour les crêpes sucrées.</p>

<p><strong>Blinis</strong> — 50% sarrasin + 50% riz blanc. Les blinis ont un goût caractéristique légèrement fermenté qui se marie parfaitement avec la saveur du sarrasin.</p>

<h2>Comment conserver ces farines ?</h2>

<p>La conservation des farines sans gluten demande plus d'attention que les farines classiques, car elles ne contiennent pas les agents de conservation naturellement présents dans le gluten.</p>

<p>La farine de riz se conserve jusqu'à 12 mois dans un contenant hermétique à l'abri de la lumière et de l'humidité. Elle peut rancir si elle est exposée à la chaleur — évite de la stocker au-dessus des plaques de cuisson.</p>

<p>La farine de sarrasin, en raison de sa teneur en graisses plus élevée, rancit plus vite. Elle se conserve environ 6 mois à température ambiante, mais jusqu'à 12 mois au réfrigérateur. Si ta farine de sarrasin a une odeur aigre ou rance, jette-la — le goût naturellement prononcé du sarrasin peut masquer le rancissement.</p>

<h2>Où acheter ces farines sans gluten certifiées ?</h2>

<p>C'est une question importante, car même si le riz et le sarrasin sont naturellement sans gluten, les farines peuvent être contaminées lors du processus de fabrication si elles sont produites dans des moulins qui traitent aussi du blé.</p>

<p>Pour les personnes coeliaques, il est indispensable d'utiliser des farines certifiées sans gluten (avec le symbole de l'épi de blé barré). Les marques françaises fiables incluent Celnat, Ma Vie Sans Gluten, Priméal et Bob's Red Mill (pour les commandes en ligne).</p>

<p>Les farines sans gluten certifiées sont disponibles en magasins bio, en grandes surfaces dans le rayon diététique, et en ligne. Acheter en vrac en ligne peut réduire significativement le coût.</p>"""

def guide_debutant():
    return """
<p class="article-intro">Tu viens de découvrir ton intolérance au gluten. Ou tu suspectes d'en avoir une. Ou tu veux simplement comprendre ce que signifie vivre sans gluten au quotidien. Quoi qu'il en soit, tu te retrouves face à une montagne d'informations, souvent contradictoires, parfois anxiogènes. Ce guide est là pour clarifier tout ça — étape par étape, sans jargon médical inutile, avec les conseils qui font vraiment la différence.</p>

<h2>La première semaine : ce qui change vraiment</h2>

<p>La première semaine sans gluten, c'est souvent un mélange de soulagement et d'inquiétude. Soulagement parce que tu as enfin une piste pour expliquer ce que tu vivais. Inquiétude parce que le gluten est partout et que le régime semble impossible à suivre.</p>

<p>Voici la vérité : oui, c'est intimidant au début. Mais non, ce n'est pas impossible. Des millions de personnes vivent sans gluten dans le monde, et la plupart finissent par trouver le régime naturel et peu contraignant. Il faut juste du temps pour apprendre les nouvelles habitudes.</p>

<p>La première semaine, concentre-toi uniquement sur une chose : apprendre à lire les étiquettes. Tout le reste peut attendre.</p>

<h2>Apprendre à lire les étiquettes : la compétence n°1</h2>

<p>En Europe, la réglementation européenne impose que les 14 allergènes majeurs — dont le gluten — soient clairement indiqués sur les étiquettes, en gras ou dans une police différente. C'est une bonne nouvelle. En pratique, cela signifie que tu dois chercher les mots "blé", "orge", "seigle", "avoine" (et "épeautre", "kamut", "triticale") dans la liste des ingrédients.</p>

<p>Mais ce n'est pas tout. Le gluten peut se cacher sous des noms moins évidents : "amidon de blé", "malt d'orge", "protéine de blé hydrolysée", "extrait de malt". Ces mentions signalent toutes la présence de gluten.</p>

<p>Il y a aussi la mention "peut contenir des traces de blé" ou "fabriqué dans un atelier qui utilise du blé". Pour les personnes coeliaques, ces mentions doivent être prises au sérieux — même des traces infimes de gluten peuvent déclencher une réaction. Pour les personnes avec une sensibilité non-cœliaque, le niveau de tolérance peut être plus élevé — à évaluer avec ton médecin.</p>

<h2>Les aliments naturellement sans gluten — la base de ton alimentation</h2>

<p>Avant de te plonger dans les produits "spécial sans gluten" qui peuvent être chers, prends le temps de réaliser que la majeure partie de ton alimentation peut être naturellement sans gluten sans effort ni surcoût.</p>

<p><strong>Tous les légumes frais</strong> — Sans exception. Légumes verts, légumes racines, légumineuses crues, champignons. C'est la base la plus saine et la plus économique.</p>

<p><strong>Tous les fruits frais</strong> — Sans exception. De la pomme à l'avocat, tous les fruits sont naturellement sans gluten.</p>

<p><strong>Les viandes et poissons non transformés</strong> — Le poulet, le bœuf, le porc, le poisson, les fruits de mer sont naturellement sans gluten dans leur forme non transformée. Attention aux marinades, panures, sauces et préparations industrielles.</p>

<p><strong>Les œufs</strong> — Naturellement sans gluten, excellente source de protéines.</p>

<p><strong>Les produits laitiers nature</strong> — Lait, yaourt nature, fromages (attention aux fromages fondus et préparations fromagères qui peuvent contenir des additifs avec gluten).</p>

<p><strong>Les céréales et pseudo-céréales sans gluten</strong> — Riz (blanc, complet, basmati, jasmin, arborio), maïs, quinoa, millet, amarante, sarrasin, teff, sorgho.</p>

<p><strong>Les légumineuses</strong> — Lentilles, pois chiches, haricots secs, fèves, pois cassés. Excellentes sources de protéines et de fibres.</p>

<p><strong>Les oléagineux</strong> — Noix, amandes, noisettes, cajous, pistaches (en version nature, sans assaisonnement).</p>

<p><strong>Les huiles végétales</strong> — Toutes sont sans gluten.</p>

<h2>Les aliments surprenants qui contiennent du gluten</h2>

<p>Au-delà des suspects évidents (pain, pâtes, gâteaux), le gluten se cache dans des produits auxquels on ne pense pas spontanément. Voici les pièges les plus courants.</p>

<p><strong>La sauce soja</strong> — La sauce soja classique (Kikkoman et la plupart des marques) est fabriquée à partir de blé fermenté. Il existe des sauces soja sans gluten (tamari), qui sont généralement indiquées comme telles sur l'étiquette.</p>

<p><strong>La bière</strong> — Fabriquée à partir d'orge maltée, la bière est une source importante de gluten. Des bières sans gluten existent, fabriquées à partir de sorgho ou de riz.</p>

<p><strong>Les bouillons cubes et mélanges d'épices</strong> — Beaucoup contiennent de l'amidon de blé ou de la levure de bière (qui peut être fabriquée à partir d'orge). Vérifie toujours les étiquettes.</p>

<p><strong>Les chips et snacks</strong> — Certaines chips de pommes de terre (comme les Pringles) contiennent de la farine de blé. Les chips plates ordinaires (Lay's, etc.) sont généralement sans gluten mais vérifie l'étiquette.</p>

<p><strong>Les saucisses et charcuteries</strong> — Beaucoup de préparations de charcuterie contiennent des liants à base de blé. Les jambons cuits, saucissons et saucisses industriels sont particulièrement concernés.</p>

<p><strong>Les yaourts aux fruits et desserts lactés</strong> — Certains contiennent de l'amidon modifié ou des céréales. Lis toujours les étiquettes même sur des produits qui semblent "naturels".</p>

<p><strong>Les médicaments et compléments</strong> — L'excipient (substance inactive) de certains médicaments ou compléments alimentaires peut contenir de l'amidon de blé. En cas de doute, demande à ton pharmacien.</p>

<p><strong>La communion religieuse</strong> — L'hostie catholique traditionnelle est faite de pain azyme (farine de blé et eau). Des hosties sans gluten existent — parles-en à ton prêtre.</p>

<h2>Organiser sa cuisine sans gluten</h2>

<p>Si tu es la seule personne dans ton foyer à suivre un régime sans gluten, la cohabitation avec des aliments contenant du gluten demande quelques précautions pour éviter la contamination croisée.</p>

<p><strong>Les ustensiles</strong> — La farine de blé s'incruste dans les rainures des planches à découper en bois, les passoires en plastique et les spatules poreuses. Si possible, dédies-toi des ustensiles : une planche à découper, une passoire, une spatule. Les ustensiles en métal lisse et en verre sont plus faciles à nettoyer et moins susceptibles de retenir des résidus.</p>

<p><strong>Le grille-pain</strong> — Un grille-pain partagé est une source importante de contamination. Les miettes de pain classique persistent et peuvent contaminer tes toasts sans gluten. Idéalement, utilise un grille-pain dédié ou des sachets à grille-pain sans gluten.</p>

<p><strong>Les confitures, beurres et condiments partagés</strong> — Quand quelqu'un trempe son couteau dans le beurre après avoir tartine son pain classique, il laisse des miettes. Solution : avoir tes propres pots, ou toujours te servir avant les autres, ou utiliser des coupelles individuelles.</p>

<p><strong>Les surfaces de préparation</strong> — Nettoie soigneusement les surfaces avant de préparer tes repas, surtout si de la farine de blé a été utilisée récemment. La farine en poudre se dépose partout et résiste aux nettoyages superficiels.</p>

<h2>Manger au restaurant sans gluten</h2>

<p>Manger au restaurant est possible et agréable avec un peu d'organisation. Voici les stratégies qui fonctionnent.</p>

<p><strong>Appelle avant</strong> — Un coup de téléphone avant la réservation te permettra de savoir si le restaurant peut t'accommoder. Les bons restaurants prennent les allergies alimentaires au sérieux et seront heureux de t'expliquer leurs options.</p>

<p><strong>Pose les bonnes questions</strong> — Quand tu commandes, demande non seulement si le plat contient du gluten, mais aussi s'il y a risque de contamination croisée. Une sauce thickened avec de la farine, une plancha utilisée pour des plats panés, une friteuse partagée — tout ça peut contaminer un plat qui semble sans gluten.</p>

<p><strong>Les cuisines naturellement plus sûres</strong> — Certaines cuisines du monde sont naturellement plus adaptées : la cuisine thaïlandaise (base de riz, sauce de poisson), la cuisine mexicaine authentique (tortillas de maïs), la cuisine japonaise avec précautions (le sushi peut contenir de la sauce soja), la cuisine indienne (nombreux plats sans gluten à base de légumineuses et de riz).</p>

<h2>Le budget sans gluten : comment ne pas se ruiner</h2>

<p>C'est l'une des inquiétudes les plus fréquentes. Et elle est légitime : les produits "spécial sans gluten" (pain, pâtes, gâteaux industriels) coûtent en moyenne 2 à 3 fois plus cher que leurs équivalents classiques.</p>

<p>Mais voici la bonne nouvelle : si ton alimentation est basée sur des produits naturellement sans gluten (riz, légumes, viandes, légumineuses, fruits), le budget n'est pas plus élevé qu'une alimentation classique. Les produits "spécial sans gluten" industriels ne doivent pas constituer la base de ton alimentation — ils sont des dépannages pratiques, pas des incontournables.</p>

<p>Les stratégies pour réduire le budget : acheter les farines sans gluten en vrac en ligne (jusqu'à 3 fois moins cher qu'en magasin bio), cuisiner son propre pain (coût divisé par 4 par rapport au pain sans gluten industriel), privilégier les légumineuses comme source de protéines (bien moins chères que la viande), faire ses courses dans les épiceries asiatiques pour le riz en gros (prix bien inférieurs aux grandes surfaces).</p>

<h2>Le premier mois : à quoi s'attendre</h2>

<p>Le premier mois sans gluten est souvent marqué par des hauts et des bas. Certaines personnes ressentent une amélioration spectaculaire dès les premières semaines — énergie retrouvée, digestion apaisée, brouillard mental levé. Pour d'autres, l'amélioration est plus progressive.</p>

<p>Il peut aussi y avoir une période de "manque" — le gluten a un effet légèrement opioïde (les glutéomorphines, fragments de gluten partiellement digérés, se lient aux récepteurs opioïdes du cerveau). Certaines personnes rapportent une légère période d'adaptation les premières semaines.</p>

<p>Patience et bienveillance envers toi-même sont les maîtres mots. Un écart occasionnel ne signifie pas l'échec — note comment tu te sens et utilise ça comme information. Et n'hésite pas à rejoindre notre communauté de 100 000 membres sur Facebook — l'entraide et les conseils pratiques de personnes qui vivent la même chose sont inestimables.</p>"""

def pizza():
    return """
<p class="article-intro">La pizza sans gluten est souvent la plus grande déception culinaire des personnes nouvellement intolérantes. Trop épaisse, qui se brise au pliage, détrempée sous les garnitures, sans le croustillant caractéristique... Ces pizzas-là ressemblent à tout sauf à une pizza. Jusqu'à ce que tu découvres cette recette. La base croustillante qui change tout repose sur un secret simple : un mélange précis de farine de riz et de fécule de tapioca, plus une technique de précuisson que peu de gens connaissent.</p>

<h2>Le secret du croustillant : comprendre pourquoi les pâtes sans gluten ramollissent</h2>

<p>Pour résoudre un problème, il faut d'abord le comprendre. Les pâtes à pizza sans gluten ramollissent pour deux raisons principales.</p>

<p>La première est l'humidité de la garniture. La mozzarella, la sauce tomate, les légumes — tout ça libère de l'humidité pendant la cuisson. Dans une pizza classique, le gluten crée un réseau qui résiste à cette humidité. Sans gluten, la base absorbe l'eau comme une éponge.</p>

<p>La deuxième est la nature même des farines sans gluten. Contrairement à la farine de blé qui forme un réseau élastique et résistant, les farines sans gluten ont tendance à donner des pâtes qui restent molles ou deviennent détrempées.</p>

<p>La solution : précuire la base sans garniture, à haute température, pour qu'elle forme une croûte solide avant d'ajouter les ingrédients humides. Et choisir les bonnes farines — la fécule de tapioca est la clé du croustillant.</p>

<h2>Pourquoi la fécule de tapioca fait toute la différence</h2>

<p>La fécule de tapioca (extraite du manioc) a une propriété unique parmi les fécules : elle donne de l'élasticité et un croustillant particulier aux préparations cuites. C'est l'ingrédient secret de nombreuses pizzas sans gluten réussies.</p>

<p>Elle crée une texture légèrement "chewy" — cette résistance douce sous la dent qui rappelle la vraie pâte à pizza — tout en donnant un croustillant prononcé à la surface. La fécule de maïs donne un résultat plus friable et moins satisfaisant pour la pizza.</p>

<h2>Les ingrédients pour une base parfaite</h2>

<p><strong>Farine de riz (200g)</strong> — La base structurelle. Utilise de la farine de riz fine, bien tamisée.</p>

<p><strong>Fécule de tapioca (80g)</strong> — Le secret du croustillant. Ne la remplace pas par de la fécule de maïs dans cette recette.</p>

<p><strong>Psyllium (10g)</strong> — Le liant qui remplace le gluten. Il donne à la pâte son élasticité et permet de l'étaler sans qu'elle se brise.</p>

<p><strong>Levure sèche (5g)</strong> — Pour une légère levée qui aère la pâte.</p>

<p><strong>Eau tiède (220ml)</strong> — Entre 35 et 38°C.</p>

<p><strong>Huile d'olive (2 cuillères à soupe)</strong> — Pour la saveur et l'élasticité.</p>

<p><strong>Sel (1 cuillère à café)</strong></p>

<p><strong>Sucre (1 cuillère à café)</strong> — Pour activer la levure.</p>

<h2>La recette étape par étape</h2>

<h3>Étape 1 : Préparer la pâte</h3>
<p>Mélange la levure et le sucre avec l'eau tiède. Laisse reposer 10 minutes jusqu'à l'apparition de la mousse. Dans un grand bol, mélange la farine de riz, la fécule de tapioca, le psyllium et le sel. Creuse un puits, ajoute le mélange levure-eau et l'huile d'olive. Mélange jusqu'à former une pâte homogène. Elle sera plus humide et collante qu'une pâte à pizza classique — c'est normal.</p>

<h3>Étape 2 : Repos (30 minutes)</h3>
<p>Couvre la pâte et laisse reposer 30 minutes. Le psyllium va absorber l'humidité et rendre la pâte plus maniable.</p>

<h3>Étape 3 : Étaler la pâte</h3>
<p>Préchauffe le four à 230°C avec la plaque à pizza (ou une pierre à pizza si tu en as une) à l'intérieur — la plaque chaude est cruciale pour le croustillant. Humidifie légèrement tes mains et étale la pâte directement sur une feuille de papier cuisson. Travaille depuis le centre vers les bords en appuyant doucement. Vise une épaisseur de 3-4mm. Relève légèrement les bords pour former une bordure.</p>

<h3>Étape 4 : La précuisson — l'étape secrète</h3>
<p>Fais glisser le papier cuisson avec la pâte sur la plaque chaude. Enfourne pour 8-10 minutes, jusqu'à ce que la surface soit légèrement dorée et que la pâte soit ferme au toucher. C'est l'étape qui change tout — cette précuisson crée la croûte protectrice qui empêchera la base de ramollir sous la garniture.</p>

<h3>Étape 5 : Garnir et cuire</h3>
<p>Sors la base précuite du four. Étale la sauce tomate (pas trop — l'excès d'humidité est l'ennemi), ajoute ta mozzarella et tes garnitures. Remets au four pour 10-12 minutes supplémentaires jusqu'à ce que le fromage soit fondu et doré. Sors du four, laisse reposer 2 minutes, puis tranches et déguste.</p>

<h2>La sauce tomate maison en 5 minutes</h2>

<p>Une bonne pizza commence par une bonne sauce. Voici notre sauce tomate express, qui se prépare en 5 minutes et fait toute la différence.</p>

<p>Dans une petite casserole, fais revenir une gousse d'ail émincée dans une cuillère à soupe d'huile d'olive jusqu'à ce qu'elle soit dorée. Ajoute une boîte de tomates pelées concassées (400g), une pincée d'origan séché, du sel, du poivre et une pincée de sucre pour équilibrer l'acidité. Laisse mijoter 10 minutes à feu doux en remuant de temps en temps. Mixe partiellement pour obtenir une sauce lisse mais avec quelques morceaux. Laisse refroidir avant d'utiliser.</p>

<h2>Garnitures sans gluten : idées et pièges</h2>

<p>La plupart des garnitures classiques sont naturellement sans gluten : mozzarella fraîche, légumes frais, viandes nature, œufs, fromages. Mais certaines garnitures apparemment innocentes peuvent contenir du gluten.</p>

<p>Fais attention aux charcuteries industrielles (certains jambons cuits, lardons, salami peuvent contenir des additifs avec gluten), aux mélanges de fromages râpés (certains contiennent de l'amidon de blé pour éviter le collage), aux sauces pré-préparées (sauce barbecue, sauce curry, etc.).</p>

<p>Nos garnitures préférées qui fonctionnent parfaitement et sont toutes sans gluten : la classique margherita (sauce tomate, mozzarella fraîche, basilic frais), la quatre fromages (mozzarella, gorgonzola, parmesan, chèvre), la chèvre-miel-noix (fromage de chèvre, miel, noix, roquette ajoutée après cuisson), la végétarienne (courgettes, poivrons rôtis, olives, champignons, artichaut).</p>

<h2>Variantes : pizza express et pizza épaisse</h2>

<p><strong>Version express sans levée</strong> — Si tu manques de temps, tu peux sauter l'étape de levée. La pizza sera légèrement moins aérée mais tout à fait satisfaisante. Mélange les ingrédients, étale immédiatement et précuis.</p>

<p><strong>Version pâte épaisse moelleuse</strong> — Pour une pizza style "deep dish" ou une pâte plus épaisse et moelleuse, double les quantités et fais cuire dans un moule à bords hauts. La précuisson sera plus longue (15 minutes) pour que le cœur soit cuit.</p>

<p><strong>Version pâte fine craquante</strong> — Étale la pâte encore plus fine (2mm) et augmente le temps de précuisson à 12-15 minutes. Tu obtiendras une base ultra-croustillante.</p>"""

def intestin_permeable():
    return """
<p class="article-intro">Tu as peut-être entendu parler de "l'intestin perméable" ou du "leaky gut syndrome". Ces termes sont de plus en plus présents dans les discussions sur la santé naturelle, souvent associés à l'intolérance au gluten. Mais que dit vraiment la science ? Est-ce un phénomène réel ou un concept marketing ? Et surtout, quel est le lien avec le gluten ? Cet article fait le point sur ce que nous savons — et sur ce que nous ne savons pas encore.</p>

<h2>Qu'est-ce que l'intestin perméable ?</h2>

<p>L'intestin grêle est tapissé d'une muqueuse qui constitue une barrière essentielle entre l'intérieur de l'intestin (et tout ce qu'il contient : bactéries, particules alimentaires partiellement digérées, toxines) et la circulation sanguine. Cette barrière doit être à la fois sélective — laisser passer les nutriments — et imperméable aux molécules indésirables.</p>

<p>Cette barrière est assurée par des cellules épithéliales jointées par des "jonctions serrées" (tight junctions en anglais) — des protéines qui scellent l'espace entre les cellules intestinales. Quand ces jonctions serrées dysfonctionnent, la barrière devient perméable, laissant passer des molécules qui n'auraient pas dû traverser. C'est ce qu'on appelle l'hyperperméabilité intestinale, ou "leaky gut".</p>

<p>Ce phénomène est réel et documenté scientifiquement. Des marqueurs biologiques permettent de le mesurer — notamment la zonuline, une protéine qui régule les jonctions serrées, et la lactulose/mannitol ratio, un test fonctionnel de perméabilité.</p>

<h2>Le rôle du gluten dans la perméabilité intestinale</h2>

<p>C'est ici que ça devient particulièrement intéressant. Le Dr Alessio Fasano, directeur du Centre pour la Recherche sur la Maladie Cœliaque à Harvard, a découvert que le gluten déclenche la libération de zonuline — indépendamment du fait que la personne soit cœliaque ou non.</p>

<p>La zonuline est une protéine qui régule l'ouverture des jonctions serrées. Quand elle est libérée, les jonctions s'ouvrent et la perméabilité intestinale augmente temporairement. Chez les personnes saines, ce phénomène est transitoire et l'intestin retrouve sa perméabilité normale rapidement. Mais chez les personnes cœliaques ou avec une sensibilité au gluten, cette réponse peut être exagérée et prolongée.</p>

<p>Cette découverte explique pourquoi le gluten peut déclencher des symptômes dans tout le corps — pas seulement dans le système digestif. Quand des molécules passent à travers une barrière intestinale compromise, elles peuvent atteindre n'importe quel organe via la circulation sanguine et déclencher des réponses inflammatoires systémiques.</p>

<h2>Hyperperméabilité intestinale et maladie cœliaque</h2>

<p>Dans la maladie cœliaque, l'hyperperméabilité intestinale est bien documentée et joue un rôle central dans la pathologie. Voici comment ça se passe.</p>

<p>Quand une personne cœliaque ingère du gluten, la zonuline est libérée, les jonctions serrées s'ouvrent, et des fragments de gluten (notamment la gliadine) passent dans la lamina propria — la couche de tissu sous la muqueuse intestinale. Là, ils déclenchent une réponse immunitaire qui produit des anticorps anti-transglutaminase. Ces anticorps attaquent non seulement le gluten, mais aussi la transglutaminase tissulaire — une enzyme de l'intestin — ce qui provoque des dommages à la muqueuse et détruit les villosités intestinales.</p>

<p>Cette destruction des villosités réduit la surface d'absorption de l'intestin, provoquant une malabsorption des nutriments. C'est la cause directe des carences en fer, vitamines B12 et D, calcium et autres nutriments si fréquemment observées chez les cœliaques non traités.</p>

<h2>Hyperperméabilité intestinale et sensibilité au gluten non-cœliaque</h2>

<p>La sensibilité au gluten non-cœliaque (SGNC) est plus récemment reconnue et encore moins bien comprise. Des études récentes suggèrent que la perméabilité intestinale joue aussi un rôle dans ce cas, mais par un mécanisme différent.</p>

<p>Chez les personnes avec SGNC, il semblerait que le gluten déclenche une réponse immunitaire innée (le premier niveau de défense) plutôt qu'une réponse auto-immune adaptative (comme dans la maladie cœliaque). Cette réponse provoque une inflammation locale et peut contribuer à l'hyperperméabilité, mais sans les lésions vilositaires caractéristiques de la maladie cœliaque.</p>

<p>Une étude publiée dans Gut (2016) a montré que les personnes avec SGNC présentent des niveaux plus élevés de marqueurs d'activation immunitaire systémique et de perméabilité intestinale. Mais beaucoup de questions restent ouvertes sur les mécanismes exacts.</p>

<h2>Les autres facteurs qui augmentent la perméabilité intestinale</h2>

<p>Le gluten n'est pas le seul facteur qui peut compromettre la barrière intestinale. D'autres éléments jouent un rôle important, ce qui explique pourquoi l'hyperperméabilité intestinale peut aussi toucher des personnes qui ne consomment pas de gluten.</p>

<p><strong>Le stress chronique</strong> — Le stress active l'axe hypothalamo-hypophyso-surrénalien et libère des hormones (cortisol, adrénaline) qui ont des effets directs sur la perméabilité intestinale. Des études en animaux ont montré que le stress psychologique peut augmenter significativement la perméabilité de la muqueuse.</p>

<p><strong>Les médicaments anti-inflammatoires non stéroïdiens (AINS)</strong> — L'ibuprofène, l'aspirine et les autres AINS peuvent endommager la muqueuse intestinale et augmenter sa perméabilité, surtout en cas d'utilisation prolongée.</p>

<p><strong>L'alcool</strong> — L'alcool est directement toxique pour les cellules épithéliales de l'intestin et compromet les jonctions serrées. Une consommation régulière, même modérée, peut contribuer à l'hyperperméabilité.</p>

<p><strong>La dysbiose intestinale</strong> — Un déséquilibre du microbiote intestinal (les milliards de bactéries qui peuplent notre intestin) est associé à une perméabilité accrue. Certaines bactéries produisent des substances qui renforcent les jonctions serrées ; leur disparition fragilise la barrière.</p>

<p><strong>L'alimentation ultra-transformée</strong> — Les émulsifiants, épaississants et certains additifs alimentaires présents dans les aliments ultra-transformés ont été montrés pour perturber le microbiote et augmenter la perméabilité intestinale dans des études animales.</p>

<h2>Comment soutenir la santé de la barrière intestinale ?</h2>

<p>Si tu suspectes une perméabilité intestinale accrue, plusieurs approches peuvent soutenir la restauration de la barrière. Mais attention : ces approches complètent le traitement médical (notamment l'éviction du gluten si tu es cœliaque), elles ne le remplacent pas.</p>

<p><strong>L'éviction du gluten</strong> — C'est la première étape pour les personnes cœliaques ou avec SGNC. Des études ont montré que la perméabilité intestinale s'améliore significativement après 6 à 12 mois de régime sans gluten strict.</p>

<p><strong>Les aliments fermentés</strong> — Yaourt, kéfir, kimchi, choucroute, kombucha (non pasteurisé) apportent des probiotiques qui peuvent contribuer à restaurer un microbiote équilibré et soutenir la barrière intestinale.</p>

<p><strong>Le bouillon d'os</strong> — Riche en glutamine, en collagène et en glycine, le bouillon d'os traditionnel est souvent recommandé pour soutenir la muqueuse intestinale. La glutamine en particulier est le carburant préféré des cellules épithéliales de l'intestin.</p>

<p><strong>Les fibres prébiotiques</strong> — Nourrissent les "bonnes" bactéries du microbiote. Les meilleures sources incluent l'ail, l'oignon, les poireaux, les topinambours, les bananes légèrement vertes, les légumineuses.</p>

<p><strong>La réduction du stress</strong> — Méditation, yoga, cohérence cardiaque, sommeil suffisant — toutes les pratiques qui réduisent le stress chronique ont des effets bénéfiques sur la santé intestinale.</p>

<p><strong>L'éviction des AINS</strong> — Si tu consommes régulièrement des anti-inflammatoires non stéroïdiens, parle-en à ton médecin pour explorer des alternatives moins impactantes pour l'intestin.</p>"""

def top_farines():
    return """
<p class="article-intro">Le marché des farines sans gluten a explosé ces dernières années. Là où il n'existait que quelques options, on trouve maintenant des dizaines de farines différentes en magasin bio, en grande surface et en ligne. Comment choisir ? Laquelle utiliser pour quoi ? Ce classement des 8 meilleures farines sans gluten en 2025 est basé sur nos propres tests, les retours de notre communauté de 100 000 membres, et les propriétés nutritionnelles et culinaires de chaque farine.</p>

<h2>Comment ce classement a-t-il été établi ?</h2>

<p>Nous avons évalué chaque farine selon cinq critères : la polyvalence (peut-elle être utilisée dans de nombreuses recettes ?), les propriétés culinaires (goût, texture, comportement à la cuisson), le profil nutritionnel, la disponibilité et le prix, et enfin les retours de notre communauté (satisfaction, facilité d'utilisation pour les débutantes).</p>

<h2>1. Farine de riz blanc — La meilleure pour commencer</h2>

<p>La farine de riz blanc est notre recommandation numéro un pour les débutantes. Polyvalente, au goût neutre, facile à trouver et relativement abordable, elle constitue la base de la plupart des mélanges de farines sans gluten.</p>

<p>Elle est idéale pour les gâteaux, les crêpes, les béchamels, les pâtes à tarte, les pains moelleux. Elle donne des résultats légers et aérés quand elle est bien utilisée. Sa seule limitation : utilisée seule, elle peut donner une texture légèrement granuleuse et un goût un peu fade. La solution est de toujours la combiner avec une fécule.</p>

<p>Profil nutritionnel : faible en fibres, bonne source de glucides complexes, facile à digérer. Prix : environ 3-5€ pour 500g en version certifiée sans gluten.</p>

<h2>2. Farine de sarrasin — La meilleure pour le goût</h2>

<p>Si la farine de riz est la plus polyvalente, la farine de sarrasin est la plus savoureuse. Sa saveur terreuse et légèrement amère, ses notes de noisette, sa couleur brun-grisé caractéristique — tout ça en fait une farine avec une identité forte.</p>

<p>Elle est parfaite pour les galettes bretonnes (c'est son territoire naturel), les pains rustiques, les crackers, les blinis, les pancakes épais. Elle s'associe très bien avec des saveurs fortes comme le roquefort, les champignons, le saumon fumé.</p>

<p>Profil nutritionnel : supérieure à la plupart des farines, riche en protéines (13g/100g) et fibres, avec un bon profil d'acides aminés. Prix : environ 3-6€ pour 500g.</p>

<h2>3. Fécule de maïs (Maïzena) — La meilleure pour la légèreté</h2>

<p>La fécule de maïs n'est pas une "farine" à proprement parler, mais elle est indispensable dans la boîte à outils sans gluten. Elle apporte légèreté et finesse aux préparations, adoucit la texture parfois granuleuse des farines sans gluten, et donne une belle dorure aux gâteaux.</p>

<p>Utilisée seule pour une béchamel ou épaissir une sauce, elle donne un résultat parfaitement lisse et transparent. En mélange avec la farine de riz, elle est dans pratiquement toutes les recettes de gâteaux réussis. Elle est aussi parfaite pour paner les viandes et poissons.</p>

<p>Profil nutritionnel : très faible en fibres et nutriments, source de glucides simples. À utiliser comme ingrédient technique, pas comme base nutritionnelle. Prix : 1-3€ pour 250-400g, très accessible.</p>

<h2>4. Poudre d'amande — La meilleure pour la pâtisserie</h2>

<p>La poudre d'amande est la base des financiers, des macarons, des fondants au chocolat et de nombreux gâteaux sans farine. Naturellement sans gluten, elle apporte un moelleux incomparable, une richesse en saveurs de noisette et une valeur nutritionnelle bien supérieure aux farines de céréales.</p>

<p>Son inconvénient : elle est calorique et riche en graisses (ce qui est une qualité nutritionnelle mais peut être un point à surveiller). Elle ne convient pas à toutes les préparations — les pains et crêpes notamment s'y prêtent moins bien. Et son prix est plus élevé que les autres farines.</p>

<p>Profil nutritionnel : excellente source de protéines végétales (21g/100g), riche en graisses mono-insaturées, vitamine E, magnésium. Prix : 8-15€ pour 500g selon la qualité et la marque.</p>

<h2>5. Fécule de tapioca — La meilleure pour l'élasticité</h2>

<p>La fécule de tapioca (extraite du manioc) est méconnue mais irremplaçable pour certaines applications. Elle donne aux préparations une élasticité et un croustillant particulier qu'aucune autre fécule ne peut reproduire. C'est l'ingrédient secret de la pizza sans gluten réussie et du pain brésilien (pão de queijo).</p>

<p>Elle s'utilise rarement seule mais apporte une texture unique en mélange avec d'autres farines. Dans les recettes de pain, elle donne ce côté légèrement "chewy" qui manque souvent au pain sans gluten. Dans les crêpes, elle apporte de la souplesse.</p>

<p>Profil nutritionnel : pauvre en fibres et nutriments, source de glucides. Comme la fécule de maïs, c'est un ingrédient technique. Prix : 4-8€ pour 500g.</p>

<h2>6. Farine de châtaigne — La meilleure pour les pains rustiques</h2>

<p>La farine de châtaigne est un trésor de la cuisine française traditionnelle. Naturellement sucrée, avec des notes de noisette et de miel, elle apporte une saveur unique aux préparations. Elle colore les pains en brun doré et leur donne un parfum irrésistible à la sortie du four.</p>

<p>Trop forte en goût utilisée à 100%, elle s'associe parfaitement à la farine de riz dans des proportions de 30-40% pour des pains rustiques, des gaufres, des madeleines, des cakes salés. Elle est aussi excellente pour les pancakes et les gaufres.</p>

<p>Profil nutritionnel : bonne source d'énergie (glucides complexes), apporte des fibres, du potassium et des vitamines B. Prix : 5-9€ pour 500g.</p>

<h2>7. Farine de pois chiche — La meilleure pour les plats salés</h2>

<p>La farine de pois chiche est incontournable dans les cuisines méditerranéenne et indienne. En Provence, elle est la base de la socca (galette de pois chiche). Dans la cuisine indienne, c'est le besan, utilisé pour les pakoras, les papadums, de nombreuses sauces.</p>

<p>Sa saveur prononcée (légumineuse, légèrement amère) la limite aux applications salées. Mais dans ce domaine, elle excelle : galettes, falafels, crêpes salées, panures, liaisons de sauces. Elle est aussi nutritionnellement très intéressante.</p>

<p>Profil nutritionnel : excellente source de protéines végétales (22g/100g), riche en fibres, fer, zinc et folates. C'est l'une des farines sans gluten les plus nutritives. Prix : 3-6€ pour 500g.</p>

<h2>8. Farine de coco — La meilleure pour la pâtisserie low-carb</h2>

<p>La farine de coco est très différente des autres farines — elle absorbe beaucoup plus de liquide et a une texture plus légère. Elle est riche en fibres et a un index glycémique bas, ce qui en fait un choix populaire dans les régimes low-carb et keto.</p>

<p>Elle ne peut pas remplacer les autres farines dans un ratio 1:1 — il faut adapter les recettes. En général, utilise 3 fois moins de farine de coco que la farine originale indiquée, et augmente les œufs et le liquide. Elle donne des préparations légères, légèrement sucrées, avec un léger goût de coco qui se marie bien avec le chocolat et les fruits tropicaux.</p>

<p>Profil nutritionnel : très riche en fibres (40g/100g !), modérée en protéines, index glycémique bas. Une des farines les plus nutritives. Prix : 6-12€ pour 500g.</p>

<h2>Comment choisir la bonne farine selon ta recette ?</h2>

<p>Pour les gâteaux moelleux : farine de riz + fécule de maïs (60/40) ou poudre d'amande seule. Pour les crêpes légères : farine de riz + fécule de maïs (75/25). Pour les galettes salées : farine de sarrasin, pure ou mélangée. Pour les pains rustiques : farine de riz + farine de sarrasin ou châtaigne + fécule de tapioca. Pour les pizzas : farine de riz + fécule de tapioca (70/30). Pour les plats salés méditerranéens : farine de pois chiche. Pour la pâtisserie low-carb : poudre d'amande ou farine de coco adaptée.</p>"""

def voyage_europe():
    return """
<p class="article-intro">Voyager sans gluten en Europe, c'est une aventure qui peut être merveilleuse ou épuisante selon ta préparation. La bonne nouvelle : l'Europe est probablement le continent le plus "gluten-free friendly" au monde, avec une réglementation sur l'étiquetage stricte, une sensibilisation croissante dans la restauration, et des pays comme l'Italie où le sans gluten est presque une culture nationale. Ce guide te donne toutes les clés pour voyager sereinement.</p>

<h2>La réglementation européenne : ton alliée</h2>

<p>La réglementation européenne sur l'étiquetage alimentaire (règlement EU 1169/2011) impose que les 14 allergènes majeurs — dont le gluten — soient clairement identifiés sur les étiquettes de tous les produits alimentaires vendus dans l'Union Européenne. Cette réglementation s'applique dans tous les pays membres, ce qui te donne une base de sécurité commune quelle que soit ta destination.</p>

<p>Sur les étiquettes, recherche les mots "blé", "seigle", "orge", "avoine" mis en évidence (en gras ou dans une police différente) dans la liste des ingrédients. Ces mots seront dans la langue du pays, mais la mise en évidence te permettra de les repérer facilement même si tu ne parles pas la langue locale.</p>

<p>Dans les restaurants, les menus doivent également indiquer les allergènes. Cependant, la façon dont cette information est présentée varie beaucoup d'un établissement à l'autre — certains ont des menus avec codes d'allergènes détaillés, d'autres mentionnent simplement "contient des allergènes, demandez au personnel". N'hésite jamais à demander.</p>

<h2>Pays par pays : les destinations les plus safe</h2>

<h3>Italie : le paradis du sans gluten</h3>
<p>L'Italie est indiscutablement le meilleur pays d'Europe pour voyager sans gluten. La raison : avec une prévalence de la maladie cœliaque parmi les plus élevées d'Europe (environ 1 habitant sur 70 est cœliaque), le pays a développé une infrastructure "gluten-free" remarquable.</p>

<p>L'AIC (Associazione Italiana Celiachia) gère un programme de certification des restaurants sans gluten qui compte des milliers d'établissements dans tout le pays. Ces restaurants ont formé leur personnel, séparé leurs équipements et peuvent garantir la sécurité des plats sans gluten. Tu peux trouver la liste sur leur application ou leur site web.</p>

<p>Les supermarchés italiens ont tous un rayon "senza glutine" bien développé. Les pharmacies vendent des produits sans gluten remboursables pour les cœliaques italiens. Et la cuisine italienne elle-même offre de nombreuses options naturellement sans gluten : risotto, polenta, viandes grillées, poissons, légumes.</p>

<p>Une mise en garde : les pâtes et pizzas sont au cœur de la cuisine italienne, et la contamination croisée est un risque réel dans les restaurants non certifiés. Les restaurants certifiés AIC sont beaucoup plus sûrs que les autres.</p>

<h3>Espagne : très bonne option</h3>
<p>L'Espagne a fait d'énormes progrès ces dernières années en termes d'offre sans gluten. La FACE (Federación de Asociaciones de Celíacos de España) gère un programme de certification similaire à celui de l'AIC italienne.</p>

<p>La cuisine espagnole offre naturellement beaucoup d'options : les tapas (jamón serrano, tortilla española, manchego, patatas bravas, fruits de mer), les paellas (à base de riz), les poissons et viandes grillés. Les villes comme Barcelona, Madrid, San Sebastián et Valencia ont une offre importante de restaurants sans gluten certifiés.</p>

<h3>Royaume-Uni : excellent mais post-Brexit</h3>
<p>Le Royaume-Uni a toujours été très avancé en matière d'offre sans gluten — les grandes chaînes de supermarchés comme Tesco, Sainsbury's et Marks & Spencer ont des gammes "free from" très développées. La Coeliac UK a un programme de certification restaurants solide.</p>

<p>Depuis le Brexit, le Royaume-Uni n'est plus soumis à la réglementation européenne d'étiquetage, mais a maintenu des standards similaires. En pratique, l'offre reste excellente.</p>

<h3>Pays nordiques : sensibilisation élevée</h3>
<p>La Suède, la Norvège, le Danemark et la Finlande ont une très bonne sensibilisation au sans gluten, en partie grâce à une prévalence élevée de la maladie cœliaque dans ces populations. Les supermarchés ont de bons rayons sans gluten et le personnel de restaurant est généralement bien formé.</p>

<h3>France : en progrès</h3>
<p>La France a progressé ces dernières années, mais reste en retard par rapport à l'Italie ou l'Espagne. L'AFDIAG (Association Française Des Intolérants Au Gluten) gère un guide des restaurants, mais le nombre de restaurants certifiés reste limité. Les grandes villes (Paris, Lyon, Bordeaux, Marseille) offrent de plus en plus d'options, mais en zone rurale, c'est plus compliqué.</p>

<h3>Pays de l'Est : à aborder avec prudence</h3>
<p>Les pays d'Europe de l'Est (Pologne, République Tchèque, Hongrie, etc.) ont une sensibilisation au sans gluten moins développée. Les produits sans gluten se trouvent de plus en plus dans les supermarchés des grandes villes, mais la formation du personnel de restaurant est inégale. Prévois plus d'autonomie (hôtel avec cuisine, courses au supermarché) si tu voyages dans ces régions.</p>

<h2>Préparer son voyage : le kit de survie</h2>

<p>La préparation est la clé d'un voyage sans gluten réussi. Voici ce qu'on te recommande de faire avant de partir.</p>

<p><strong>Télécharge les applications indispensables</strong> — Find Me Gluten Free est l'application référence pour trouver des restaurants sans gluten dans le monde entier, avec des avis de la communauté. Yelp et Google Maps permettent aussi de filtrer par "sans gluten". Pour l'Italie, l'application de l'AIC est indispensable.</p>

<p><strong>Apprends les mots clés dans la langue locale</strong> — "Sans gluten" dans les principales langues européennes : senza glutine (italien), sin gluten (espagnol), sans gluten (français), glutenfrei (allemand), gluten-free (anglais), bez glutenu (polonais), glutenvrij (néerlandais).</p>

<p><strong>Prépare une carte d'allergie</strong> — Une carte écrite dans la langue du pays expliquant ton intolérance au gluten et les aliments à éviter est précieuse dans les restaurants. Des sites comme AllergyTranslation.com proposent des cartes traduites dans de nombreuses langues.</p>

<p><strong>Contacte ton hébergement à l'avance</strong> — Si tu séjournes dans un hôtel avec petit-déjeuner, contacte-les à l'avance pour qu'ils puissent prévoir des options sans gluten. La plupart des hôtels de qualité en Europe peuvent accommoder cette demande avec un préavis suffisant.</p>

<p><strong>Emporte des provisions de dépannage</strong> — Quelques barres de céréales sans gluten certifiées, des crackers sans gluten, des sachets de purée déshydratée sans gluten — ces petites provisions te sauveront dans les moments où tu ne trouves rien de sûr.</p>

<h2>Au restaurant : les bonnes pratiques</h2>

<p>Manger au restaurant à l'étranger demande un peu plus de vigilance. Voici les réflexes à adopter.</p>

<p>Choisis tes restaurants avec soin. Les restaurants certifiés par les associations nationales cœliaques sont les plus sûrs. À défaut, les restaurants qui proposent une section "sans gluten" claire sur leur menu, ou qui mentionnent explicitement leur gestion des allergènes, sont généralement plus fiables.</p>

<p>Arrive en dehors des heures de pointe si possible. Quand un restaurant est calme, le personnel a plus de temps pour s'occuper correctement de ta commande et éviter les contaminations croisées.</p>

<p>Explique toujours ton intolérance au serveur, même si le plat semble "naturellement" sans gluten. La contamination croisée (même plan de travail, même huile de friture, même ustensiles) peut rendre un plat sans gluten dangereux pour une personne cœliaque.</p>

<p>Reste à l'écoute de toi-même. Si quelque chose ne semble pas sûr, fais confiance à ton instinct et change de commande. Ta santé passe avant la politesse ou la gêne de déranger.</p>

<h2>Les cuisines naturellement plus sûres</h2>

<p>Certaines cuisines méditerranéennes et européennes sont naturellement plus adaptées au régime sans gluten.</p>

<p>La cuisine grecque est particulièrement favorable : la plupart des mezes (houmous, tzatziki, salade grecque, olives, fromages), les viandes et poissons grillés, les salades, le riz et les légumes — tout cela est naturellement sans gluten. Attention aux tiropites et spanakopites (feuilletés au fromage et aux épinards) qui contiennent de la pâte filo.</p>

<p>La cuisine portugaise est aussi très accessible : le poisson grillé (bacalhau, sardines), les viandes, les légumes, le riz — la base de la cuisine portugaise est naturellement sans gluten. Les pastéis de nata (tartelettes à la crème) contiennent de la farine, mais des versions sans gluten commencent à apparaître dans les boulangeries spécialisées.</p>

<p>La cuisine basque est excellente pour les personnes sans gluten : les pintxos (tapas sur pain) sont à éviter pour le pain, mais les garnitures (fruits de mer, viandes, fromages) peuvent souvent être servies seules.</p>"""

BODIES = {
    "pain-rustique-farine-chataigne": pain_chataigne,
    "crepes-sans-gluten-infaillible": crepes,
    "gateau-chocolat-fondant-sans-gluten": gateau_chocolat,
    "7-symptomes-intolerance-gluten": symptomes_gluten,
    "farine-riz-vs-sarrasin": farines_riz_sarrasin,
    "guide-debuter-sans-gluten": guide_debutant,
    "pizza-sans-gluten-base-croustillante": pizza,
    "gluten-et-intestin-permeable": intestin_permeable,
    "top-8-farines-sans-gluten-2025": top_farines,
    "voyage-europe-sans-gluten": voyage_europe,
}
