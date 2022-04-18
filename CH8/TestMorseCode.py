from CH8.MakeMorseTree import makeMorseTree, encode, decode

MorseCode = makeMorseTree()

str = input("문자 입력 : ")
mlist = []
for ch in str:
    code = encode(ch)
    mlist.append(code)
print("MorseCode : ", mlist)
print("Decoding : ", end='')
for code in mlist:
    ch = decode(MorseCode, code)
    print(ch, end='')
print()
