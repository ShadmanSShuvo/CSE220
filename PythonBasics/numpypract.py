import numpy as np 
t = np.array([-3,-2,-1,0,1,2]).astype(int)
s = np.array([8,2,7,9,11,10]).astype(int)
print(t)
print(s)
s_inversed = s[::-1]
print(s_inversed)

t_new = -t
pos = np.searchsorted(t,t_new)
print(pos)
pos= np.clip(pos,0,len(t) -1)
mask1 = (t[pos] == t_new)

s_inversed3 = np.zeros_like(s)
s_inversed3[mask1] = s[pos[mask1]]
#s_inversed2 = s[pos]
print(s_inversed3)
