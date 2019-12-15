import re, translitcodec, codecs
from .index   import *
from .article import *

@app.template_global()
def slugify(text, delim='_'):
    """
    Generates an ASCII-only slug.
    Taken from 'http://flask.pocoo.org/snippets/5/'
    """

    punctuation_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')
    result = []

    for word in punctuation_re.split(text.lower()):
        word = codecs.encode(word, 'translit/short')
        if word:
            result.append(word)

    return delim.join(result)
