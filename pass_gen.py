import random, string

def passgen(x, y,poss):

  arrpass = set()
  
  for _ in range(x):
    temp = random.sample(poss,y)
    pwd = ''.join(temp)
    arrpass.add(pwd)
  
  return arrpass

def chact():
  letters = string.ascii_letters + u'\u00F1' + u'\u00D1'
  numb = string.digits 
  sim = string.punctuation 
  poss = letters + numb + sim
  return poss
  
num_pass = int(input('Number of passwords: '))
length =int(input('Password length: '))
print()

record = passgen(num_pass,length,chact())
print(record)
