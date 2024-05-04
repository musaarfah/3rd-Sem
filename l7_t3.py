import random

def hash_function(n, size):
    return n % size

def hash_exp(size):
    hash_table = {}
    count = 0
    while True:
        count += 1
        random_int = random.randint(1, 100)
        hash_value = hash_function(random_int, size)
        if hash_value in hash_table:
            break  
        else:
            hash_table[hash_value] = random_int
    return count

def main():
    experiments = 50
    total_insertions = 0
    for i in range(experiments):
        total_insertions += hash_exp(150)
    average_insertions = total_insertions / experiments
    print("Average number of insertions:", average_insertions)


main()
