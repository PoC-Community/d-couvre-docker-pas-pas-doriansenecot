import session
from app import *
from app.models import get_username_from_id

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title = '404 not found')


@app.route(('/'), methods = ['GET'])
def route_home():
    return render_template('index.html',title = 'Epytodo')


@app.route('/signin_page')
def signin_page():
    return render_template('signin_page.html',title = 'Please signin')


@app.route('/register_page')
def regiser_page():
    return render_template('register_page.html',title = 'Please register')


@app.route(('/my_profile'), methods = ['GET'])
def profil_route():
    if session.session == -1:
        return render_template('error.html',title = 'Epytodo')
    else:
        return render_template('user.html',title = 'Profil', user = get_username_from_id(session.session))
