
with 
-- Defining false negatives as transactions NOT flagged as fraud (scored too low) that were later disputed
false_negatives as (
    select 
        count(*) as count_false_negatives
    from fraud1
    where "Flagged As Fraud" = 'No' 
    and "Chargeback (Yes/No)" = 'Yes'
),

-- Defining false positives as transactions flagged as fraud that are manually approved
-- and not later disputed 
false_positives as (
    select 
        count(*) as count_false_positives
    from fraud1
    where "Flagged As Fraud" = 'Yes' 
    and "Chargeback (Yes/No)" = 'No'
    and "Result" = 'Approved'
)

select 
    fn.count_false_negatives, 
    fp.count_false_positives
from false_negatives fn
cross join false_positives fp;