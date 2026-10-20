
select * from  pizza_sales;
--1
select SUM(total_price) as TotalRevenue,SUM(unit_price)  as Unitprice from pizza_sales;
--2
select SUM(total_price)/count(distinct order_id) as Average_Order_Value from pizza_sales;
--3

select  sum(quantity) as Total_Pizza_Sold from pizza_sales;

--4
select count(distinct(order_id)) as Total_Orders from pizza_sales;
--5

select CAST(cast(sum(quantity) as decimal(10,2))/cast(count(distinct order_id) as decimal (10,2)) as decimal (10,2)) 
as AVG_Pizza_Per_Order from pizza_sales;