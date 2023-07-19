def check_prime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i == 0:           #The number is divisible by any number less than itself kem ke n-1 sudhi j loop jase toh ee prime nathi
                return False
        return True

print(check_prime(9))