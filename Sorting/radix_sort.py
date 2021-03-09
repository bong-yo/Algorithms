from typing import List


class RadixSort:
    def __init__(self, base: int = 10):
        self.b = base  # Usulaly digits are in base 10, however base=n is usually the most conveninet.

    def count_sort(self, arr: List[int], digit_pos: int, method: int = 1) -> List[int]:
        power_of_base = self.b ** digit_pos
        if method == 1:  ### METHOD 1 #####
            counter = [0] * self.b
            for num in arr:
                # Get digit in position 'digit_pos'
                digit = self.get_digit(num, power_of_base)
                counter[digit] += 1
            # Modify 'counter' so that the value stored at each index represents 
            # the position in 'arr' where to place the nums with that value at 'digit pos'.
            # This turns out to be achieved by cumulative sum of counter, 
            # as the index in arr where to start storing nums with value 3 
            # will come after all nums with value 0 plus all 1s plus all 2s (i.e cumsum).
            for i in range(1, self.b):
                counter[i] += counter[i - 1]

            output = [0] * len(arr)
            for i in range(len(arr) - 1, -1, -1):
                num = arr[i]
                digit = self.get_digit(num, power_of_base)
                index = counter[digit] - 1  # Becasue arr is 0-based and the cumsum is 1-based.
                output[index] = num
                counter[digit] -= 1  # Next time I encounter a num with digit = digit, it will go 1 position closer to index=0 in arr.
            return output

        else:  ### METHOD 2 #####
            counter = [[] for i in range(self.b)]
            for num in arr:
                # Get digit in position 'digit_pos'.
                digit = self.get_digit(num, power_of_base)
                counter[digit].append(num)
            # Replace the elements of arr with the ones sorted according to 
            # the 'digit_pos' digit.
            i = 0
            for sorted_nums in counter:
                for sorted_num in sorted_nums:
                    arr[i] = sorted_num
                    i += 1
            return arr

    def sort(self, arr: List[int]) -> List[int]:
        max_digit = self.get_max_digit(arr)
        #  Partial sort according to every digit position.
        for d in range(max_digit):
            arr = self.count_sort(arr, d)
        return arr

    def get_digit(self, num, power_of_base):
        return (num // power_of_base) % self.b

    def get_max_digit(self, arr):
        maxd = max(arr)
        if maxd == 0:
            return 0
        else:
            return len(str(maxd))


if __name__ == "__main__":
    inp = [1, 4, 6, 3, 4, 234, 7, 23, 1, 6, 9, 54, 2, 4]
    rs = RadixSort()
    print(rs.sort(inp))
