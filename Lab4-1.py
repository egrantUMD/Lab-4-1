#!/usr/bin/python37all
import cgi
import json
import cgitb



cgitb.enable()


data = cgi.FieldStorage()

s = data.getvalue('slider1')
p = data.getvalue('PIN') 

data = {"slider1":s, "pin":p}

with open('led-pwm.txt', 'w') as f:
  json.dump(data,f)



print('Content-type: text/html\n\n')
print('</head>')
print('<body>')
print('<div style="width:600px;background:#FFFFFF;border:1px;text-align:center"> <br>')
print('<form action="/cgi-bin/Lab4.py" method="POST">')
print('<input type="radio" name="PIN" value=17 > LED 1 <br>')
print('<input type="radio" name="PIN" value=27> LED 2 <br>')
print('<input type="radio" name="PIN" value=22> LED 3 <br>')
print('<input type="range" name="slider1" min ="0" max="100" value ="0"/><br>')
print('<input type="submit" value="Submit">')
print('</body>')
print('</form>')
print('</div>')
print('</html>')