def contarDigitos(num):
    if num== 0:
        return 0
    return 1+contarDigitos(num//10)
