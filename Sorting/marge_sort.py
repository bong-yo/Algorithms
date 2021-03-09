from typing import List


class MergeSort:
    def merge_sort(self, b1: List[float], b2: List[float]) -> List[float]:
        '''Merges 2 sorted buckets b1 and b2'''
        res = []
        m = n = 0
        while m < len(b1) and n < len(b2):
            if b1[m] <= b2[n]:
                res.append(b1[m])
                m += 1
            else:
                res.append(b2[n])
                n += 1
        # Append reminder of the less used of the 2 buckets.
        res += b2[n:] if m == len(b1) else b1[m:]
        return res

    def sort(self, arr: List[float]) -> List[float]:
        # Put each number in its own bucket.
        buckets = [[x] for x in arr]
        while len(buckets) > 1:
            buckets = [
                self.merge_sort(buckets[i], buckets[i + 1])
                for i in range(0, len(buckets) - 1, 2)
            ]
        return buckets[0]


if __name__ == "__main__":
    ms = MergeSort()
    print(ms.sort([2, 4, 65, 3, 21, 5, 3, 7, 2]))
