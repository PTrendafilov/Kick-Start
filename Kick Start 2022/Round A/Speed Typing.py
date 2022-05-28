n = int(input())
for i in range(n):
    I = input()
    P = input()
    I = list(I[::-1])
    P = list(P[::-1])
    corrects = 0
    while P:
        if I:
            if P[len(P)-1] == I[len(I)-1]:
                I.pop()
                P.pop()
            else:
                P.pop()
                corrects += 1
        else:
            P.pop()
            corrects += 1
    if P == I:
        print(f'Case #{i + 1}: {corrects}')
    else:
        print(f'Case #{i + 1}: IMPOSSIBLE')
