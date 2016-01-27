#coding:utf-8
import requests
import re
import urllib

url="http://www.jianshu.com"
home="http://www.jianshu.com/collections/16/notes?order_by=added_at&page="
f=open("jianshu.html",'a')
start = input("从哪页开始:\n")
end = input("到哪页结束:\n")
if start==1:
    f.write('<meta charset="utf-8">')
for i in range(start,end+1):
    print "正在解析第"+str(i)+"页..."
    html = requests.get(home+str(i))
    site = re.findall('<h4 class="title"><a target="_blank" href="(.*?)">(.*?)</a>',html.text,re.S)
    for each in site:
        link=each[0]
        link=urllib.unquote(link.encode('utf-8'))
        name=each[1]
        name=urllib.unquote(name.encode('utf-8'))
        f.write('<h4 class="title"><a target="_blank" href="'+url+link+'">'+name+'</a></h4>')
f.close()