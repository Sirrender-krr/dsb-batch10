/*Request 1
Can you find out the total milk production for 2023? 
Your manager wants this information for the yearly report.
What is the total milk production for 2023?*/
CREATE view final_project_01
as
select 
year,
sum(value) total_production
from milk_production
group by year
order by year desc
limit 6
-- 91812000000

/*Request 2
Which states had cheese production greater than 100 million in April 2023? 
The Cheese Department wants to focus their marketing efforts there. 
How many states are there?*/
CREATE view final_project_02
as
SELECT 
Value,
period,
state_ansi
FROM cheese_production
WHERE Year = 2023
and period = 'APR'
and value > 100000000
group by period, state_ansi;
-- 13

/*Request 3
Your manager wants to know how coffee production has changed over the years. 
Query a yearly comparison table and find out what is the total value of coffee production for 2011?*/

CREATE view final_project_03
as
select
year,
value
from coffee_production
where year >= 2011
group by year
order by year;
-- 7600000

/*Request 4
There's a meeting with the Honey Council next week. 
Query a yearly average comparison table of five years till 2022 and find the average honey production for 2022 so you're prepared.*/

CREATE view final_project_04
as
select
year,
avg(value)
from honey_production
where year between 2017 and 2022
group by year
order by year;
-- table

/*Request 5
5. The State Relations team wants a list of all states names with their corresponding ANSI codes. Can you generate that list? 
Query a list of the state that has not produced cheese. How many state did not produce cheese at all?*/

CREATE view final_project_05
as
select 
s.state,
s.state_ANSI,
c.value
from state_lookup s
left join cheese_production c
on s.State_ANSI = c.State_ANSI
where c.Value is null
group by s.state;
-- 14

/*Request 6
For a cross-commodity report, can you list all states with their cheese production values in April of 2023? 
What state product the most and how much?*/

CREATE view final_project_06
as
select
c.year,
c.period,
s.state,
sum(c.value) total
from cheese_production c, state_lookup s
where c.State_ANSI = s.State_ANSI
and year = 2023
and period = 'APR'
group by state, period
order by total desc;
-- WISCONSIN 289699000

/*Request 7
Can you find the state and the total yogurt production for states in the year 2022 which also have cheese production data from 2023?
This will help the Dairy Division in their planning.*/

CREATE view final_project_07
as
select
sum(y.value),
s.state
from yogurt_production y, state_lookup s
where y.year = 2022
and y.State_ANSI in (
  select 
  DISTINCT c.state_ansi
  from cheese_production c
  where c.year = 2023)
and y.State_ANSI = s.State_ANSI;
-- 1171095000 CALIFORNIA

/*Request 8
List all states from state_lookup that are missing from milk_production in 2023.
How many states are there?*/

CREATE view final_project_08
as
SELECT
count(*)
from(SELECT
s.state,
s.state_ansi
from state_lookup s
where s.state_ansi not in (
  select
  distinct m.state_ansi
  from milk_production m
  where year = 2023));
-- 26
  
/*Request 9
List all states with their cheese production values and yogurt production values, including states that didn't produce any cheese or yogurt in April 2023. 
Did IDAHO produce any cheese and any yogurt in April 2023?*/

CREATE view final_project_09
as
select
s.state,
c.period,
c.year,
c.value cheese_total,
y.value yogurt_total
from state_lookup s
left join cheese_production c on s.State_ANSI = c.State_ANSI
left join yogurt_production y on c.State_ANSI = y.State_ANSI
where c.year = 2023
and c.Period = 'APR'
group by s.state;
-- IDAHO pruduced cheese but did not produce yogurt in April 2023
