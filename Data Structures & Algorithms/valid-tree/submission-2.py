class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list: dict[int, set[int]] = defaultdict(set)
        for key, val in edges:
            adj_list[key].add(val)
            adj_list[val].add(key)
        
        """
        undirected graph that is connected and has no cycles

        so i need to check 2 things:
        1. connected
        2. no cycles

        first is fairly easy to check.... if any value in [0 .. n - 1] is not in adj_list
        then its not connected no?

        actually im wrong, the other thing is about being able to reach every node..


        so connectedness has 2 things:
        1. everything from range(n) must be in adj_list
        2. everything is reachable from any index

        how can i compute the 2?

        im thinking more of the 2nd one


        i can do a normal visited set thing no?

        the issue is its undirected so we need extra checks

        how do we traverse an undirected graph? we make sure that we're not going to any element that is directly a parent of you
        """

        has_cycle: bool = False

        visited: set[int] = set()
        def traverse(node: int, parent: int):
            nonlocal has_cycle
            if has_cycle:
                return
            visited.add(node)
            for neighbour in adj_list[node]:
                if neighbour not in visited:
                    traverse(neighbour, node)
                elif neighbour != parent:
                    # WOAH WE HAVE A CYCLE....
                    has_cycle = True
                    return

        traverse(0, -1)

        for node in range(n):
            if node not in visited:
                print(node, "was not visited")
                return False

        return not has_cycle


        