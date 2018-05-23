n = 4
a = [4,5,10,20]

max_len = 0

triangles = []

def checktriangle(triangle):
    result = None
    if triangle[2] < triangle[0] + triangle[1]:
        result = True
    else:
        result = False
    return result

def main():
    triangle = [0, 0, 0]
    for _i in range(len(a) - 2):
        triangle[0] = a[_i]
        for __i in range(len(a) - _i - 1):
            triangle[1] = a[__i + _i + 1]
            i = __i + _i + 1
            for ___i in range(len(a) - i - 1):
                triangle[2] = a[___i + __i + 1 + _i + 1]    
                b = checktriangle(triangle)
                if b:
                    global max_len
                    max_len = triangle[0] + triangle[1] + triangle[2]



if __name__ == '__main__':
    main()
    print(max_len)
