import sys
from typing import List
from stack import Stack


class Disk:
    def __init__(self, size: int):
        self.size = size


class Pile(Stack):
    def __init__(self, initial_pile: List[Disk] = []):
        super(Pile, self).__init__()
        for disk in initial_pile:
            self.add(disk)

    def add(self, disk: Disk):
        top_disk = self.peek()
        if top_disk and disk.size > top_disk.size:
            sys.exit(f"Error! Size added disk ({disk.size}) > size top disk ({top_disk.size})")
        else:
            self.push(disk)

    def take(self):
        if not self.is_empty():
            return self.pop()
        else:
            return False

    def show(self):
        if not self.is_empty():
            return str([x.size for x in self.elements])
        else:
            return "[]"


class TowerOfHanoi:
    def __init__(self, size: int, render: bool = False):
        self.left = Pile([Disk(i) for i in range(size, 0, -1)])
        self.centre = Pile()
        self.right = Pile()
        self.piles = [self.left, self.centre, self.right]
        self.render = render
        if render:
            print(self)

    def move_pile(self, n: int, start_rod: int, end_rod: int):
        '''Move a pile of size 'n' from 'start' rod to 'end' rod'''
        aux_rod = 3 - (start_rod + end_rod)

        # Move the n-1 pile (on top of the last disk) from the starting rod 
        # to the to the auxiliari rod.
        if n > 1:
            self.move_pile(n - 1, start_rod, aux_rod)

        # Move last disk of the pile to the end rod.
        disk = self.piles[start_rod].take()
        self.piles[end_rod].add(disk)

        if self.render:
            print(self)

        # Move n-1 pile form the auxiliary rod to the end rod.
        if n > 1:
            self.move_pile(n - 1, aux_rod, end_rod)

    def __str__(self):
        return f"\n{self.left.show()}\n{self.centre.show()}\n{self.right.show()}\n"


if __name__ == "__main__":
    th = TowerOfHanoi(size=6, render=True)
    th.move_pile(6, 0, 2)
