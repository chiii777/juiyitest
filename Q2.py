def find_number(n):
    ans = []
    for i in range(1,n+1):
        if not i%15:
            ans.append(i)
        elif not i%3 or not i%5:
            pass
        else:
            ans.append(i)
    return len(ans)
