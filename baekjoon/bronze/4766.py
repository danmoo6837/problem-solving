from sys import stdin

input = stdin.readline

if __name__== "__main__":
    t = float(input())
    if t == 999:
        exit()

    while True:
        t1 = float(input())
        if t1 == 999:
            break
        
        print(f"{t1-t:.2f}")
        t=t1