try:
    arr=list(map(int,input().split()))
    first=float("-inf")
    second=float("-inf")
    third=float("-inf")
    for x in arr:
        if x>first:
            third>second
            second=first
            first=x
        elif x>second:
            third=second
            second=x
        else:
            first=x
    if len(arr)>=3:
        print(first,second,third)
    else:
        print("Inavlid")
except:
    print("Invalid input")