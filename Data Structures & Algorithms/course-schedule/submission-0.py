from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prereq_to_courses = defaultdict(set)
        course_to_prereqs = defaultdict(set)
        q = deque()

        for a,b in prerequisites:
            # this means b -> a, b is needed before a
            prereq_to_courses[b].add(a)
            course_to_prereqs[a].add(b)

        courses_completed = 0

        for course in range(numCourses):
            if len(course_to_prereqs[course]) == 0:
                q.append(course)
        # q can only have courses with no prereqs left
        while q:
            course = q.popleft()
            courses_completed += 1

            for future_course in prereq_to_courses[course]:
                course_to_prereqs[future_course].remove(course)
                if len(course_to_prereqs[future_course]) == 0:
                    q.append(future_course)

        return courses_completed == numCourses



        


