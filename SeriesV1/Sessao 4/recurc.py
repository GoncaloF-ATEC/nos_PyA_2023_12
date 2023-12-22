

def somador(n:int) -> int:
    if n == 0:
        return n
    else:
       return n + somador(n-1)

print(somador(5)) # 15


"""
15
5 + somador(4)
4 + somador(3)
3 + somador(2)
2 + somador(1)
1 + 0


"""