import random, string, numpy as np

def passgen(x, y):
  letters = string.ascii_letters # string a-z ans A-Z
  numb = string.digits #0-9
  sim = string.punctuation #!”#$%&'()*+,-./:;<=>?@[]^_`{|}~
  poss = letters + numb + sim
  
  arrpass = []

  for i in range(x):
    #pwd = ''
    temp = random.sample(poss,y)
    pwd = ''.join(temp)
    arrpass.append(pwd)
  return arrpass

num_pass = int(input('Number of passwords: '))
length =int(input('Password length: '))
print()

print(passgen(num_pass,length))
