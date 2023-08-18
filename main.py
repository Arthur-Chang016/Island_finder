
def rec(source, sink, dp, graph):
    if source == sink: return True
    if dp[source][sink] != -1: return dp[source][sink]
    # not found
    if len(graph[source]) == 0:
        dp[source][sink] = False
        return False
    for child in graph[source]:
        if rec(child, sink, dp, graph) == False:
            dp[source][sink] = False
            return False
    dp[source][sink] = True
    return True

def reverse(graph):
    N = len(graph)
    rev = [[] for _ in range(N)]
    for parent in range(N):
        for child in graph[parent]:
            rev[child].append(parent)
    return rev

def InOutDegree(graph):
    N = len(graph)
    inD = [0] * N
    outD = [0] * N
    for parent in range(N):
        for child in graph[parent]:
            inD[child] += 1
            outD[parent] += 1
    return inD, outD
    

def solve(graph):
    N = len(graph)
    inDegree, outDegree = InOutDegree(graph)
    # reverse graph
    revserseG = reverse(graph)
    
    # init memo for DP
    forwardDP = [([-1] * N) for _ in range(N)]
    backwardDP = [([-1] * N) for _ in range(N)]
    
    # print all islands
    for i in range(N):
        for j in range(N):
            inout = (inDegree[i] == 1 or inDegree[i] == 0) and (outDegree[j] == 0 or outDegree[j] == 1)
            if inout and rec(i, j, forwardDP, graph) and rec(j, i, backwardDP, revserseG):
                print(f"{i}, {j}")


def main():
    graph = [[1, 2], [3, 4], [], [4], []]
    
    solve(graph)
    

if __name__ == "__main__":
    main()