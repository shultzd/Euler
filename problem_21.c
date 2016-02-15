/*
 * Euler 21:
 *
 * Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
 * If d(a) = b and d(b) = a, where a ? b, then a and b are an amicable pair and each of a and b are called
 * amicable numbers.
 *
 * For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
 * therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
 *
 * Evaluate the sum of all the amicable numbers under 10000.
 *
 * Ans: 31626
 */

#include <stdio.h>

#define MAX_NUM 10000

long d(long num)
{
	long i;
	long sum = 0;

	for (i=1; i<(num/2+1); i++)
		if(num%i == 0)
			sum += i;

	return sum;
}

int main()
{
	long d_ans[MAX_NUM] = {0};
	long i;
	long sum;

	for(i=1; i<MAX_NUM; i++)
		d_ans[i] = d(i);

	/* Calculate the sum */
	sum = 0;
	for(i=1; i<MAX_NUM; i++)
		if(i < MAX_NUM)
			if(d_ans[i] < MAX_NUM)
				if(d_ans[i] == d_ans[i] && d_ans[d_ans[i]] == i)
					if(i != d_ans[i])
						sum += i;

	printf("The sum of all the amicable numbers under 10000 is %ld\n", sum);

	return 0;
}
