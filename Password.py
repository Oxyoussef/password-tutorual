# password tutorual

import random

l = "qwertyuiopasdfghjklzxcvbnm"
h = "QWERTYUIOPASDFGHJKLZXCVBNM"
g = '0123456789'
o = "{}+[]/\@"
all = l + h + g + o
p = 16
password = ''.join(random.sample(all, p))
print (password)
