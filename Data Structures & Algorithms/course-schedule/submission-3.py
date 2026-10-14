class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        [a, b] means you need to take b first to take course a

        so basically: the prereq of a is b
        so basically: a requires b


        ok so i need to figure out if i can do all courses or not

        so im given a graph and i need to know if it is disjoint or not?

        can i use a dsu here?

        issue is i kinda dont know how to make a dsu

        no  idk if dsu is correct here

        for example in example 2

        course 1 requires course 0

        course 0 requires course 1

        a dsu does not care about this sort of relation i dont think it cares about these sorts of loops

        itd be useless there


        assume i traverse the graph in whatever way.

        if theres a cycle, then its impossible:
            - how to detect cycle?

        if something is disjoint, then its impossible
            - what does that look like?

        well lets think about the disjoint portion a bit more

        we get given a number of courses

        if a course is not said to have a prereq, then it means theres no prereq
        however, if somehow a course's prereq >= numCourses, then that means its disjoint


        ok we got the disjoint quesiton solved, if at any point prereq >= numCourses, we return false

        we still need to figure out how to detect cycles and then how to traverse the graph

        lets take a small example

        example 2:

        0 requires 1

        then we're asking ourselves, does 1 require anything?

        well it does, it requires 0.

        to detect cycles, i believe we need to maintain a visited set

        and then to quickly know which prereq every course requires, lets convert prerequisites into a dictionary

        this is what i will do first

        prereq_dict: dict[int, int] where the key is the course we wanna take and the value is the prereq

        something i failed to take into account (and i should always ask this in an interview): can the dict support multiple items?
        """


        prereq_dict: dict[int, set[int]] = defaultdict(set)
        completed: set[int] = set()
        for key, val in prerequisites:
            prereq_dict[key].add(val)

        def can_take_course(course: int, visited: set[int]) -> bool:
            if course in completed:
                return True

            if course in visited:
                print("cycle counting issue?", course, visited)
                return False
            
            if course in prereq_dict:
                new_courses_to_check = prereq_dict[course]
                for new_course in new_courses_to_check:
                    visited.add(course)
                    if not can_take_course(new_course, visited):
                        return False
                    visited.remove(course) # silly backtracking

            completed.add(course)

            return True

        print(prereq_dict)

        for course in prereq_dict:
            if not can_take_course(course, set()):
                return False

        return True