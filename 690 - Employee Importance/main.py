from typing import List

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


def add_importance(employee, e, importance):
    if not employee:
        return
    importance[0] += employee.importance
    for s in employee.subordinates:
        add_importance(e.get(s), e, importance)


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importance = [0]
        e = {employee.id: employee for employee in employees}
        add_importance(e.get(id), e, importance)
        return importance[0]