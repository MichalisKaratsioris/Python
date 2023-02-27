from flask import Flask, render_template, url_for
import random

app = Flask(__name__)

greeting = ['Hello', 'Γειά σου', 'Buongiorno', 'Buen dia', 'Guten tag']
names = ['Lolo', 'Moraki', 'Sachito']
products = [
    ("Milk", 3.59123),
    ("Bread", 2.96332),
    ("Rice", 0.64111)
]
articles = [
    {
        "content": "Ne istas culpa ha im negat de. Ii perductae evertenda at desuescam. Nudi per ita sui dare ideo sola omne ordo. Sui sex item sane quum. Paucos sicuti tot qui tantae aliquo strata iis tantas. Mo purgantur at affirmans im reddendum co. Pleraque videntur ut ideamque imaginem ha.",
        "seen": ["John", "Jane", "Bob"]
    },
    {
        "content": "Aliud curam seu venti nihil sed istud volui eae qua. Autho ha falsi fidam tangi ut an tactu. Revera per eandem vox coelum videbo nam virtus. Item olim ei se duas ut. Ut mo ut peccato student adorare et diversa. Praecipuis ad conjunctam me percipitur agnoscerem at perfectius respondere. Horum meo porro uno debeo. Fallacem sentiens ha expertus delapsus dubitare ii. Ex ii efficiente et to perspicuae voluptatem arbitrabar.",
        "seen": ["John", "Jane"]
    },
    {
        "content": "Credendi at nequidem exhibere de. Debeo me dicam ex at ferri digna. Coloribus differant disputari vix cogitandi jam stabilire. Perfacile ut reliquiae perfectae ut. Fuisse falsas captum cui volent notior verbis sui. Meam idem nam ope prae isti quia jure hac. Lor durent has secius fronte usu auditu sumpti. Falso nomen aliud vim calor jam alias annos ubi. Movendi sum creatus vim fas majorem attendo propter. Sui videamus uno profecto refutent rom notitiam innumera potuerit.",
        "seen": ["John"]
    },
    {
        "content": "Potui habeo visus ens mea. An vi re continetur me familiarem negationem. Rei inveniri jam viderunt subducam tam imponere jam. Sub cui more ipsi meum.",
        "seen": []
    }
]

authors = [
    {
        "id": 100,
        "name": "John",
        "likes": [
            202,
            200
        ]
    },
    {
        "id": 101,
        "name": "Jane",
        "likes": [
            200
        ]
    }
]

posts = [
    {
        "id": 200,
        "author": 100,
        "content": "Difficulty on insensible reasonable in. From as went he they."
    },
    {
        "id": 201,
        "author": 100,
        "content": "Preference themselves me as thoroughly partiality considered on in estimating."
    },
    {
        "id": 202,
        "author": 101,
        "content": "In as name to here them deny wise this. As rapid woody my he me which."
    }
]

exercises = ['Random Language 1', 'Random Language 2', 'Products', 'Articles', 'Posts']


@app.route('/')
def hello_world():
    return render_template('index.html', name='Home Page')


@app.route('/index')
def home_page():
    return render_template('index.html', list=exercises, name='Index')


@app.route('/1')
def rl1():
    random_language = random.choice(greeting)
    return render_template('random_language_1.html', lang=random_language, name='Random Language 1')


@app.route('/2')
def rl2():
    rl = random.choice(greeting)
    rn = random.choice(names)
    return render_template('random_language_2.html', lang=rl, person_name=rn, name='Random Language 2')


@app.route('/3')
def get_products():
    return render_template('products.html', products=products, name='Products')


@app.route('/4')
def get_articles():
    return render_template('articles.html', articles=articles, name='Articles')


@app.route('/5')
def get_posts():
    transformed_posts = None
    posts_list = [posts, authors]
    return render_template("posts.html", posts=transformed_posts, list=posts_list, name='Posts')


if __name__ == '__main__':
    app.run(debug=True)
