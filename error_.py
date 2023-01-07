class NotPage(Exception):
    pass


def error_404():
    page = {'/', '/posts/', '/search/', '/users/'}
    if not page:

        raise NotPage
    return NotPage
