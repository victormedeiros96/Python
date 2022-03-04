def parallel(*resistances):
    # resistances is any iterable with value-type as string, int, or float
    # so we need to cast type to float
    conductance = [1/float(r) for r in resistances]
    conductance_sum = sum(conductance)
    resistance_result = 1/conductance_sum
    return resistance_result
def series(*resistances):
    # resistances is any iterable with value-type as string, int, or float
    # so we need to cast type to float
    resistances = [float(r) for r in resistances]
    resistance_result = sum(resistances)
    return resistance_result
def _tests():
    print(series(1))
    print(series(4,4))
    print(series(12,12,12,12))
    print(parallel(1))
    print(parallel(4,4))
    print(parallel(12,12,12,12))
if __name__=='__main__':
    _tests()