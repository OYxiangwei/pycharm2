from lxml import etree

html = etree.parse("./student1.html")
print(type(html))
r1 = html.xpath('//studnt')
print(r1)
print(type(r1))
r2 = html.xpath('//studnt[@level="4"]')
print(r2)
print(type(r2))
r3 = html.xpath('//studnt[@level="4"]/age')
r3 = r3[0]
print(r3)
print(r3.text)
print(r3.tag)