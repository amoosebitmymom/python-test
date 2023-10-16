def switch_last_letters(str1, str2):
    return str2[:-1] + str1[-1]  + ' ' + str1[:-1] + str2[-1]


def change_verb_form(string):
    if len(string) < 3:
        return string
    
    suffix = 'ing'
    if string.endswith(suffix):
        suffix = 'ly'
    
    return string + suffix


def remove_char_by_index1(string, index):
    return string[:index] + string[index + 1:]
 

def remove_char_by_index2(string, index):
    new_string = ''
    for idx, char in enumerate(string):
        if idx != index:
            new_string += char
    
    return new_string


def caeser_chiper(string, shift, direction='right'):
    manipulator = 1
    if direction == 'left':
        manipulator = -1

    shift = (shift % 26) * manipulator
    cipher = ''
    for idx, char in enumerate(string):
        offset = 97
        if char.isupper():
            offset = 65

        cipher += chr((ord(char) % offset + shift) % 26 + offset)
    
    return cipher


def object_to_json(obj):
    return dict_to_json(obj.__dict__)
    #attrs = dir(obj)
    #json = ""
    #for attr in attrs:
    #    if not callable(getattr(obj, attr)):
    #        value = str(getattr(obj, attr))
#
    #        if isinstance(getattr(obj, attr), dict):
    #            value = dict_to_json(getattr(obj, attr))
#
    #        if isinstance(getattr(obj, attr), str):
    #            value = '"' + value + '"' 
    #        
    #        if isinstance(getattr(obj, attr), (tuple, set)):
    #            value = '"' + value + '"'
    #            
    #        json_attr = '"' + attr + '"' + ':' + value
    #        json += json_attr + ','
    #
    #json = json[:-1]
    #json = json.replace('None', 'null')
    ##json = json.replace("'", '"')
    #json = json.replace('False', 'false')
    #json = json.replace('True', 'true')
    #return "{" + json + "}"

def dict_to_json(dic):
    json_dict = ""
    for item in dic:
        key = '"' + str(item) + '"' + ":"
        if isinstance(dic[item], (int, bool, float)) or dic[item] is None:
            json_dict += key + str(dic[item]) + ','
        elif isinstance(dic[item], list):
            json_dict += key + list_to_json(dic[item]) + ','
        elif isinstance(dic[item], dict):
            json_dict += key + dict_to_json(dic[item]) + ','
        elif isinstance(dic[item], (str, tuple, set, frozenset, complex, bytes, bytearray, range, memoryview)):
            json_dict += key + '"' + str(dic[item]) + '"' + ','
        else:
            json_dict += key + object_to_json(dic[item]) + ','

    json_dict = json_dict[:-1]
    json_dict = json_dict.replace('False', 'false').replace('True', 'true').replace('None', 'null').replace('\\','\\\\')
    return "{" + json_dict + "}"

def list_to_json(lst):
    json_list = ""
    for item in lst:
        if isinstance(item, (int, bool, float)) or item is None:
            json_list += str(item) + ','
        elif isinstance(item, list):
            json_list += list_to_json(item) + ','
        elif isinstance(item, dict):
            json_list += dict_to_json(item) + ','
        elif isinstance(item, (str, tuple, set, frozenset, complex, bytes, bytearray, range, memoryview)):
            json_list += '"' + str(item) + '"' + ','
        else:
            json_dict += key + object_to_json(dic[item]) + ','

    json_list = json_list[:-1]
    return "[" + json_list + "]"

def remove_dupes(lst):
    unique_lst = []
    for element in lst:
        if element not in unique_lst:
            unique_lst.append(element)
    return unique_lst

def kth_larget_element(lst, k):
    lst.sort()
    lst = remove_dupes(lst)
    return lst[-k]

def kth_lsmallest_element(lst, k):
    lst.sort()
    lst = remove_dupes(lst)
    return lst[k - 1]

def dict_from_string(string):
    return {char: string.count(char) for char in string}

#print(switch_last_letters('abc', 'xyz'))

#print(change_verb_form('abc'))
#print(change_verb_form('string'))
#print(change_verb_form('hi'))

#print(remove_char_by_index2('I have no clue', 3))

#print(caeser_chiper('xYz', 3, 'right'))
"""
class Again:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Idk:
    def __init__(self, a, b, c, d, e, f, g):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g

cef = Again(1, 2)
abc = Idk(('a', 'b', 'c'), '1', cef, {1, "5", False}, 5, [1, 2, 4, "hello", {"a": (1, 3, 4), "b": {True, None}, "c": [1, 2, 3, (0, 1, 2)]}], {"a": 1, "b": 'hello', "c": {1, '2', True}, "d": {"a" : 1, "b": {2, None, ('hello', 5) }}, "e": [bytes(4), False, 'hello', (1, 3, 4)]})
print(object_to_json(abc))
"""

#print(remove_dupes([1,1,3,1,3,5,6,1,5,6,1,32,8,45,1]))

print(dict_from_string('w3resource'))