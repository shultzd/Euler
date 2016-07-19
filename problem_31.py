# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
# 
#     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#
# It is possible to make £2 in the following way:
# 
#     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#
# How many different ways can £2 be made using any number of coins?
#
# ans = 73682

#########################################################
import time

#########################################################
num_coins = 8
NO_COIN = 100
coin_values = [1, 2, 5, 10, 20, 50, 100, 200] # values are in pence[p]
target_value = 200#200

#########################################################
def recursive_solve(coins, coin_id = NO_COIN):
    num_options = 0
    
    if coin_id != NO_COIN:
        coins[coin_id] += 1
    sum_coins = sum([a*b for a,b in zip(coins, coin_values)]) 
    
    if sum_coins == target_value:
        return 1
    elif sum_coins > target_value:
        return 0
    
    if coin_id == NO_COIN: 
        starting_coin = 0
    else: 
        starting_coin = coin_id
    for coin_id in range(starting_coin, num_coins):
        num_options += recursive_solve(coins[:], coin_id)
    
    return num_options

#########################################################
def euler_problem_31():
    print "Problem 31:"
    
    
    ans = recursive_solve([0,0,0,0,0,0,0,0])
    
    print "ans = ", ans

#########################################################
start_time = time.time()
euler_problem_31()
end_time = time.time()

print "total calculation time is ", (end_time - start_time), " [Sec]"
