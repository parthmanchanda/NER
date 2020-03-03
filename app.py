

import spacy
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('submit') == 'submit':
            text = request.form['text']
            nlp2 = spacy.load("ur")
            doc2 = nlp2(text)
            res = [(ent.label_, ent.text) for ent in doc2.ents]
            te = ""
            for l, t in res:
                te += l + " : " + t + '\n'
            return render_template('home.html', summary=te, text=text)
        elif request.form.get('Reset') == 'Reset':
            return render_template('home.html', summary='', text='')

    return render_template("home.html")


if __name__ == '__main__':
    app.run()

