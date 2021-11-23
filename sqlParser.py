# Analizador Léxico by Elmer Jaén

# Get all the tokens of a string
# Compare if the order of the tokens is a correct sql statement

import re
import os

reserved_keywords = (
    'SELECT', 'FROM', 'DISTINCT', 'WHERE',
    'BETWEEN', 'AND', 'COUNT', 'DROP', 'TABLE')

keywords_in_data = []
identifiers_in_data = []

def delete_repeated_identifier(identifiers, sql_string):
    unique_identifiers = []
    for i in identifiers:
        if i not in unique_identifiers:
            unique_identifiers.append(i)
    
    unique_identifiers.append('\*') # * para la sentencia SELECT
    var = ""
    keywords = ""
    var += ',|'.join(unique_identifiers)
    keywords += '|'.join(reserved_keywords)
    evaluate_sql(var, keywords, sql_string)

def evaluate_sql(var, keywords, sql_string):
    #p_SELECT = re.compile('SELECT(['+var+']+)FROM(?!$|\W|\w+\W|'+keywords+')')
    p_SELECT = re.compile('SELECT([\w+,\w+]+|\*)FROM(?!$|\W|\w+\W|'+keywords+')')
    p_COUNT = re.compile('SELECTCOUNT\(\w+\)FROM(?!$|\W|\w+\W|'+keywords+')')
    p_DROP = re.compile('DROPTABLE(?!$|\W|\w+\W|'+keywords+')')
    #p_SELECT = re.compile('SELECT(DISTINCT)?(['+var+']+)FROM(?!$|'+table_name+')')
    #p_SELECT_DISTINCT = re.compile('SELECTDISTINCT(['+var+']+)FROM(?!$|'+table_name+')')
    #p_BETWEEN = re.compile(r'SELECT('+var+')FROM('+var+')WHERE('+var+')BETWEEN\dAND\d')
    
    os.system('cls')
    print('Pattern:', p_SELECT)
    print(p_SELECT.findall(sql_string))
    if p_SELECT.match(sql_string):
        print('La sentencia SQL es correcta.')
    else:
        print('La sentencia SQL es incorrecta')

def classify(split_string, sql_string):
    
    # get all the possible identifiers that are not in
    # reserved_keywords
    for i in split_string:
        if i.isidentifier() == True and i not in reserved_keywords:
            identifiers_in_data.append(i)
    
    # for i, j in enumerate(identifiers_in_data):
    #     if j[0] != "_":
    #         IDENTIFIERS.append(j)
    
    delete_repeated_identifier(identifiers_in_data, sql_string)
 #   return keywords_in_data, IDENTIFIERS, operators_in_data, numbers_in_data

def run():
    user_input = input("\nA continuación ingrese una sentencia SQL:\n")
    # get rid off the spaces in the string
    split_string = re.split(',|, | ', user_input)
    #split_string = re.split(' COUNT\(|\) | ', user_input)
    sql_string = ''.join(re.split(' ', user_input))
    classify(split_string, sql_string)
  
if __name__ == '__main__':
  run()