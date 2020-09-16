import csv
import Farm_Evaluator_Vec2
arrr=[]
X=[1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0,
 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0,
 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1,
 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1,0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1,
 1, 1, 1, 1]
# X=[1. 1. 1. 0. 1. 1. 1. 0. 1. 1. 0. 0. 0. 1. 0. 0. 0. 1. 0. 1. 1. 1. 0. 0.
#  0. 1. 0. 0. 0. 1. 1. 0. 0. 1. 0. 0. 1. 0. 1. 1. 1. 0. 0. 0. 1. 0. 0. 0.
#  0. 1. 1. 0. 1. 0. 0. 1. 0. 1. 0. 1. 1. 0. 0. 1. 0. 0. 1. 0. 0. 1. 1. 1.
#  0. 0. 1. 1. 0. 1. 0. 1. 1. 0. 1. 0. 0. 0. 0. 0. 0. 1. 1. 1. 1. 0. 1. 1.
#  1. 1. 1. 1.]
for i in range(200, 4000, 400):
    for j in range(200, 4000, 400):
        row = []
        row.append(i)
        row.append(j)
        arrr.append(row)
temp = []
for i in range(0,100):
    if X[i]:

        t=arrr[i]
        temp.append(t)

f = open('turbine_loc_testf.csv', 'w')

with f:

    writer = csv.writer(f)
    r = ['x', 'y']
    writer.writerow(r)
    for row in temp:
        writer.writerow(row)



j = 0
for it in range(0, 7):
    mt= int(Farm_Evaluator_Vec2.retfit(it))


    j +=mt

print(j)
for i in range(0,100):
    if X[i]:
        print(" 1 ", end =" ")
    else:
        print("   ", end =" ")
    if (i+1)%10==0:
        print("\n")
