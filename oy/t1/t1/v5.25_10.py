import os
import os.path as op
import shutil
import zipfile

#print(os.getcwd())
#print(os.listdir()[1])
#print(os.makedirs("dana"))
#print(os.system("dir"))
#print(os.getenv("PATH"))
#print(os.curdir)
#print(os.pardir)
#print(os.linesep)
#print(os.sep)
print(os.name)
path = "/oy"+"/"+"dana"
print(path)
absph = op.abspath(".")
print(absph)
bn = op.basename(absph)
print(bn)
bd ="D:\pycharm\pkg01"
fn = "oy"
print(op.join(bd,fn))

s,t = op.split(absph)
print(s,t)
print(op.isdir("v1.py"))
print(op.exists("dana"))

print(shutil.copy("D:\\pycharm\\pkg01\\oy\\v5.25_4.py","D:\\pycharm\\pkg01\\oy\\ve5.25_4.py"))
print(shutil.copy2("D:\\pycharm\\pkg01\\oy\\v5.25_4.py","D:\\pycharm\\pkg01\\oy\\ve45.25_4.py"))
print(shutil.copyfile("t1.txt","t2.txt"))
#print(shutil.move(D:\\pycharm\\pkg01\\oy\\v5.25_4.py","D:\\pycharm\\pkg01"))
print(shutil.make_archive("D:\\pycharm\\pkg01\\oy\\t1","zip","D:\\pycharm\\pkg01\\oy"))
print(shutil.unpack_archive("D:\\pycharm\\pkg01\\oy\\t1.txt.zip","D:\\pycharm\\pkg01\\oy\\t8.txt"))

zf = zipfile.ZipFile("D:\\pycharm\\pkg01\\oy\\t1.zip")
print(zf.getinfo("t1.zip"))
print(zf.namelist())
print(zf.extractall("D:\\pycharm\\pkg01\\oy\\t1"))