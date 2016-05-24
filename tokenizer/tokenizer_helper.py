import re

def remove_apostrophe(token):
    """Removes the apostrophe, combines two sides

    :param token: string
    :return: combined string
    """
    token = token.replace("'", "")
    token = token.replace("`", "")

    return token


def is_dashed_words(token):
    """Is the string is dash seperated like "Galatasary-Besiktas".

    :param token: string
    :return: Boolean
    """
    regexp = re.compile(r'^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$')
    if regexp.search(token) is not None:
        return True
    else:
        return False
