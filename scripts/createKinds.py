import json
import itertools



def create_kinds():
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    kinds_amount_max = 1000
    kind_amount = 0
    kinds = []
    for L in range(0, len(alphabet)+1):
        for subset in itertools.combinations(alphabet, L):
            kind_amount += 1
            kinds.append("".join(list(subset)))
            if (kind_amount >= kinds_amount_max):
                break
        if (kind_amount >= kinds_amount_max):
            break
    return kinds[1:]


def write_kinds():
    kind_path = "data/kinds.json"
    with open(kind_path, 'w') as f:
        d = { "kinds": create_kinds()}
        json.dump(d, f)


write_kinds()