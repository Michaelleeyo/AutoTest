'''
shutil.copy() 复制文件,返回新文件的路径
shutil.copytree(source,destination) 复制文件夹,返回新文件夹的路径
shutil.move(source,destination) 将路径 source 处的文件夹移动到路径
destination，并返回新位置的绝对路径的字符串。
永久删除
os.unlink(path) 删除path处的文件
os.rmdir(path) 将删除path处的文件夹，文件夹必须为空
shutil.rmtree(path) 删除path处的文件夹，包括里面的所有东西

使用send2trash模块安全删除，会放到回收站
sen2trash.send2trash('a.txt')

遍历目录 os.walk(path)

zipfile.ZipFile() 读取zip文件 
ZipFile对象有namelist()方法，返回ZIP文件中包含的文件和文件夹名的字符串列表
字符串可以传递给 ZipFile 对象的 getinfo()方法，返回一个关于特定文件的 ZipInfo 对象。 
ZipInfo 对象有自己的属性，诸如表示字节数的 file_size
和 compress_size，它们分别表示原来文件大小和压缩后文件大小。 ZipFile 对象表示
整个归档文件，而 ZipInfo 对象则保存该归档文件中每个文件的有用信息。

zipfile.ZipFile(zipfile).extractall() 解压缩到当前目录
zipfile.ZipFile(zipfile,'w') 创建添加ZIP文件
'''
import os
import zipfile

for folderName, subfolders, filenames in os.walk('F:\\1Doc\\AutoTest\\Python'):
    print('The current folder is '+folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF '+folderName+':'+subfolder)
    for filename in filenames:
        print('FILE INSIDE'+folderName+':'+filename)
    print('')

os.chdir('F:\\1Doc\\AutoTest\\Python')
testZip = zipfile.ZipFile('test.zip')
print(testZip.namelist())
print(testZip.getinfo('test.txt'))
print(testZip.getinfo('test.txt').compress_size)
print(testZip.getinfo('test.txt').compress_type)
print(testZip.getinfo('test.txt').file_size)
