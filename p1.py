
def get_transition_function(size, file):
    transition_f = []
    for i in range(size):
        line = file.readline()[0:-1] #remove /n character
        string_arr = (line.split(","))
        floats_arr = list(map(float, string_arr))
        transition_f.append(floats_arr)
        
    return transition_f

#preprocess the file to get all the data from the MDP file
def get_all_MDP_data (file_name):
    fh = open(file_name, "r")

    size = int(fh.readline())
    
    reward_for_states = []
    for i in range(size):
        state_reward = float(fh.readline())
        reward_for_states.append(state_reward)
    
    Left = get_transition_function(size, fh)
    Up = get_transition_function(size, fh)
    Right = get_transition_function(size, fh)
    Down = get_transition_function(size, fh)

        
    fh.close()
    
    return [size, reward_for_states, Left, Up, Right, Down]


def max_action_over_sum(index, all_actions, U):
    all_action_expectation = []
    for action in all_actions:
        P_s_prime_given_s_a = action[i]
        action_expectation = sum([P_s_prime_given_s_a[j] * U[j] for j in range(len(U))])
        all_action_expectation.append(action_expectation)
    return max(all_action_expectation)


file_name = "GW1.txt"

size, rewards, Left, Up, Right, Down = get_all_MDP_data (file_name)

all_actions = [Left, Up, Right, Down]

#initialize Utility array 
U = [0] * size
gamma = 1
epsilon = 0.001

k = 0
delta = 0
while(True):
    U_cpy = U.copy()
    
    for i in range(size):
        U_cpy[i] = rewards[i] + gamma * max_action_over_sum(i, all_actions, U)
        delta = max(delta, abs(U[i])-abs(U_cpy[i]) )
    
    if (delta < epsilon):
        break
    
    k = k + 1
    if (k > 1000):
        print("k BREAK!")
        break