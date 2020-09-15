import csv

arrr=[]
X=[1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1,
 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0,
 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1,
 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0,0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1,
 0, 1, 0, 1]
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