SELECT d.name as Department, e.name as Employee , e.salary as Salary
from employee as e join department as d 
 on e.departmentID = d.id
 where (e.departmentid , e.salary) in (
   select departmentid, max(salary) from employee
   group by departmentid
 )

