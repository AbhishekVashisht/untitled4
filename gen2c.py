# Python3 program to create target string, starting from 
# random string using Genetic Algorithm 
import csv
import random 
import Farm_Evaluator_Vec
# Number of individuals in each generation 
POPULATION_SIZE = 100
from random import randint
# Valid genes 
k=0
g=""
for i in range(200,4000,400):
    for j in range(200,4000,400):
        if k :
            g=g+"0"
            k=0
        else:
            g=g+"1"
            k=1

# GENES = '010101010101010101010101010101010101010110101010'
GENES=g
# Target string to be generated 
TARGET = "I love GeeksforGeeks"
  
class Individual(object): 
    ''' 
    Class representing individual in population 
    '''
    def __init__(self, chromosome): 
        self.chromosome = chromosome  
        self.fitness = self.cal_fitness() 
  
    @classmethod
    def mutated_genes(self): 
        ''' 
        create random genes for mutation 
        '''
        global GENES 
        gene = random.choice(GENES) 
        return gene 
  
    @classmethod
    def create_gnome(self): 
        ''' 
        create chromosome or string of genes 
        '''
        # global TARGET
        gnome_len = 100
        return [self.mutated_genes() for _ in range(gnome_len)] 
  
    def mate(self, par2): 
        ''' 
        Perform mating and produce new offspring 
        '''
  
        # chromosome for offspring 
        child_chromosome = [] 
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):     
  
            # random probability   
            prob = random.random() 
  
            # if prob is less than 0.45, insert gene 
            # from parent 1  
            if prob < 0.45: 
                child_chromosome.append(gp1) 
  
            # if prob is between 0.45 and 0.90, insert 
            # gene from parent 2 
            elif prob < 0.90: 
                child_chromosome.append(gp2) 
  
            # otherwise insert random gene(mutate),  
            # for maintaining diversity 
            else: 
                child_chromosome.append(self.mutated_genes()) 
  
        # create new Individual(offspring) using  
        # generated chromosome for offspring 
        return Individual(child_chromosome) 
  
    def cal_fitness(self): 
        ''' 
        Calculate fittness score, it is the number of 
        characters in string which differ from target 
        string. 
        '''
        global TARGET 

        # fitness = 0
        # for gs, gt in zip(self.chromosome, TARGET): 
            # if gs != gt: fitness+= 1
        k=0
        arr=[]
        for i in range(200,4000,400):
            for j in range(200,4000,400):
                
                if self.chromosome[k]=="1":
                    row=[]
                    row.append(i)
                    row.append(j)
                    arr.append(row)
                k=k+1
        if len(arr)!=50:
            return 3000
        f = open('turbine_loc_test.csv', 'w')

        with f:

            writer = csv.writer(f)
            r=['x','y']
            writer.writerow(r)
            for row in arr:
                writer.writerow(row)

        # value = randint(0, 6)
        # value = randint(0, 2)
        # value=0
        j=0.0
        for it in range(0,7):
            j+=1000/Farm_Evaluator_Vec.retfit(it)
        # print(j)
        # j=j/7.0
        return j
  
# Driver code 
def main(): 
    global POPULATION_SIZE 
  
    #current generation 
    generation = 1
  
    found = False
    population = [] 
  
    # create initial population 
    for _ in range(POPULATION_SIZE): 
                gnome = Individual.create_gnome() 
                population.append(Individual(gnome)) 
  
    while not found: 
  
        # sort the population in increasing order of fitness score 
        population = sorted(population, key = lambda x:x.fitness) 
  
        # if the individual having lowest fitness score ie.  
        # 0 then we know that we have reached to the target 
        # and break the loop 
        # if population[0].fitness <= 1488:
        #     found = True
        #     break
  
        # Otherwise generate new offsprings for new generation 
        new_generation = [] 
  
        # Perform Elitism, that mean 10% of fittest population 
        # goes to the next generation 
        s = int((80*POPULATION_SIZE)/100)
        new_generation.extend(population[:s]) 
  
        # From 50% of fittest population, Individuals  
        # will mate to produce offspring 
        s = int((20*POPULATION_SIZE)/100)
        for _ in range(s): 
            parent1 = random.choice(population[:65])
            parent2 = random.choice(population[:65])
            child = parent1.mate(parent2) 
            new_generation.append(child) 
  
        population = new_generation 
  
        print("Generation:  "+str(generation)+"\tString: "+str(population[0].chromosome)+"\tFitness: "+str(population[0].fitness)) 
        print(population[0].fitness )
        generation += 1
        if generation==3000:
            break
      
    print("Generation:  "+str(generation)+"\tString: "+str(population[0].chromosome)+"\tFitness: "+str(population[0].fitness)) 
  
if __name__ == '__main__': 
    main() 
