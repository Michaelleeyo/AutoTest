import json


def save_file(dict_info):
    with open('person.json', 'w')as f:
        json.dump(dict_info, f)


def load_file():
    try:
        with open('person.json', 'r')as f:
            dict_info = json.load(f)
    except FileNotFoundError:
        return {}
    else:
        return dict_info


dict_info = load_file()
if not dict_info:
    name = input('Enter your name:')
    number = input('Enter your favorite number:')
    dict_info[name] = number
    save_file(dict_info)
else:
    name = input('Enter your name:')
    if name in dict_info:
        print(name+"'s favorite number is "+dict_info[name])
    else:
        number = input('Enter your favorite number:')
        dict_info[name] = number
        save_file(dict_info)
