import xml.etree.ElementTree

root = xml.etree.ElementTree.parse("student.xhtml")
print("使用getiterator访问:")
nodes = root.getiterator()
for node in nodes:
    print("{0}---{1}".format(node.tag,node.text))

print("使用find和findall方法：")
e_student= root.find("student")
print(type(e_student))
#print("{0}".format(e_student.text))

ele_stu=root.findall("student")
print(type(ele_stu))
for ele in ele_stu:
    print("{0},,,{1}".format(ele.tag,ele.text))
    for sub in ele.getiterator():
        if sub.tag =="Name":
            if "other" in sub.attrib.keys():
                print(sub.attrib["other"])