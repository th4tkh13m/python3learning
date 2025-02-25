###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    num_count = len(cows)
    spaceship_list = []
    cow_dict_sorted = dict(sorted(cows.items(), key = lambda cows: cows[1], reverse = True))
    while num_count > 0 :
        spaceship = []
        avail = limit
        for k, v in cow_dict_sorted.items():
            if avail < v:
                continue
            else:
                spaceship.append(k)
                avail -= v
        for element in spaceship:
            cow_dict_sorted.pop(element)
        num_count -= len(spaceship)
        spaceship_list.append(spaceship)
    return spaceship_list


# Problem 2
def brute_force_cow_transport_1(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    memo = {}
    result = []
    trips = len(cows)
    for item in get_partitions(cows.keys()):
        for element in item:
            con = True
            memo_key = tuple(element)
            if memo_key not in memo:
                memo[memo_key] = sum([cows[name] for name in element])
            if memo[memo_key] > limit:
                con = False
                break
        if len(item) <= trips and con:
            trips = len(item)
            result = item
    return result

def brute_force_cow_transport_2(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    result = []
    trips = len(cows)
    for item in get_partitions(cows.keys()):
        for element in item:
            con = True
            if sum([cows[name] for name in element]) > limit:
                con = False
                break
        if len(item) <= trips and con:
            trips = len(item)
            result = item
    return result



            

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
print(cows)

start = time.time()
## code to be timed
print(greedy_cow_transport(cows, limit))
end = time.time()
print('greedy',end - start)

start = time.time()
## code to be timed
print(brute_force_cow_transport_1(cows, limit))
end = time.time()
print('bruteforce 1',end - start)

start = time.time()
## code to be timed
print(brute_force_cow_transport_2(cows, limit))
end = time.time()
print('bruteforce 2',end - start)




