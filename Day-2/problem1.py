n=int(input())
if (n>=0 and n<10):
    print("Single Digit")
elif (n>=10 and n<100):
    print("Two Digit")
elif (n>100 and n<1000):
    print("Triple Digit")
else:
    print("Out of range")