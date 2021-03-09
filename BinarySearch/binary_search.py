from typing import List


class BinarySearch:

    @staticmethod
    def search_old(target: float, arr: List[float], left: int, right: int) -> int:
        '''
        Binary search requires the input to be sorted
        Return: index of target, or -1 if target is not in arr
        '''
        window = right - left
        d = window // 2 + (window % 2 != 0)

        if target == arr[left]:
            return left

        elif target == arr[right]:
            return right

        elif window == 1:
            return -1  # Becasue window is just 1 but target is neither left or right.

        else:
            i = left + d  # Window middle point.
            pivot = arr[i]
            if target > pivot:
                left = i
            elif target < pivot:
                right = i
            elif target == pivot:
                return i
            return BinarySearch.search(target, arr, left, right)

    @staticmethod
    def search(target: float, arr: List[float]) -> int:
        start = 0
        end = len(arr) - 1

        while start < end:
            mid = (start + end) // 2
            if target > arr[mid]:
                start = mid + 1
            elif target < arr[mid]:
                end = mid
            elif arr[mid] == target:
                return end
        else:
            return -1


if __name__ == "__main__":
    array = sorted([1, 2, 4, 6, 2, 3, 56, 2, 214, 32, 6, 34, 7, 467, 325, 2, 4, 675, 84, 21, 1])
    print(array)
    print(BinarySearch.search(4, array))