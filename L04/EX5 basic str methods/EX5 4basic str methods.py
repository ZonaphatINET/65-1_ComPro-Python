balloon = "      Anirach has a balloon      "

print('[',balloon.strip(),']')
print('[',balloon.lstrip(),']') #ตัดซ้าย
print('[',balloon.rstrip(),']') #ตัดขวา


balloon = "###Anirach has a balloon####"
print('[',balloon.strip('#'),']')
print('[',balloon.rstrip('#'),']') #ตัดขวา

#[ Anirach has a balloon ]
#[ Anirach has a balloon       ]
#[       Anirach has a balloon ]
#[ Anirach has a balloon ]
#[ ###Anirach has a balloon ]