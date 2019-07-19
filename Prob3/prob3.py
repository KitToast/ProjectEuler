import math

def main():

    #Proceed by find primes factors and reducing the number into divisors.
    num = 600851475143
    primes_list = [2]
    max_prime = 2

    while (num != 1):

        if num % primes_list[-1] == 0:
            num = num / primes_list[-1]
            max_prime = primes_list[-1]
        else:
            found_prime = False
            candidate = primes_list[-1] + 1
            while(not found_prime):
                for index in range(0,len(primes_list)):

                    if(primes_list[index] >= math.sqrt(candidate)):
                        found_prime = True
                        primes_list.append(candidate)
                        break

                    if(candidate % primes_list[index] == 0):
                        break

                candidate += 1
    print(max_prime)

if __name__ == "__main__":
    main()
