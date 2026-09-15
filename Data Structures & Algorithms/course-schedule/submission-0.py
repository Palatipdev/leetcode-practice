class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Plan: pop the first element, then check dfs, by searching for other element in the list the find whether the prerequisite of the first element also in some current[0] then search for that prerequisite 
        # recurse until:
            # a prerequisite is also has a prerequisite for that element
            # case one doesn't hold and we can't find anymore prerequisite in our dfs, then push all values it to our valid queue, increment courseTaken


        # dfs with cycle detection

        courseTaken = 0
        adj = defaultdict(list) # for O(1) lookup pre req
        for a, b in prerequisites:
            adj[a].append(b)
            
        done = set()
        current = set()
        def dfs(course):
            if course in current:
                return False
            if course in done:
                return True
            current.add(course)
            for a in adj[course]:
                if not dfs(a):
                    return False
            done.add(course)
            current.remove(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
