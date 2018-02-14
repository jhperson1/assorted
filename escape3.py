#!/user/bin/env/Python

import Queue

def build_adj_list(n,k,f):
    pairs = {}
    for i in range(1,n+1):
        for j in range(1,n+1):
            for key in range (0,k):
                new = pairs.get( (f[key][i-1] , f[key][j-1]) , set())
                new.add((i,j))
                pairs[(f.get(key, [])[i-1] , f.get(key, [])[j-1])] = new
    return pairs

def BFS(n,k,f):
    E = build_adj_list(n,k,f)
    target = n ** 2
    seen_pairs = {}
    for vertex in range(1, n+1):
        q = Queue.Queue()
        q.put((vertex, vertex))
        seen = set()
        while q.qsize() > 0:
            e = q.get()
            seen.add(e)
            neighbors = E.get(e,[])
            for neighbor in neighbors:
                x = seen_pairs.get(neighbor,0)
                if x != 0:
                    seen.add(neighbor)
                    seen = seen.union(x,seen)
                elif not neighbor in seen:
                    q.put(neighbor)
        seen_pairs[(vertex,vertex)] = seen
        if len(seen) == target:
            print "YES"
            return
    print "NO"
    return

def main():
    T = map (int, raw_input().split(' '))
    for test in range(T[0]):
        n, k = map (int, raw_input().split(' '))
        f = {}
        for key in range(k):
            f[key] = ( map (int, raw_input().split(' ')) )
        BFS(n,k,f)

if __name__ == "__main__":
    main()