import goslate


def translate(text, to_language):
    return goslate.Goslate().translate(text, to_language)
