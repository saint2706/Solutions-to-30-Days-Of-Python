from flask import Flask, render_template, request, redirect, url_for
import os
import re
import string
from collections import Counter
from lexical_diversity import lex_div as ld

app = Flask(__name__)
# to stop caching static file
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
content = ''


def clean_text(text):
    text = text.lower()
    text = re.sub("\[.*?]", "", text)
    text = re.sub("https?://\S+|www\.\S+", "", text)
    text = re.sub("<.*?>+", "", text)
    text = re.sub("[%s]" % re.escape(string.punctuation), "", text)
    text = re.sub("\n", "", text)
    text = re.sub("\w*\d\w*", "", text)
    return text


def most_common_word(text):
    split_it = text.split()
    Cnter = Counter(split_it).most_common()
    return Cnter


def lex_div_calc(text):
    return '%.1f' % (ld.ttr(ld.flemmatize(text)) * 100)


@app.route('/')  # this decorator create the home route
def home():
    techs = ['CSS', 'Flask', 'HTML', 'Python']
    name = 'Text Analyzer'
    return render_template('home.html', techs=techs, name=name, title='Home')


@app.route('/about')
def about():
    name = 'Rishabh Agrawal'
    return render_template('about.html', name=name, title='About Us')


@app.route('/result')
def result():
    clean_content = clean_text(content)
    most_used_words = most_common_word(clean_content)
    most_used_word = most_used_words[0][0]
    total_words = len(clean_content.split())
    number_of_chars = len(clean_content)
    lexical_diversity_text = lex_div_calc(clean_content)
    return render_template('result.html', clean_content=clean_content, most_used_word=most_used_word,
                           most_used_words=most_used_words, total_words=total_words, number_of_chars=number_of_chars,
                           lexical_diversity_text=lexical_diversity_text)


@app.route('/post', methods=['GET', 'POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)
    if request.method == 'POST':
        # noinspection PyUnusedLocal
        global content
        content = request.form['content']

        return redirect(url_for('result'))


if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
