'''
random.shuffle(list) 随机打乱列表
list.index(x[,start[,end]]) 例子：list.index('apple',4,10)
查找某一个值的索引位置，可以定义查找开始结束位置
random.sample(list,k)
返回一个长度为k的新列表，新列表存放list所产生k个随机唯一的元素
'''

# 生成随机测试试卷和对应的答案
import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# 创建考试卷，并且打乱问题的次序
for quizNum in range(35):
    # 每份试卷文件名为capitalsquizX.txt,答案文件名为capitalsquiz_answersX.txt
    quizFile = open('capitalsquiz%s.txt' % (quizNum+1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum+1), 'w')

    # 学生填写内容
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((''*20)+'State Gapitals Quzi(Form %s)' % (quizNum+1))
    quizFile.write('\n\n')

    # 创建题目列表
    states = list(capitals.keys())
    # random.shuffle()函数创建随机列表
    random.shuffle(states)

    # 针对一份试卷，创建选项。确认正确答案，
    # 错误答案为删除正确答案后，任意选择三个。放到一起后，再随机打乱
    for questionNum in range(50):
        correctAnswers = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswers)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswers]
        random.shuffle(answerOptions)

        # 创建题目
        quizFile.write('%s.What is the capital of %s?\n' %
                       (questionNum+1, states[questionNum]))
        # 写入选项
        for i in range(4):
            quizFile.write('%s.%s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')
        # 正确答案
        answerKeyFile.write('%s.%s\n' % (
            questionNum+1, 'ABCD'[answerOptions.index(correctAnswers)]))
quizFile.close()
answerKeyFile.close()
