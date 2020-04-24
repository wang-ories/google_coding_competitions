T = int(input())
def solution():
    s = input()  
    n = len(s)
    _s = ''
    for i in range(n):
        v = int(s[i])
        t = int(s[i-1])
        if v >= 1:
            if i > 0:
                if t == v:
                    _s = _s[:-v] + str(v) + ')'* v
                else:
                    if t == 0:
                        _s += v*'(' + str(v) + ')'*v
                    else:
                        if t < v:
                            diff = v - t
                            _s = _s[:-t] + '('*diff + str(v) + ')'*diff + ')'*t
                        elif t > v:
                            diff = t - v
                            _s = _s[:-v] + str(v)+')'*v
            else:
                _s += v*'(' + str(v) + ')'*v
                            
            
        else:
            _s += str(v)
            
    return _s

for t in range(1, T+1):
    print('Case #%d: %s' %(t, solution()))