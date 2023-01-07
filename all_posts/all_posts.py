from flask import Flask, Blueprint, json, jsonify
from utils import all_posts
all_postsblueprint = Blueprint('all_postsblueprint', __name__)

@all_postsblueprint.get('/api/posts/')
def loads_all_file():

    posts_for_api = all_posts#(ensure_ascii=False)
    # for posts in all_posts:
    #     ensure_ascii=False)
        # posts_for_api.append(posts)



    return json.jsonify(posts_for_api)

@all_postsblueprint.get('/api/posts/<post_id>')
def post_by_id(post_id):

    posts = []

    for post in all_posts:

        if post_id == post:

            x = post['content']

            return jsonify({'content': x})
