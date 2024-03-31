def factorization(n):
    factors = [i for i in range(1, n+1) if n % i == 0]
    return factors

def differentiation(pow_cff):
    pow_cff_prime =  {}
    for i in pow_cff.keys():
        if i - 1 >= 0:
            pow_cff_prime[(i-1)] = i * pow_cff[i]
        else:
            break
    return pow_cff_prime

def zeros(highest_degree, cff):
    zeros_x = []
    
    # Taking the highest degree of the function
    try:
        highest_degree = int(highest_degree)
        
    except:
        print("Please input a valid integer")
    
    # Taking the coefficients of the terms
    pow_cff = {}
    for i in reversed(range(highest_degree + 1)):
        pow_cff[i] = int(cff[(i * -1) - 1])

    # Removing the terms with 0 cocfficient
    temp = pow_cff.copy()
    for i in temp:
        if pow_cff[i] == 0:
            pow_cff.pop(i)
    highest_degree = max(pow_cff)

    # Removing the constant term 0, if found
    if 0 not in pow_cff:
        zeros_x.append(0)
        decrease = min(pow_cff)
        temp = {}
        for i in pow_cff:
            temp[i-decrease] = pow_cff[i]
        pow_cff = temp.copy()

    # Finding the Fators of the constant and leading terms
    lt_f = factorization(int(str(pow_cff[highest_degree]).lstrip('-')))
    ct_f = factorization(int(str(pow_cff[0]).lstrip('-')))

    # Finding all the possible zeros of the function
    possible_zeros = set()
    for j in ct_f:
        for k in lt_f:
            for y in [1, -1]:
                possible_zeros.add((j/k) * y)
    possible_zeros = list(possible_zeros)


    # Finding the actual zeros of the function
    cnt = highest_degree
    for p in possible_zeros:
        res = 0
        for k in pow_cff.keys():
            res += pow_cff[k] * (int(p) ** k)
        if res == 0:
            zeros_x.append(int(p))
            cnt -= 1
            if cnt == 0:
                break
            
    # Finding the multiplicity of the zeros
    zero_mul = {}
    cnt = 1
    for i in range(len(zeros_x)):
        derivative = differentiation(pow_cff)
        while True:
            res = 0
            for j in derivative.keys():
                res += (zeros_x[i] ** j) * derivative[j]
            if res == 0:
                cnt += 1
                derivative = differentiation(derivative)
            else:
                zero_mul[zeros_x[i]] = cnt
                cnt = 1
                break

    # Returning the outputs
    if len(zeros_x) > 0:
        return f"The zeros of the function with their coefficients are {zero_mul}"
    else:
        return "There are no rational zeros for the function. All the zeros are either decimal or complex numbers"