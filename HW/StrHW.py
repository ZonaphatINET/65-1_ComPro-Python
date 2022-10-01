strg = str(input('Input String: ')) 
vow = 'AaEeIiOoUu'

def OnlyStrg():

    print('Number of Letters:' , len(strg.replace(' ','')))

def Vowels():
    numVow = [masg for masg in strg if masg in vow]
    print('Number of vowels:',len(numVow))

def Capital():
    res = [upper for upper in strg if upper.isupper()]
    print('Number of Capital: %d, '%len(res)+'[%s]'%', '.join(map(str,res)))

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