class Employee(object):
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees, id):
        """

        :type employees: Employee
        :type id:int
        :rtype: int
        """
        ret = 0
        temp_map = dict()
        for employee in employees:
            temp_map[employee.id] = employee
        subs = [id]
        for sub in subs:
            ret += temp_map.get(sub).importance
            subs.extend(temp_map.get(sub).subordinates)
        return ret


def main():
    solution = Solution()
    employees = [Employee(1, 5, [2,3]), Employee(2, 3, []), Employee(3,3,[])]
    ret = solution.getImportance(employees, 1)
    print(ret)


if __name__ == '__main__':
    main()
