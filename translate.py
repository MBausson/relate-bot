import translators as ts


"""
    Translator API
"""


def translate(text, to_l: str) -> str:
    return ts.bing(text, from_language='auto', to_language=to_l)

"""
    Users file (language preference)
"""


def add_user(id, lang):
    with open('users.txt', 'a') as f:
        f.write(f'{id}:{lang}')


def get_user(id):
    with open('users.txt', 'r') as f:
        for line in f.readlines():
            data = line.removesuffix('\n').split(':')

            if int(data[0]) == id:
                return {
                    'id': int(data[0]),
                    'lang': str(data[1])
                }

    return None


def change_user(id, oldlang, newlang):
    #   This is probably a very bad idea, but whatever.
    content = ''

    with open('users.txt', 'r') as f:
        content = f.read()

    content = content.replace(f'{id}:{oldlang}', f'{id}:{newlang}')
    with open('users.txt', 'w') as f:
        f.write(content)


languages = ['ar', 'bg', 'ca', 'zh-CN', 'zh-TW', 'hr', 'cs', 'da', 'nl', 'en', 'fi', 'fr', 'de', 'el', 'hi', 'hu',
             'id', 'it', 'ja', 'ko', 'no', 'pl', 'pt', 'ro', 'ru', 'sr', 'sk', 'es', 'sv', 'th', 'tr', 'uk', 'vi']
