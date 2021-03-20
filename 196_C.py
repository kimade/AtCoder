import math

N = input()
T=""

if len(N) == 1 or int(N) == 10:
    print(0)

elif len(N)%2 == 1:
    if int(N[len(N)//2:]) == 0:
        for i in range(math.floor(len(N)//2)):
            T = T + "9"
    else:
        print(min(N[:len(N)//2],N[len(N)//2:-1]))

else:
    if int(N[len(N)//2:]) == 0:
        for i in range(len(N[len(N)//2:]) - 1):
            T = T + "9"
    else:
        T = min(N[:len(N)//2],N[len(N)//2:])

print(T)
