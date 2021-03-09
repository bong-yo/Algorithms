from typing import List


class Object:
    def __init__(self, key: int):
        self.key = key
        self.attr = []

    def __str__(self):
        return str(self.key)


class CountSort:
    def __init__(self, number_of_keys: int):
        self.K = number_of_keys
        # Initialize list of k empty lists.
        self.sorting_counter = [[] for i in range(self.K)]

    def sort(self, arr: List[Object]) -> List[Object]:
        # Append object at the 'self.sorting_counter' index equals
        # to its integer key.
        for x in arr:
            self.sorting_counter[x.key].append(x)

        # Linear taverse 'self.sorting_counter' and add the list of objects 
        # of each index to res.
        res = []
        for objs in self.sorting_counter:
            if objs:
                res.extend(objs)
        return res


if __name__ == "__main__":
    inp = [1, 4, 6, 3, 4, 234, 7, 23, 1, 6, 9, 54, 2, 4]
    num_keys = max(inp) + 1
    inp = [Object(x) for x in inp]

    cs = CountSort(num_keys)
    for x in cs.sort(inp):
        print(x)
