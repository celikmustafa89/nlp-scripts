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
    """Is the string is dash separated like "Galatasary-Besiktas".

    :param token: string
    :return: Boolean
    """
    regexp = re.compile(r'^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$')
    if regexp.search(token) is not None:
        return True
    else:
        return False


def separate_dashed_words(token):
    """Separates dashed words and returns the list of all words.

    :param token: string
    :return: list
    """

    return token.split('-')


def is_date(token):
    """Is the string is a date.

    :param token: string
    :return: Boolean
    """
    regexp = re.compile(r'^(?:(?:(?:0?[13578]|1[02])(\/|-|\.)31)\1|(?:(?:0?[1,3-9]|1[0-2])(\/|-|\.)(?:29|30)\2))'
                        r'(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:0?2(\/|-|\.)29\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|'
                        r'[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:(?:0?[1-9])|'
                        r'(?:1[0-2]))(\/|-|\.)(?:0?[1-9]|1\d|2[0-8])\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$')
    if regexp.search(token) is not None:
        return True
    else:
        return False


def get_date(token):
    regexp = re.compile(r'^(?:(?:(?:0?[13578]|1[02])(\/|-|\.)31)\1|(?:(?:0?[1,3-9]|1[0-2])(\/|-|\.)(?:29|30)\2))'
                        r'(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:0?2(\/|-|\.)29\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|'
                        r'[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:(?:0?[1-9])|'
                        r'(?:1[0-2]))(\/|-|\.)(?:0?[1-9]|1\d|2[0-8])\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$')

    reg = regexp.search(token)
    return reg.group()
