
def rank_based_rw_selection(fitness_values,selection_values):
    n = len(fitness_values)
    tot_value = sum(fitness_values)     # get total fitness
    new_list = [[fitness_values[i],i] for i in range(n)] # map fitness_values with indices 
    new_list.sort() # sort on the basis of fitness_values
    
    rank = 1
    total_rank = (n *(n+1))/2 

    # Prefix list to store the portion of roulette wheel on the basis of rank
    # It consists of cummulative protions of choromosome covered on the roulette wheel on the basis of the rank
    prefix = []
    for i in range(n):
        prefix.append((rank / total_rank) + (prefix[-1] if i!=0 else 0))
        rank+=1

    # result list to store the output of the indices that will be selected on the basis of selection values  

    result = []
    for i in selection_values:
        ans = -1
        for j in range(len(prefix)):
            if j==0 or ( j!=0 and i <= prefix[j] and i > prefix[j-1] ):
                ans = j
        result.append(new_list[ans][-1])

    # return result
    return result

if __name__ == '__main__':
    print(rank_based_rw_selection([0.2,0.3,0.5], [0.4,0.9]))
    print(rank_based_rw_selection([0.1,0.6,0.6,0.9,1.98], [0.3,0.8]))
