import webbrowser, os
import sys
from urllib.request import pathname2url

path=sys.argv[1]
def readfile(p):
    file_object  = open(p, 'r')
    return file_object.read()

data=readfile(path)
data=data.splitlines()

rows = 7
columns = 18
table = [0] * rows
for i in range(rows):
    table[i] = [0] * columns

row=0
for element in data:
    content=element.split(',')
    pos=content[0].find(':')+1
    col=int(content[0][pos:])
    table[row][col]=content
    if col==17:
        row=row+1
        
def CreateCell(element):
    name  = element[0][:element[0].find('=')-1]
    number= element[1].replace('number:', 'No ')
    small = element[2].replace('small:','')
    molar = element[3][element[3].find(':')+1:]
    electron = element[4].replace('electron:','')
    electron = electron + ' electron'
    html = """<h4>""" + name + """</h4>
              <ul>
              <li>""" + number   + """</li>
              <li>""" + small    + """</li>
              <li>""" + molar    + """</li>
              <li>""" + electron + """</li>
              <ul>"""  
    
    return (html)

html = """<html>
<head></head>
<body>
<table>"""

for i in range(len(table)):
    html= html + """<tr> """
    for j in range(len(table[0])):
        if table[i][j]==0:
             html=html + """<td style="border: 1px solid black; padding:10px"></td>"""
        else:
            element=CreateCell(table[i][j])
            html=html + """<td style="border: 1px solid black; padding:10px">""" + element + """</td>"""

html = html + """</table></html>"""
f = open('periodic_table.html','w')
f.write(html)
f.close()

url = 'file:{}'.format(pathname2url(os.path.abspath('periodic_table.html')))
webbrowser.open(url)

