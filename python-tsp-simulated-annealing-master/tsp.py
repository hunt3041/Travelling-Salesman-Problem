from nodes_generator import NodeGenerator
from simulated_annealing import SimulatedAnnealing


def main():
    '''set the simulated annealing algorithm params'''
    temp = 50
    stopping_temp = 0.00000001
    alpha = 0.999
    stopping_iter = 150000

    '''set the dimensions of the grid'''
    size_width = 100
    size_height = 100

    '''set the number of nodes'''
    population_size = 101

    '''generate random list of nodes'''
    nodes = NodeGenerator(size_width, size_height, population_size).generate()
    
    '''run simulated annealing algorithm with 2-opt'''
    sa = SimulatedAnnealing(nodes, temp, alpha, stopping_temp, stopping_iter)
    sa.anneal()

    '''animate'''
    sa.animateSolutions()
    # sa.animateSingle()

    '''show the improvement over time'''
    sa.plotLearning()


if __name__ == "__main__":
    main()
