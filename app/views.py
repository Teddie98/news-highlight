from flask import render_template
from app import app
from .request import get_sources
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general_categories = get_sources('general')
    # business_category = get_sources('business')
    # entertainment_category = get_sources('entertainment')
    # sports_category = get_sources('sports')
    # technology_category = get_sources('technology')
    # science_category = get_sources('science')
    # health_category = get_sources('health')

    title = 'World News Highlights'
    return render_template('index.html',title = title, general = general_categories)

@app.route('/newsarticle/<id>')
def newsarticle(id):

    '''
    View article page function that returns the article details page and its data
    '''
    # article = get_article
    title = 'News Articles'
    return render_template('article.html',title = title,id = id)