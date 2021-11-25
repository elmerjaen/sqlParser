# Analizador Sintáctico
# by Elmer Jaén, Louis Aguilar, Omar Flores

import re

keywords = 'SELECT|FROM|DISTINCT|WHERE|BETWEEN|AND|COUNT|DROP|TRUNCATE|TABLE|DELETE'

def get_tokens(a):

    token_list = [x.strip(' ') for x in a]
    p_keywords = re.compile(keywords)
    p_var = re.compile('(\w+)(?<!['+keywords+']|[\d+])')
    p_numbers = re.compile('\d+')
    p_special_characters = re.compile('\W')

    t = {}
    tokens = {
        "Palabras reservadas:": p_keywords,
        "Variables:": p_var,
        "Números:": p_numbers,
        "Caracteres especiales:": p_special_characters
    }

    for key, value in tokens.items():
        for i in token_list:
            if value.match(i):
                if key not in t:
                    t[key] = list()
                t[key].append(i)
    return t

def evaluate_sql(sql_string):

    p_SELECT = re.compile('SELECT[\s](\w+|\*|\w+,[\s]\w+)(?<!['+keywords+'])[\s]FROM[\s]([a-zA-Z]+)(?<!['+keywords+'])([\s]WHERE[\s]([a-zA-Z]+)(?<!['+keywords+'])(=|>|<|(=)*|<(=)*|<(>)*)(\'\w+\'|\d+)(?<!['+keywords+']))*')
    
    p_SELECT_DISTINCT = re.compile('SELECT[\s]DISTINCT[\s](\w+)(?<!['+keywords+'])[\s]FROM[\s]([a-zA-Z]+)(?<!['+keywords+'])')
    
    p_COUNT = re.compile('SELECT[\s]COUNT\((\w+)(?<!['+keywords+'])\)[\s]FROM[\s]([a-zA-Z]+)(?<!['+keywords+'])')
    
    p_DROP = re.compile('DROP[\s]TABLE[\s]([a-zA-Z]+)(?<!['+keywords+'])')
    
    p_TRUNCATE = re.compile('TRUNCATE[\s]TABLE[\s]([a-zA-Z]+)(?<!['+keywords+'])')
    
    p_DELETE = re.compile('DELETE[\s]FROM[\s]([a-zA-Z]+)(?<!['+keywords+'])[\s]WHERE[\s]([a-zA-Z]+)(?<!['+keywords+'])(=|>|<|(=)*|<(=)*|<(>)*)(\'\w+\'|\d+)(?<!['+keywords+'])')

    patterns = {
        "SELECT": p_SELECT,
        "SELECT_DISTINCT": p_SELECT_DISTINCT,
        "SELECT COUNT": p_COUNT,
        "DROP TABLE": p_DROP,
        "TRUNCATE TABLE": p_TRUNCATE,
        "DELETE": p_DELETE
    }

    for key, value in patterns.items():
        if value.fullmatch(sql_string):
            print(value.fullmatch(sql_string))
            return 1, key
    return 0,0