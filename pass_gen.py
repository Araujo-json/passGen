import random, string, numpy as np

def passgen(x, y):
  letters = string.ascii_letters # string a-z ans A-Z
  numb = string.digits #0-9
  sim = string.punctuation #!”#$%&'()*+,-./:;<=>?@[]^_`{|}~
  poss = letters + numb + sim
  
  arrpass = []

  pwd = ''
  for i in np.arange(x):
    #less effitient O^2
    for c in np.arange(y): 
      pwd += random.choice(poss)
    arrpass.append(pwd)
  return arrpass
  #for l in arrpass: return l


num_pass = int(input('Number of passwords: '))
length =int(input('Password length: '))
print()

print(passgen(num_pass,length))