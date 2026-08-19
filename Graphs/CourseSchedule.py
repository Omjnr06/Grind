# There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.
# - For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.
# Return `true` if you can finish all courses. Otherwise, return `false`.

def courseSchedule(self,prerequisites,numCourses):
    adjList = {i: [] for i in range(numCourses)}

    for c,p in prerequisites:
        adjList[c].append(p)

    visiting = set()

    def dfs(course):
        if course in visiting:
            return False
        if adjList[course] == []:
            return True

        visiting.add(course)

        for prereq in adjList[course]:
            if not dfs(prereq):
                return False

        visiting.remove(course)
        adjList[course] = []
        return True

    for course in range(numCourses):
        if not dfs(course):
            return False

    return True