def main():
    n = int(input())

    if n == 0:
        print("0 0 0")
        return

    if n == 1:
        print("0 0 1")
        return

    m2 = 2
    m = -1
    z = 1
    f = 0
    s = 1

    while 1:
        a = f
        b = s

        m2 = m
        m = z
        z = f
        f = s
        s = a + b

        if s == n:
            print(f, m, m2)
            return
main()
        
        
