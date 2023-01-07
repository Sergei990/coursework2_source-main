from flask import Flask, Blueprint, render_template, request

from utils import all_posts, get_posts_by_user, search_for_posts, search_by_name

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.get('/')
def index():
    """представление для всех постов"""
    posts = all_posts
    return render_template('index.html', all_posts=posts)


@main_blueprint.get('/posts/<int:postid>')
def get_comments(postid):

    """Выведeт комментарий к посту."""

    comments, user, y = get_posts_by_user(postid)

    return render_template('post.html', comments=comments, user=user, y=y)


@main_blueprint.get('/search/')
def search_by_qwery():
    """Создайте представление для поиска """
    s = request.args.get('s')
    search = search_for_posts(s)

    return render_template('search.html', search=search)
    # return f'word{s}'

@main_blueprint.get('/users/<username>')
def search_users(username):

    user_name=search_by_name(username)

    return render_template('user-feed.html', user_name=user_name)
