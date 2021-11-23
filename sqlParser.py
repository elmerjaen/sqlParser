# Analizador Léxico by Elmer Jaén

# Get all the tokens of a string
# Compare if the order of the tokens is a correct sql statement

import re
import os

keywords = 'SELECT|FROM|DISTINCT|WHERE|BETWEEN|AND|COUNT|DROP|TABLE'

keywords_in_data = []
identifiers_in_data = []

# def delete_repeated_identifier(identifiers, sql_string):
#     unique_identifiers = []
#     for i in identifiers:
#         if i not in unique_identifiers:
#             unique_identifiers.append(i)
    
#     unique_identifiers.append('\*') # * para la sentencia SELECT
#     var = ""
#     keywords = ""
#     var += ',|'.join(unique_identifiers)
#     keywords += '|'.join(reserved_keywords)
#     evaluate_sql(var, keywords, sql_string)

def evaluate_sql(sql_string):
    # need to fix keywords in SELECT and COUNT
    # I can find the keywords first and make them not to match
    p_SELECT = re.compile('SELECT([\w+,\w+]+|\*)FROM(?!$|\W|\w+\W|'+keywords+')')
    p_COUNT = re.compile('SELECTCOUNT\(\w+\)FROM(?!$|\W|\w+\W|'+keywords+')')
    p_DROP = re.compile('(DROP|TRUNCATE)TABLE(?!$|\W|\w+\W|'+keywords+')')
    #p_DELETE = re.compile('DELETEFROM(?!$|\W|\w+\W|'+keywords+')')
    p_DELETE = re.compile('DELETEFROM\w+WHERE\w+[=|>|<|>=|<=|<>](\'\w+\'|\d+)')
    print(p_DELETE.findall(sql_string))

    patterns = (p_SELECT, p_COUNT, p_DROP, p_DELETE)
    #os.system('cls')
    band = False
    for i in patterns:
        if i.match(sql_string):
            band = True
            print('Pattern:', i)
            print(i.findall(sql_string))
            print('La sentencia SQL es correcta.')
    if band==False:
        print('Comando incorrecto.')

    # DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';
    # DELETE FROM table_name;
    # DELETE FROM Customer WHERE name='Elmer'
    # DELETE FROM Customer
    # DELETE FROM Customer WHERE
    #p_DELETE = re.compile('DELETEFROM((?!$|\W|\w+\W|'+keywords+'))+(WHERE((?!$|\W|\w+\W))+[=|>|<|>=|<=|<>](\'\w+\'|\d+))*')

   # p_DELETE = re.compile('DELETEFROM(?!$|\W|\w+\W|'+keywords+')WHERE')
    #p_SELECT = re.compile('SELECT(DISTINCT)?(['+var+']+)FROM(?!$|'+table_name+')')
    #p_BETWEEN = re.compile(r'SELECT('+var+')FROM('+var+')WHERE('+var+')BETWEEN\dAND\d')

# def classify(split_string, sql_string):
    
#     # get all the possible identifiers that are not in
#     # reserved_keywords
#     for i in split_string:
#         if i.isidentifier() == True and i not in reserved_keywords:
#             identifiers_in_data.append(i)
    
#     # for i, j in enumerate(identifiers_in_data):
#     #     if j[0] != "_":
#     #         IDENTIFIERS.append(j)
    
#     delete_repeated_identifier(identifiers_in_data, sql_string)
#  #   return keywords_in_data, IDENTIFIERS, operators_in_data, numbers_in_data

def run():
    user_input = input("\nA continuación ingrese una sentencia SQL:\n")
    # get rid off the spaces in the string
    split_string = re.split(',|, | ', user_input)
    #split_string = re.split(' COUNT\(|\) | ', user_input)
    sql_string = ''.join(re.split(' ', user_input))
    evaluate_sql(sql_string)
  
if __name__ == '__main__':
  run()