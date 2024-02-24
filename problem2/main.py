def pow(x, n):
    if x==0 and n==0:return None #0^0 is error
    return x**n

if __name__ == '__main__':
    print(pow(2, 3)) # 8
    print(pow(7, 2)) # 49
    print(pow(10, 5)) # 100000 
    print(pow(17, 6)) # 24137569
    print(pow(5, 3)) # 125