n=int(input())
if (n>=65 and n<=90):
    print("Capital Letter")
elif (n>=97 and n<=122):
    print("Small Letter")
elif (n>=0 and n<=31):
    print("Non Printable character")
elif((n>=33 and n<=47)or(n>=58 and n>=64)or(n>=91 and n<=96)or(n>=123)):
    print("Symbols")
else:
    print("Space")