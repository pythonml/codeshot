import math

def is_prime(x):
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0:
            return False
    return True

if __name__ == "__main__":
    num = 101
    result = is_prime(num)
    if result:
        print("{} is a prime number".format(num))
    else:
        print("{} is not a prime number".format(num))
