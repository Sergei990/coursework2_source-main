from flask import Flask, render_template, Blueprint

from utils import search_tagname

tag_blueprint = Blueprint('tag_blueprint', __name__, template_folder='templates')

@tag_blueprint.get('/tag/<tagname>')
def search_tag(tagname):

    tags = search_tagname(tagname)

    return render_template('tag.html', tags=tags)

