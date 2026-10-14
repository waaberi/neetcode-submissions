"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        we're gonna dfs through it
        i will maintain a visited set
        any time i visit an element i need to add it to the visited set before going through its neighbours
        that will prevent loops.

        think about 2 things:
        - what to return, we decided dfs returns the copy
        - copy mechanism:
            - making a new node is straight forward
            - im thinking more about self.neighbours
            - what we can do is we just do something like Node(current_node.val, [dfs(next_node) for next_node in current_node.neighbours])

        ok this seems like it settles it for me
        the only other thing would be to think about if dfs on its own would NOT work
        do we need backtracking? i dont think so.
        i will stick to dfs.

        there is one last thing i need to do 

        i maintain a visited set but i still have to return SOMETHING on those cases no?
        if i dont return anything on those cases then what will happen is that i will have empty references in some places somehow (at least i think so)
        the trivial fix is to use a dict instead.
        but it is possible that im wrong and that we dont need all of that.

        ill do a mapping of og reference to copied reference
        """

        visited_dict: dict[Optional['Node'], Optional['Node']] = {}

        def dfs(current_node: Optional['Node']) -> Optional['Node']:
            if current_node is None:
                return None
            if current_node in visited_dict:
                return visited_dict[current_node]
            """
            tthis is a bit tricky, but essentially im still getting infinite recursion
            because i mark it as visited AFTER
            how can i mark it as visited before?
            """
            copied_node = Node(current_node.val)
            visited_dict[current_node] = copied_node # mark as visited and set copy for mapping
            copied_node.neighbors = [dfs(next_node) for next_node in current_node.neighbors]
            return copied_node

        return dfs(node)
            


