# Analizador Léxico by Elmer Jaén

# Get all the tokens of a string
# Compare if the order of the tokens is a correct sql statement

import re
import os

keywords = 'SELECT|FROM|DISTINCT|WHERE|BETWEEN|AND|COUNT|DROP|TABLE'

def evaluate_sql(sql_string):

    p_SELECT = re.compile('(SELECT((?!$|\W|\w+\W|'+keywords+')|\*|\w+|\w+,\w+)FROM)(?!$|\W|\w+\W|'+keywords+')')
    p_COUNT = re.compile('(SELECTCOUNT\(((?!$|\W|\w+\W|'+keywords+')|\w+)\)FROM)(?!$|\W|\w+\W|'+keywords+')')
    p_DROP = re.compile('DROPTABLE(?!$|\W|\w+\W|'+keywords+')')
    p_TRUNCATE = re.compile('TRUNCATETABLE(?!$|\W|\w+\W|'+keywords+')')
    p_DELETE = re.compile('DELETEFROM(\w+)(?<!['+keywords+'])WHERE(\w+)(?<!['+keywords+'])(=|>|<|(=)*|<(=)*|<(>)*)(\'\w+\'|\d+)(?<!['+keywords+'])')

    patterns = {
        "SELECT": p_SELECT,
        "SELECT COUNT": p_COUNT,
        "DROP TABLE": p_DROP,
        "TRUNCATE TABLE": p_TRUNCATE,
        "DELETE": p_DELETE
    }

    for key, value in patterns.items():
        print(value.match(sql_string))
        if key == "DELETE":
            if value.fullmatch(sql_string):
                return 1, key
        else:
            if value.match(sql_string):
                return 1, key
    return 0,0

def run():
    user_input = input("\nA continuación ingrese una sentencia SQL:\n")
    # get rid off the spaces in the string
    split_string = re.split(',|, | ', user_input)
    #split_string = re.split(' COUNT\(|\) | ', user_input)
    sql_string = ''.join(re.split(' ', user_input))
    evaluate_sql(sql_string)
  
if __name__ == '__main__':
  run()