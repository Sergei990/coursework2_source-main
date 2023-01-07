from flask import Flask, Blueprint

from all_posts.all_posts import all_postsblueprint
from error_ import  error_404
from main.main import main_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)

app.register_blueprint(all_postsblueprint)

@app.errorhandler(404)
def error_404(error_400):

    return 'код 404.Нет страници'

@app.errorhandler(500)
def error_500(error_500):

    return 'ошибка 500, Internal Server Error'



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888, debug=True)
