#datval yvelaze xshiri elementis raodenoba arrayshi
from collections import Counter
a=[]
def solution(a):
    try:
        counter=Counter(a)
        
        
        return counter.most_common(5)[0][1]
    except:
        return("list is empty")

print(solution(a))

