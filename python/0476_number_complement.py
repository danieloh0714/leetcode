def find_complement(num: int) -> int:
    n = 1
    while n <= num:
        n = n << 1
    return (n-1)^num
