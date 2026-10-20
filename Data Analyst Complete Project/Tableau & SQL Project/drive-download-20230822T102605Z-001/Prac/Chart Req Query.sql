
select * from pizza_sales;
--1
select DATEPART(hour,order_time) as order_hour,sum(quantity) as Total_Pizzas_Sold
from pizza_sales
group by  DATEPART(hour,order_time)
order by DATEPART(hour,order_time)
--2

select DATEPART(ISO_WEEK,order_date) as Week_Number, YEAR(order_date) as Order_Year,
COUNT(distinct( order_id)) as Total_Orders
from pizza_sales
group by DATEPART(ISO_WEEK,order_date),YEAR(order_date)
order by DATEPART(ISO_WEEK,order_date),YEAR(order_date)

--3
select pizza_category,SUM(total_price)as total_sales, sum(total_price)*100/
(select sum(total_price) from pizza_sales) as PCT_total_sales
from pizza_sales
group by pizza_category 

--3 per month
select pizza_category,SUM(total_price)as total_sales, sum(total_price)*100/
(select sum(total_price) from pizza_sales where MONTH(order_date)=1) as PCT_total_sales

from pizza_sales
where MONTH(order_date)=1
group by pizza_category 


--4

select pizza_size,SUM(total_price)as total_sales, sum(total_price)*100/
(select sum(total_price) from pizza_sales) as PCT_total_sales

from pizza_sales

group by pizza_size 
order by PCT_total_sales DEsc

--5