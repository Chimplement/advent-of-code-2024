s=lambda l:all([0<abs(n-p)<4 and(p<n)==(l[0]<l[1])for p,n in zip(l,l[1:])])
d=lambda l,i:i<len(l)and(s(l[:i]+l[i+1:])or d(l,i+1))
a=b=0
for l in[list(map(int,l.split(" ")))for l in open(0).read().split("\n")if l]:a+=s(l.copy());b+=d(l,0)
print(a,b)