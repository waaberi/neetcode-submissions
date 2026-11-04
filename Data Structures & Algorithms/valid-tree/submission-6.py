class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list: dict[int, list[int]] = defaultdict(list)
        for key, val in edges:
            adj_list[key].append(val)
            adj_list[val].append(key)

        visited: set[int] = set()
        def has_cycle_func(node: int, parent: int) -> int:
            visited.add(node)
            for neighbour in adj_list[node]:
                if neighbour not in visited:
                    if has_cycle_func(neighbour, node):
                        return True
                elif neighbour != parent:
                    return True
            return False

        has_cycle = has_cycle_func(0, -1)

        for node in range(n):
            if node not in visited:
                return False

        return not has_cycle