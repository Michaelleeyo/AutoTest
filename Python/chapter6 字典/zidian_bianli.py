'''
items()
keys()
values()
set() 
剔除重复项，可使用集合set，集合类似列表，每一个元素都是独一无二的
get() 例：dict.get('a',0)
它有两个参数：第一个要取得其值的键，第二个如果该键不存在时，返回的备用值
setdefault() 例：dict.setdefault('color','black)
它有两个参数：第一个是要检查的键，第二个键如果不存在要设置的值(存在值不变)
'''

# 练习：词汇表
languages = {
    'Python': '.py',
    'Java': '.java',
    'PHP': '.php',
    'JS': '.js'
}
languages.setdefault('go', '.go')
for language, houzhui in languages.items():
    print(language)
    print(houzhui)


# 练习：河流
rivers = {
    'nile': 'egypt',
    'changjiang': 'china',
    'huanghe': 'china'
}
for river, country in rivers.items():
    print('The '+river + ' runs through '+country)

for river in set(rivers.keys()):
    print(rivers.keys())
    print('Rivers include '+river)

for country in set(rivers.values()):
    print('Countries include '+country)


# 练习：调查
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
name_list = ['jen', 'michael', 'fox', 'phil']
for name, language in favorite_language.items():
    if name in name_list:
        print('thanks, '+name)
    else:
        print(name+',you are invited to join us.')
