N = input()
count = 0
if 1 <= len(N) < 4:
    count = 0

elif 4 <= len(N) < 7:
    count = int(N) - 999

elif 7 <= len(N) < 10:
    count = (int(N) - 999999) * 2
    count += (999999 - 999)

elif 10 <= len(N) < 13:
    count = (int(N) - 999999999) * 3
    count += (999999 - 999)
    count += (999999999 - 999999) * 2

elif 13 <= len(N) < 16:
    count = (int(N) - 999999999999) * 4
    count += (999999 - 999)
    count += (999999999 - 999999) * 2
    count += (999999999999 - 999999999) * 3

else:
    count = (int(N) - 999999999999999) * 5
    count += (999999 - 999)
    count += (999999999 - 999999) * 2
    count += (999999999999 - 999999999) * 3
    count += (999999999999999 - 999999999999) * 4

print(count)