class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1]-x[0], reverse = True)

        cur_energy = tasks[0][1] - tasks[0][0]
        total_energy = tasks[0][1]
        for task in tasks[1:]:
            if cur_energy < task[1]:
                total_energy += task[1] - cur_energy
                cur_energy += task[1] - cur_energy

            cur_energy -= task[0]

        return total_energy