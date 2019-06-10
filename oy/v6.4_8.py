from lxml import etree
text ="""
<div>
    <ul>
        <li class = "item-0"><a herf = "0.html">first item</a></li>
        <li class = "item-1"><a herf = "1.html">second item</a></li>
        <li class = "item-2"><a herf = "2.html">three item</a></li>
    </ul>
</div>
"""
html = etree.HTML(text)
s = etree.tostring(html)
print(s)