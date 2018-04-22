from lxml import etree

from pyquery import PyQuery as pq

doc = pq("<html></html>")

doc_url = pq("http://www.baidu.com")

doc_et = pq(etree.fromstring('<html></html>'))

doc_file = pq(filename='resource/hello.html')
print(doc_file.html())
print(type(doc_file))

li = doc_file('li')
print(type(li))
print(li.text())


p1 = pq("<p id='hello' class='hello'></p><input id='hello' class='hello'></input>")('input')
print(p1.add_class('beauty'))
print(p1.remove_class('hello'))
print(p1.css('front-size', '16px'))
print(p1.css({'background-color': 'yellow'}))

print("####")
p2 = pq('<p id="hello" class="hello"></p>')
print(p2.append(' check out <a href="http://reddit.com/r/python"><span>reddit</span></a>'))
print(p2.append("oh yes!"))
print("####")
p3 = pq('<p id="hello" class="hello"></p>')('p')
d = pq('<div class="wrap"><div id="test"><a href="http://cuiqingcai.com">Germy</a></div></div>')
p3.prepend_to(d('#test')) # 放入id为test的第一个位置
print(p3)
print(d)
d.empty()
print(d)
print("####")
lis = doc_file('li')
for li in lis.items():
    print(li.html())
    print("$")
print(lis.each(lambda e: e))




