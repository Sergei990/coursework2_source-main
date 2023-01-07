import json


def get_posts_all():
    """ возвращает посты"""

    with open('data/posts.json', encoding='UTF-8') as file:
        return json.load(file)


all_posts = get_posts_all()


def get_posts_by_user(user_name):
    """возвращает посты определенного пользователя"""

    with open('data/comments.json', encoding='UTF-8') as file:

        comments_ = json.load(file)

        posts_by_pk = []
        comments_by_post = []

        for comment in comments_:

            if user_name == comment['post_id']:
                comments_by_post.append(comment)

        for posts in all_posts:

            if user_name == posts['pk']:
                posts_by_pk.append(posts)
            if '#' in posts['content']:
                e = posts['content']
                x = []
                x.append(e)
                y = f'<a href="user-feed.html">{x}</a>'
                # x = posts['content'] + f'<a href"user-feed.html">{}</a>'

        return comments_by_post, posts_by_pk, y


def search_for_posts(query):
    """ возвращает список постов по ключевому слову"""
    posts = []

    for post in all_posts:

        if query.lower() in post['content'].lower():
            posts.append(post)

    return posts


def search_by_name(name):
    user_name = []

    for users in all_posts:

        if name.lower() in users['poster_name'].lower():
            user_name.append(users)
    return user_name

def search_tagname(tag):

    tags = []

    for tagname in all_posts:

        if tag in tagname['content']:
            tags.append(tagname)
    return tags
