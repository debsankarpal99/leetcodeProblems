select p.firstName, p.lastName, a.city, a.state from Person as p full join address as a on p.personid = a.personid
where p.personid is not null