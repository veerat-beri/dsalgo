def is_armstrong(num: int):
    sum = 0
    while num:
        rem = num % 10
        quotient = num / 10
        num = quotient
        sum = sum + pow(rem, 3)
        if sum > num:
            break
    if sum == num:
        return True
    return False


# driver code
def run():
    pass
