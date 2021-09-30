#Dijkstra's shortest path algorithm

inf = float('inf')
N = [
	{1:2, 2:1, 3:3, 4:9, 5:4}, # 0
	{2:4, 4:3}, # 1
	{3:8}, # 2
	{4:7}, # 3
	{5:5}, # 4
	{2:2, 6:2, 7:2}, # 5
	{5:1, 7:6}, # 6
	{5:9, 6:8} # 7
    ]

def shortest_path(list):
    result = []

    def sf
