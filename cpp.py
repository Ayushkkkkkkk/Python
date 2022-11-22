t = int(input())
# Yess, YES or se.
# esY, YesYes, sYes, e, but you couldn't Yess, YES or se.
while t > 0:
    s1 = input()
    if "se" in s1:
        print("NO")
        continue
    if "YES" in s1:
        print("NO")
        continue
    if "Yess" in s1:
        print("NO")
        continue
    if "esY" in s1:
        print("YES")
        continue
    if "YesYes" in s1:
        print("YES")
        continue
    if "sYes" in s1:
        print("YES")
        continue
    if s1=="e":
        print("YES")
        continue
    else:
        print("NO")
        continue
    t-=1