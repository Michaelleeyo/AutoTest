import json


def save_info(info_dict):
    with open('info.json', 'w') as f:
        json.dump(info_dict, f)


def load_info():
    try:
        with open('info.json', 'r') as f:
            info_dict = json.load(f)
    except FileNotFoundError:
        return {}
    return info_dict


info_dict = load_info()
if not info_dict:
    name = input("请输入你的名字：")
    number = input("请输入你喜欢的数字：")
    info_dict[name] = number
    save_info(info_dict)
else:
    name = input("请输入你的名字：")
    if name in info_dict:
        print("你喜欢的数字是：", info_dict[name])
    else:
        number = input("请输入你喜欢的数字：")
        info_dict[name] = number
        save_info(info_dict)
