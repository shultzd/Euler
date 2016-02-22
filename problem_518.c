/*
 * Euler 518:
 *
 * Let S(n) = a+b+c over all triples (a,b,c) such that:
 *
 * a, b, and c are prime numbers.
 * a < b < c < n.
 * a+1, b+1, and c+1 form a geometric sequence.
 * For example, S(100) = 1035 with the following triples:
 *
 * (2, 5, 11), (2, 11, 47), (5, 11, 23), (5, 17, 53), (7, 11, 17),
 * (7, 23, 71), (11, 23, 47), (17, 23, 31), (17, 41, 97), (31, 47, 71), (71, 83, 97)
 *
 * Find S(10^8).
 *
 * Ans: ####
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define VAL 100000000UL
#define MAX_PRIMES 5761460UL

unsigned long primes[VAL];
unsigned long long comps[MAX_PRIMES];
unsigned long long comp_sqrs[MAX_PRIMES];
unsigned long num_primes = 0;

unsigned char is_prime_num[VAL] = {0};

void build_primes()
{
	unsigned long i, num;
	int is_prime;

	unsigned long long *prime_sqrs =
			(unsigned long long *)malloc(sizeof(unsigned long long) * MAX_PRIMES);

	primes[0] = 2;
	prime_sqrs[0] = 4;
	comps[0] = 3;
	comp_sqrs[0] = 9;
	is_prime_num[2] = 1;
	num_primes = 1;

	for(num=3; num<VAL; num++) {
		is_prime = 1;
		for(i=0; i<num_primes; i++) {
			if(prime_sqrs[i] > num)
				break;

			if(num % primes[i] == 0) {
				is_prime = 0;
				break;
			}
		}

		if(is_prime) {
			primes[num_primes] = num;
			comps[num_primes] = num + 1;
			comp_sqrs[num_primes] = (num + 1) * (num + 1);
			prime_sqrs[num_primes] = num * num;
			is_prime_num[num] = 1;

			num_primes++;
		}
	}

	free(prime_sqrs);
}

int main()
{
	unsigned long a, c;
	unsigned long prime_b;
	unsigned long sum = 0;
	unsigned long long b_comp_2;

	/* Workaround - turn off console buffering */
	setvbuf (stdout, NULL, _IONBF, 0);

	printf("searching for all primes under %lu\n", VAL);
	build_primes();
	printf("found %lu primes\n", num_primes);

	printf("looking for triples...\n");
	for(a=0; a<(num_primes-2); a++) {
		for (c =a+2; c<num_primes; c++) {
			b_comp_2 = (comps[a]) * (comps[c]);
			prime_b = (unsigned long) sqrt(b_comp_2) - 1;
			if(is_prime_num[prime_b] == 1)
				if(((prime_b+1)*(prime_b+1)) == b_comp_2)
					sum += primes[a] + prime_b + primes[c];
		}
	}

	printf("\nS(%lu) = %lu\n", VAL, sum);

	return 0;
}


