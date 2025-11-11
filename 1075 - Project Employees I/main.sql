SELECT project_id, ROUND(AVG(experience_years),2) as average_years
FROM Project
Inner Join 
Employee
ON Project.employee_id = Employee.employee_id
Group BY (project_id)