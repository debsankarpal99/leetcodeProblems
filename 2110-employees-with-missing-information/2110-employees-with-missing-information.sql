select s.employee_id from employees as e full join salaries as s 
on e.employee_id = s.employee_id
where e.name is null 

union

select e.employee_id from employees as e full join salaries as s 
on e.employee_id = s.employee_id
where s.salary is null ;