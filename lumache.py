def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: if the kind is invalid.
    :return: the ingredients list.
    :rtype: list[str]
    
    """

    return ["eggs", "bacon", "spam"]

def hello_world():
    """The classical "Hello, world!" function"""
    print("Hello, world!")

class InvalidKindError(Exception):
    """Raised if the kind is invalid"""
    
    pass
