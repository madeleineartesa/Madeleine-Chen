import random

##list of random charge pairs
charge_pairs=[]
while len(charge_pairs)<100:
    new_pair=[random.randint(-100,100), random.randint(-100,100)]
    if new_pair[0]==0 or new_pair[1]==0:
        continue
    charge_pairs.append(new_pair)

##list of distances
dists=[]
for dist in range(100):
    dists.append(random.randint(1,50))

##table headings
print(" C1 ", " C2 ", "  Force (N)", "    Dir", "    Type")

#finding required values
rows=[]
for x in range(100):
    ##charge
    c1=charge_pairs[x][0]
    c2=charge_pairs[x][1]

    ##force
    k=8.99*10**9
    distance=dists[x]
    force=k*(c1**-9)*(c2**-9)/distance**2
    
    ##type and direction
    if (c1<0 and c2<0) or (c1>0 and c2>0) and (c1>c2):
        type="repulsive"
        direction="left"

    if (c1<0 and c2<0) or (c1>0 and c2>0) and (c1<c2):
        type="repulsive"
        direction="right"

    if (c1>0 and c2<0) or (c1<0 and c2>0) and (c1>c2):
        type="attractive"
        direction="right"

    if (c1>0 and c2<0) or (c1<0 and c2>0) and (c1<c2):
        type="attractive"
        direction="left"
    
    answers=[c1,c2,force,direction,type]
    rows.append(answers)

##printing table
from tabulate import tabulate
print(tabulate(rows))