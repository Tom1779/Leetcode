select distinct p1.email
from person as p1, person as p2
where p1.id != p2.id and p1.email = p2.email