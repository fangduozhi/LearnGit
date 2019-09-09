d={'a':'4','b':'2','c':'3'}
c={val:key for key,val in d.items()}
print(c)
print(sorted(d.items(),key=lambda x:x[1]))
print(d.values())