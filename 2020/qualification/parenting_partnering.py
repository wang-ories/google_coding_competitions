from operator import itemgetter

T = int(input())
def solution():
    # number of activities
    
    n = int(input())
    parents = ['J', 'C']
    res = [0]*n
    tasks = []
    for i in range(n):
        v = input().split(' ')
        task  = {}
        task['start'] = int(v[0])
        task['end'] = int(v[1])
        task['index'] = i
        
        tasks.append(task)
    #print(tasks)
    t_ = sorted(tasks, key=itemgetter('start')) 
    
    #is_parent_1_free = True    
    task_1 = {'start': 0, 'end':0, 'index': 0}
    task_0 = t_[0]
    res[task_0['index']] = 'C'
    #is_parent_0_free = False
    #res = 'C'
    k = len(t_)
    for i in range(1, k):
        task = t_[i]
        # check if parent_0 is free
        if task_0['end'] <= task['start']:
            # parent is free
            task_0 = task
            res[task['index']] = 'C' 
        else:
            # check if parent_1 is free
            if task_1['end'] <= task['start']:
                task_1 = task
                res[task['index']] = 'J' 
            else:
                # Both are busy
                return 'IMPOSSIBLE'
    return ''.join(str(c) for c in  res)
    
for t in range(1, T+1):
    print('Case #%d: %s' %(t, solution()))
