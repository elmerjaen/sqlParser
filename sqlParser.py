# Analizador Sintáctico
# by Elmer Jaén, Louis Aguilar, Omar Flores

import re

keywords = 'SELECT|FROM|DISTINCT|WHERE|BETWEEN|AND|COUNT|DROP|TABLE'

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

def run():
    sql_string = input("\nA continuación ingrese una sentencia SQL:\n")
    evaluate_sql(sql_string)
  
if __name__ == '__main__':
  run()