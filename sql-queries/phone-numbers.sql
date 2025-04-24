select 
    "phone number", 
    count(distinct user_id) as number_of_associated_accounts
from fraud2
group by "phone number"
having count(distinct user_id) > 1
order by number_of_associated_accounts desc