class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        dic = {
            "student1":0,
            "student0":0,
            "sandwiche1":0,
            "sandwiche0":0,
        }
        for x in range(len(students)):
            dic[f"student{students[x]}"] +=1
            dic[f"sandwiche{sandwiches[x]}"] +=1

        for x in sandwiches:
            if dic[f"student{x}"] > 0:
                dic[f"student{x}"] -= 1
            else:
                break

        return(dic[f"student0"] + dic[f"student1"])