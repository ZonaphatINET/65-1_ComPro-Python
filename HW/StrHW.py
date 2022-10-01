strg = str(input('Input String: ')) 
vow = 'AaEeIiOoUu'

def OnlyStrg():
    strg.replace(' ','')
    print('Number of Letters:' , len(strg.replace(' ','')))

def Vowels():
    final = [each for each in strg if each in vow]
    print('Number of vowels:',len(final))

def Capital():
    res = [char for char in strg if char.isupper()]
    print('Number of Capital:',len(res),res)

def main():
    OnlyStrg()
    Vowels()
    Capital()

main()

#Input
#The Quick Brown Fox Jump Over The Lazy Dog
#The purpose of our Lives is to be Happy

#Number of Letters
#Number of vowels
#Number of Capital