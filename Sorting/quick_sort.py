from typing import List


class QuickSort:
    def partition(self, arr: List[float]) -> (List[float], List[float], float):
        pivot = arr.pop()
        big = [x for x in arr if x >= pivot]
        small = [x for x in arr if x < pivot]
        return big, small, pivot

    def sort(self, arr: List[float], ascending: bool = False) -> List[float]:
        if len(arr) <= 1:
            return arr
        bigger, smaller, pivot = self.partition(arr)
        if ascending:
            return self.sort(smaller, ascending) + [pivot] + self.sort(bigger, ascending)
        else:
            return self.sort(bigger, ascending) + [pivot] + self.sort(smaller, ascending)


if __name__ == "__main__":
    qs = QuickSort()
    print(qs.sort([1, 4, 6, 3, 4, 234, 7, 23, 1, 6, 9, 54, 2, 4], ascending=True))
