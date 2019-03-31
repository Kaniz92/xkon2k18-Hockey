import numpy
import genetic_calc

class Genetic:
    def __init__(self):
        self.initial_values = None

    def calculatePopulation(self,initial_values):

        # Pass game parameters here
        initial_values = initial_values#[4,-2,3.5,5,-11,-4.7]

        # Each step characteristics should represent here
        # start state of puke/disk
        # end state of disk
        # behavior- movements
        step_genes = len(initial_values)

        """
        Genetic algorithm parameters:
            Mating pool size
            Population size
        """
        sol_per_pop = 8
        num_parents_mating = 4

        # Defining the population size.
        pop_size = (sol_per_pop,step_genes) # The population will have sol_per_pop chromosome where each chromosome has step_genes genes.
        #Creating the initial population.
        new_population = numpy.random.uniform(low=-4.0, high=4.0, size=pop_size)
        print(new_population)

        """
        new_population[0, :] = [2.4,  0.7, 8, -2,   5,   1.1]
        new_population[1, :] = [-0.4, 2.7, 5, -1,   7,   0.1]
        new_population[2, :] = [-1,   2,   2, -3,   2,   0.9]
        new_population[3, :] = [4,    7,   12, 6.1, 1.4, -4]
        new_population[4, :] = [3.1,  4,   0,  2.4, 4.8,  0]
        new_population[5, :] = [-2,   3,   -7, 6,   3,    3]
        """

        best_outputs = []
        num_generations = 1000
        for generation in range(num_generations):
            print("Generation : ", generation)
            # Measuring the fitness of each chromosome in the population.
            fitness = genetic_calc.cal_pop_fitness(initial_values, new_population)
            print("Fitness")
            print(fitness)

            best_outputs.append(numpy.max(numpy.sum(new_population*initial_values, axis=1)))
            # The best result in the current iteration.
            print("Best result : ", numpy.max(numpy.sum(new_population*initial_values, axis=1)))
            
            # Selecting the best parents in the population for mating.
            parents = genetic_calc.select_mating_pool(new_population, fitness, 
                                            num_parents_mating)
            print("Parents")
            print(parents)

            # Generating next generation using crossover.
            offspring_crossover = genetic_calc.crossover(parents,
                                            offspring_size=(pop_size[0]-parents.shape[0], step_genes))
            print("Crossover")
            print(offspring_crossover)

            # Adding some variations to the offspring using mutation.
            offspring_mutation = genetic_calc.mutation(offspring_crossover)
            print("Mutation")
            print(offspring_mutation)

            # Creating the new population based on the parents and offspring.
            new_population[0:parents.shape[0], :] = parents
            new_population[parents.shape[0]:, :] = offspring_mutation
            
        # Getting the best solution after iterating finishing all generations.
        #At first, the fitness is calculated for each solution in the final generation.
        fitness = genetic_calc.cal_pop_fitness(initial_values, new_population)
        # Then return the index of that solution corresponding to the best fitness.
        best_match_idx = numpy.where(fitness == numpy.max(fitness))

        print("Best solution : ", new_population[best_match_idx, :])
        print("Best solution fitness : ", fitness[best_match_idx])


        import matplotlib.pyplot
        matplotlib.pyplot.plot(best_outputs)
        matplotlib.pyplot.xlabel("Iteration")
        matplotlib.pyplot.ylabel("Fitness")
        matplotlib.pyplot.show()