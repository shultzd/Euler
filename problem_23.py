# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the 
# proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant 
# numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two 
# abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest 
# number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# ans = 4179871

import time

#########################################################
MIN_ABUNDANT = 12
ABUNDANT_LIMIT = 28123

abundant_list = []
abundant_sums_list = []
            
            
#########################################################
# Fill the abundant_list and primes_list lists
#########################################################
def generate_lists():
    for i in range(1, ABUNDANT_LIMIT + 1):
        sum = 0
        for div in range(1, int(i/2)+1): #int(math.sqrt(i)) + 1
            if(i % div == 0):
                sum += div
        
        if(sum > i):
            abundant_list.append(i)

#########################################################
def find_all_sums():
    global abundant_sums_list
    
    for i in abundant_list:
        for j in abundant_list:
            temp_sum = i + j
            if(temp_sum <= ABUNDANT_LIMIT):
                abundant_sums_list.append(temp_sum)

#########################################################
def euler_problem_23():
    print "Problem 23:"
    
    generate_lists()
    find_all_sums()
    
    abundant_sums_set = set(abundant_sums_list)
    full_set = set(range(1, ABUNDANT_LIMIT+1))
    final_set = full_set - abundant_sums_set
     
    ans = sum(list(final_set))
    
    print ans


#########################################################
start_time = time.time()
euler_problem_23()
end_time = time.time()

print "total calculation time is ", (end_time - start_time), " [Sec]"
