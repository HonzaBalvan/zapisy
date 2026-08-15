def from_permutation_to_disjoints_cycles(perm):
    #mappings = { a: b for a, b in zip(*perm) }
    mappings = perm
    cycles = []
    for a in perm[0]:
        b = mappings.pop(a, None)
        if b is None:
            continue # `a` has already been handled
        cycle = [a]
        while a != b:
            cycle.append(b)
            b = mappings.pop(b)
        cycles.append(cycle)
    return cycles

inp = [int(x) for x in input().split()]
outp = from_permutation_to_disjoints_cycles(inp)
print(*outp)
