
import numpy as np
import Farm_Evaluator_Vec
from geneticalgorithm import geneticalgorithm as ga
import csv
arrr=[]
k=0
for i in range(200, 4000, 400):
    for j in range(200, 4000, 400):
        row = []
        row.append(i)
        row.append(j)
        arrr.append(row)

# print(len(arrr))



def f(X):
    l=0
    temp = []
    for i in range(0,100):
        if X[i]:

            t=arrr[i]
            temp.append(t)
            l=l+1

    if l!=50:
        # print(l)
        return  35000+55000*abs(50-l)
    f = open('turbine_loc_test.csv', 'w')

    with f:

        writer = csv.writer(f)
        r = ['x', 'y']
        writer.writerow(r)
        for row in temp:
            writer.writerow(row)

    # value = randint(0, 6)
    # value = randint(0, 2)
    # value=0
    j = 0
    for it in range(0, 7):
        mt= int(Farm_Evaluator_Vec.retfit(it))


        j +=mt

    print(j)
    if j > 3534:
        f = open('turbine_loc_test2.csv', 'w')

        with f:

            writer = csv.writer(f)
            r = ['x', 'y']
            writer.writerow(r)
            for row in temp:
                writer.writerow(row)

    return (21000-int(j))

# def f(x):
#     return -1*np.sum(x)
# for i in range(0,50):
#     row = []
#     row.append(i)
#     row.append(i+4)
#     arrr.append(row)
#     contr=
# varbound=np.array([[0,99]]*50)
algorithm_param = {'max_num_iteration': 1000,\
                   'population_size':300,\
                   'mutation_probability':0.1,\
                   'elit_ratio': 0.5,\
                   'crossover_probability': 0.9,\
                   'parents_portion': 0.8,\
                   'crossover_type':'one_point',\
                   'max_iteration_without_improv':None}
model=ga(function=f,dimension=100,variable_type='bool',algorithm_parameters=algorithm_param)
model.run()
print("ff")
# print(model.output_dict)
