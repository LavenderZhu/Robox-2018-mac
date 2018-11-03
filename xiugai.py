import math
xinbiaodian=[]
r=6371.0088
i=70

for i in range(-i,i+1): # latitude
    y=r*2*3.1415926*i/360
    zhouchang=math.cos(3.1415926/180*i)*r*2*3.1415926
    zhouchang=int(zhouchang)
    for x in range(-1*zhouchang/2,zhouchang/2,15): # realDistance
        xinbiaodian.append([x,y])

position=[[1,2],[2,3]] # need data
radiusCircle=[2,2] # need data
covered=[]
uncovered=xinbiaodian[:]
for xinbiaodianweizhi in xinbiaodian:
    for i in range(len(position)):
        if (xinbiaodianweizhi[0]-position[i][0])**2+(xinbiaodianweizhi[1]-position[i][1])**2<=radiusCircle[i]: # Covered
            covered.append(xinbiaodianweizhi)
            uncovered.remove(xinbiaodianweizhi)
            break
print covered
print len(covered)
print 1.0*len(covered)/len(position)