select u.name, sum(t.amount) as balance from users as u join transactions as t  on u.account = t.account

group by u.name
having balance > 10000
