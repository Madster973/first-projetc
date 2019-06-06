s=list(input())
print(''.join([i+str(s.count(i)) for i in sorted(set(s))]))
