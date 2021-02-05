from time import time
from collections import defaultdict
import numpy as np


class LCS_brute:
    def __init__(self, s1, s2):
        self.a = list(s1)
        self.b = list(s2)
        self.seq = set()
        self.max_seq_len = 0
        start = time()
        self.lcs_find()
        print(f"time : {time()-start} sec.")

    def lcs_find(self, m=0, n=0, s=""):
        if m == len(self.a) or n == len(self.b):
            self.save_seq(s)
            return 0

        elif self.a[m] == self.b[n]:
            s += self.a[m]
            return 1 + self.lcs_find(m + 1, n + 1, s)

        else:
            return max(self.lcs_find(m, n + 1, s), self.lcs_find(m + 1, n, s))

    def save_seq(self, s):
        '''Save all longest common seq. (that have same len)'''
        if not self.seq:
            self.seq = set([s])
            self.max_seq_len = len(s)
        elif len(s) == self.max_seq_len:
            self.seq.add(s)
        elif len(s) > self.max_seq_len:
            self.seq = set([s])
            self.max_seq_len = len(s)
        else:
            return


class LCS_DP:
    def __init__(self, s1, s2):
        self.a = list(s1)
        self.b = list(s2)
        self.M = len(s1) - 1
        self.N = len(s2) - 1
        self.seqs_names = set([])
        self.lcs_table = np.zeros((self.M + 2, self.N + 2), dtype=int)
        self.lcs_path = defaultdict(lambda: defaultdict(str))
        self.max_seq_len = 0
        start = time()
        self.build_lcs_table()
        self.max_seq_len = self.lcs_find()
        self.get_seqs_names()
        print(f"time : {time() - start} sec.")

    def build_lcs_table(self):
        for m in range(self.M, -1, -1):
            for n in range(self.N, -1, -1):
                if self.a[m] == self.b[n]:
                    # Adding 1 from the lcm(m-1, n-1) avoids double counting matches
                    # when already happened that a[m] = b[n] for another n and same m
                    # or another m and same n (in which case we don't want
                    # to add 1 from the lcm(m, n + 1) or lcm(m + 1, n)).
                    self.lcs_table[m, n] = self.lcs_table[m + 1, n + 1] + 1
                    self.lcs_path[m][n] = "bingo"
                else:
                    # If no match -> propagate normally the highest lcs.
                    if self.lcs_table[m + 1, n] > self.lcs_table[m, n + 1]:
                        self.lcs_table[m, n] = self.lcs_table[m + 1, n]
                        self.lcs_path[m][n] = "down"
                    elif self.lcs_table[m + 1, n] < self.lcs_table[m, n + 1]:
                        self.lcs_table[m][n] = self.lcs_table[m, n + 1]
                        self.lcs_path[m][n] = "right"
                    else:
                        self.lcs_table[m][n] = self.lcs_table[m, n + 1]
                        self.lcs_path[m][n] = "left & right"

    def lcs_find(self):
        return self.lcs_table[0, 0]

    def get_seqs_names(self, m=0, n=0, s=""):
        if self.lcs_table[m, n] == 0:  # End of the sequence.
            self.seqs_names.add(s)
            return
        elif self.lcs_path[m][n] == "bingo":
            s += self.a[m]
            self.get_seqs_names(m + 1, n + 1, s)
        elif self.lcs_path[m][n] == "down":
            self.get_seqs_names(m + 1, n, s)
        elif self.lcs_path[m][n] == "right":
            self.get_seqs_names(m, n + 1, s)
        elif self.lcs_path[m][n] == "left & right":
            self.get_seqs_names(m + 1, n, s)
            self.get_seqs_names(m, n + 1, s)


if __name__ == "__main__":
    s1 = "areggtgbdtrtgwg"
    s2 = "qagwegtethewtgrdahfgf"
    print(f"\n\n\n\nseq1 : {s1}\nseq2 : {s2}\n")

    print("\n   **** Brute Force ****")
    lcs = LCS_brute(s1, s2)
    print(f"lcs lenght : {lcs.max_seq_len}")
    print(f"lcs names : {sorted(list(lcs.seq))}")

    print("\n   **** DP ****")
    lcs = LCS_DP(s1, s2)
    print(f"lcs lenght : {lcs.max_seq_len}")
    print(f"lcs names : {sorted(list(lcs.seqs_names))}")
