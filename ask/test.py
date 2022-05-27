import random
import string

letters = string.ascii_letters + string.digits 

print(''.join(random.choice(letters) for i in range(245)))

import datetime

a = datetime.datetime.now()

b = a + datetime.timedelta(1)

print(a)

print(b)

