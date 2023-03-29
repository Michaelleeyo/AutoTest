'''
在 Python 中使用正则表达式有几个步骤，但每一步都相当简单。
1.用 import re 导入正则表达式模块。
2.用 re.compile()函数创建一个 Regex 对象（记得使用原始字符串）。
3.向 Regex 对象的 search()方法传入想查找的字符串。它返回第一一个 Match 对象。
4.调用 Match 对象的 group()方法，返回实际匹配文本的字符串。

更多匹配模式：
1.括号分组 re.compile((a),(bc)).search('xxxx').group(1)
2.管道匹配多个分组,第一个出现的对象将作为Match对象返回
re.compile(r'a|b').search('this is a pen').group()
3.问号实现可选匹配 re.compile(r'Bat(wo)?man').search('i am Batman').group() 
wo可出现零次或者一次
4.星号匹配零次或者多次，星号前的分组可以出现任意次
re.compile(r'Bat(wo)*man').search('i am Batwowowoman').group()
5.加号出现一次或者多次
re.compile(r'bat(wo)+man').search('xxxx').group()
6.花括号指定出现次数
re.compile(r'(oh){3,5}').search('xxxx').group()

findall()方法返回所有匹配的字符串列表

\d 0-9的任何数字
\D 除0-9数字以外的任何字符
\w 任何字母、数字、下划线
\W 除了字母、数字、下划线任何字符
\s 空格、制表符、换行符
\S 除了空格、制表符、换行符任何字符

自定匹配规则 例： re.compile(r'[^0-9a-zA-Z]').findall()匹配所有非字符类

正则表达式的开始处使用插入符号（^），表明匹配必须发生在被查找文
本开始处。类似地，可以再正则表达式的末尾加上美元符号（$），表示该字符串必
须以这个正则表达式的模式结束。
例： re.compile(r'^\d+$') 从开始到结束都是数字
re.compile(r'^Hello') 匹配以Hello开始的字符串
re.compile(r'\d$') 以数字结尾

通配字符 .只能匹配一个字符 *前面的字符出现零次或者多次
贪心 .* 匹配任意字符。 re.compile(r'first:(.*) last:(.*)')
非贪心 .*? re.compile(r'<.*?>')
匹配换行符 re.compile('.*',re.DOTALL)
匹配不区分大小 re.compile(r'a',re.IGNORECASE)

sub() 方法替换字符串 传入两个参数，第一个要取代的字符串，第二个是正则表达式
re.compile(r'a').sub('b','a pen')
re.sub(pattern, repl, string, count=0, flags=0)
pattern：正则表达式模式，用于匹配要替换的字符串；
repl：用于替换匹配字符串的字符串；
string：要被处理的字符串；
count：可选参数，指定替换的最大次数。默认为 0，表示替换所有匹配；
flags：可选参数，指定正则表达式使用的匹配模式。

忽略正则表达式字符串中的空白符和注释， 从而缓解这一点。 要实现这种详细模式， 
可以向 re.compile()传入变量 re.VERBOSE， 作为第二个参数。
例：见regex.py

'''
import os
import re

current_dir = os.path.dirname(__file__)
mad_lib_file = os.path.join(current_dir, 'mad_libs.txt')

# 读文件内容
with open(mad_lib_file, 'r') as mad_libs:
    words = mad_libs.read()

# 正则表达式匹配规则
mo = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')

# 替换单词
for word in mo.findall(words):
    alternative = input('Enter a '+word.lower()+':')
    words = re.sub(mo, alternative, words, 1)

# 写入文件
with open(mad_lib_file, 'w') as mad_libs:
    mad_libs = words

print(words)
