import re 

def decompresor(encrypted_string,symble_and_code):
    symble_and_code = get_key_values(symble_and_code)
    result_string=""
    sub_string=''
    for item in encrypted_string:
        sub_string +=item
        if sub_string in symble_and_code.keys():
            result_string+=symble_and_code[sub_string]
            sub_string=""

    return result_string


def get_key_values(symble_and_code):

    symble_and_code_list= re.findall("[\d\D ] : [01]*",symble_and_code)

    result={}
    for item in symble_and_code_list:
        key_value_list = item.split(" : ")
        result[key_value_list[1]] = key_value_list[0]

    return result












    



            
