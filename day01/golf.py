a=list(map(int,open(0).read().split()))
o=sorted
r=o(a[1::2])
d=s=0
for x,y in zip(o(a[::2]),r):d+=abs(x-y);s+=x*r.count(x)
print(d,s)