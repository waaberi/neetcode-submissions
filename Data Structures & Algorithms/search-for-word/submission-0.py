class Solution:
    """
    9:30
    my state will be a set[tuple[int, int]] where the ints are i and j
    issue: this does not represent the order.
    i could have an array to maintain the order
    actually, an array would be fine
    i was thinking of doing a set so i can do a membership check quickly
    but for backtracking purposes i need to know in order what was inserted and an array/stack is superior for that
    thereore, i will be using BOTH set[tuple[int, int]] AND list[tuple[int, int]]

    - is_valid_state (gets us to an answer)
    - get_candidates (selects next states to explore)
    - search (our backtracking function, return a boolean that we will use in exist)
    - solve (exist)


    FOR MY EYES ONLY: NEED TO STUDY TIME COMPLEXITY OF DFS/BFS MORE

    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0]) # assert len(board) >= 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        visited_set: set[tuple[int, int]] = set()
        word_state: list[tuple[int, int]] = []

        def is_valid_state() -> bool:
            # simply returns true if word_state's length is word's length
            # we can do this because get_candidates does the filtering
            return len(word_state) == len(word)
        
        def get_candidates() -> list[tuple[int, int]]:
            # returns list of all valid adjacent idxs
            # THIS DOES THE FILTERING, NOT IS_VALID_STATE
            answers = []
            state_length = len(word_state)
            if state_length == 0:
                return [(i, j) for i in range(m) for j in range(n) if board[i][j] == word[0]]


            last_i, last_j = word_state[-1]
            for i, j in directions:
                new_i, new_j = last_i + i, last_j + j
                if not 0 <= new_i < m:
                    continue
                if not 0 <= new_j < n:
                    continue
                if board[new_i][new_j] == word[state_length] and (new_i, new_j) not in visited_set:
                    answers.append((new_i, new_j))

            return answers

        def search() -> bool:
            if is_valid_state():
                return True

            for candidate in get_candidates():
                # take
                word_state.append(candidate)
                visited_set.add(candidate)
                # recurse
                is_valid = search()
                if is_valid:
                    return True
                # drop
                visited_set.remove(candidate)
                word_state.pop()

            return False # everything exhausted

        return search()