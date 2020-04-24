T = int(input())
def solution():
    n = int(input())
    m = [[0]*n]*n
    k = 0
    r = 0
    c = 0
    for i in range(n):
        m[i] = list(map(int, input().split()))    
    k = sum(m[i][i] for i in range(n))
    for i in range(n):
        columns = [column[i] for column in m]
        cc = set([x for x in columns if columns.count(x) > 1])
        if len(cc) > 0:
            c +=1
        rows = m[i]
        rr = set([x for x in rows if rows.count(x) > 1])
        if len(rr) > 0:
            r += 1             
    return k,r,c

for t in range(1, T+1):
    print('Case #%d: %s' %(t, ' '.join(str(c) for c in solution())))
