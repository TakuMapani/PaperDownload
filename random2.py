import random
import re

url  = "https://pmt.physicsandmathstutor.com/wp-content/uploads/../../download/Physics/A-level/Past-Papers/CIE/Paper-1/June%2008%MS%-%Paper%1%CIE%Physics%A-level.pdf"
print(re.sub('[%]', " ", url))

a = (re.sub('/wp-content/uploads/../..',"",url))
b = (re.sub('%',"%20",a))
f = (b.split('%20')[1:10])
print(f[0]+"_"+f[1]+f[2]+f[3]+f[4]+f[len(f)-1])
print(f)