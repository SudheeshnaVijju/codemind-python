for u in range(int(input())):
    s=input()
    d=int(s,16)
    d=(bin(d)[2:])
    while(len(d)%4!=0):
        d='0'+d
    print(d)