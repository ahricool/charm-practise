def test_gene(n):
    if n<=0:
        return [[[[[1,2,3,4,5]]]]]
    else:
        yield 1


def test_gene2(n):

        return [[]]

print(next(test_gene(0)))