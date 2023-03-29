import re

print(re.compile(r'(a) (bc)').search('apple banana bc crone ').group(2))
print(re.compile(r'a|b').search('this is a banana').group())
print(re.compile(r'Bat(wo)?man').search('I am Batman').group())
print(re.compile(r'Bat(wo)*man').search('I am Batwowoman').group())
print(re.compile(r'Bat(wo)+man').search('I am Batman'))
print(re.compile(r'(oh){2,3}').search('oh ohohoh ohoh ohohohoh').group())
print(re.compile(r'\d\d\d-\d\d\d-\d\d\d\d').findall('Cell: 415-555-9999 Work: 212-555-0000'))
print(re.compile(r'[^0-9a-zA-Z]').findall('!@# aa $$%^^ 123 ab'))
print(re.compile(r'\d+$').findall('12 312'))
print(re.compile(r'\d$').findall('ab1 cd2'))
print(re.compile(r'^br').findall('brown brother'))
print(re.compile(r'a+').sub('b', 'a pen'))
phoneRegex = re.compile(r'''(
    (\d{3} |\(\d{3}\))? #类似 123 或者 (123)
    (\s | - |\.)? #分隔符为空格、-、.
    \d{3} #三位数字
    (\s | - |\.)
    \d{4} #四位数字
    (\s*(ext | x | ext.)\s *\d{2, 5})?)''', re.VERBOSE)  # 分机号
print(phoneRegex)
