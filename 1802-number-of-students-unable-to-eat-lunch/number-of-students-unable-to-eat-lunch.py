class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)

        for i in range(len(sandwiches)):
            count = 0
            while students[0] !=  sandwiches[i] and count <= len(students):
                p = students.popleft()
                students.append(p)
                count += 1

            if students[0] != sandwiches[i]:
                break;
            elif students[0] == sandwiches[i]:
                students.popleft()
        
        return len(students)
