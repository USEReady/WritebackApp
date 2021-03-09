'''
insert into public."Forecast"
SELECT
"Row ID", "Order Date", "Ship Date", "Customer ID", "Customer Name", "Category", "Sales", "Profit", 0
FROM public."Sales";

SELECT * from public."Forecast"
where
"Order Date" > '01-01-2020' and "Profit" > 50;

SELECT
count(1)
from public.
"Forecast"
where
"Order Date" > '01-01-2020'
-- and "Profit" > 10
-- and "Customer Name" = 'Chris Selesnick';

SELECT
distinct
"Customer Name"
from public.
"Forecast"
where
"Order Date" > '01-01-2020'
and "Profit" > 50
order
by
"Customer Name";

delete
from public.
"Forecast"
where
"Order Date" > '01-01-2020'
and "Profit" < 10

SELECT
count(1), "Customer Name"
from public.
"Forecast"
where
"Order Date" > '01-01-2020'
and "Profit" > 10
group
by
"Customer Name"
having
count(1) > 6
order
by
"Customer Name"

update public."Sales"
set "Category" = 'Upfront' where "Category" = 'Furniture'

update public."Sales"
set "Category" = 'Software Rental' where "Category" = 'Office Supplies'

update public."Sales"
set "Category" = 'Prof Svcs' where "Category" = 'Technology'

update public."Forecast"
set "Category" = 'Upfront' where "Category" = 'Furniture'

update public."Forecast"
set "Category" = 'Software Rental' where "Category" = 'Office Supplies'

update public."Forecast"
set "Category" = 'Prof Svcs' where "Category" = 'Technology'


'''