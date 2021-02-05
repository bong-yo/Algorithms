from os.path import dirname, abspath


class Paths:
    CURR_DIR = dirname(abspath(__file__))
    ALGO_DIR = dirname(CURR_DIR)
    DS_DIR = f"{dirname(ALGO_DIR)}/DataStructures"
    QUEUE_DIR = f"{DS_DIR}/Queues"
    UNIONFIND_DIR = f"{DS_DIR}/UnionFind"
