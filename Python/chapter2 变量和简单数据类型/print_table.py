def printTable(List1, List2):
    # 第一层循环
    for i in range(len(List1[0])):
        # 第二层循环
        for j in range(len(List1)):
            print(List1[j][i].rjust(int(List2[j])), end=' ')  # 打印完一行再换行
        print()


tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bod', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]
colWidths = [0]*len(tableData)  # colWidths列表中每个元素放置每个内置列表的最长字符串长度
len1 = 0
# 分别求列表的每一个内置列表中最长的字符串的长度
for i in range(len(tableData)):
    for j in range(len(tableData[i])):
        if len(tableData[i][j]) > colWidths[i]:
            colWidths[i] = len(tableData[i][j])

printTable(tableData, colWidths)
