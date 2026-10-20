#1
select * from emp;

#2
select sal from emp;
#3
select distinct job from emp;
#4
select ename, concat("$",sal *1.15) as salary from emp;
#5
SELECT concat(ename,"   ", job ) AS "Employee   Job"
FROM emp ;
#6
SELECT concat(ename,"(", job,")" ) AS "Employee" 
FROM emp ;
#7
select empno,ename,sal,DATE_FORMAT(hiredate, '%M/%d/%Y') as formatted_hire_date from emp;
#8
select length(trim(ename)) as length from emp;
#9
select empno,sal,comm    from emp;

#10
select   distinct deptno,job  from emp;
#11

select * from emp where deptno not in (20);

#12
select * from emp where hiredate>1991-1-1;

#13
select avg(sal) from emp where job='ANALYST';
#14
select * from emp where ename= "allen";
#15
select * from emp where comm>sal;
#16
select *  from emp where sal*1.25>3000 ;

#17
select ename from emp where length(ename) =6;

#18
select * from emp where  month(hiredate)=1;

#------------------19

select concat(e.ename," works for ",m.ename ) as work 
from emp e ,emp m where e.mgr=m.empno;

select concat(e.ename,"  works for ",m.ename) as work 
from emp e,emp m where e.empno=m.mgr;

#20
select * from emp where job='clerk';

#21
select * from emp where datediff(curdate(),hiredate)>27*365;
#22
select * from emp where sal<3500 ;

#23
select * from emp where job="clerk";
#24

select * from emp where  year(hiredate)=1980;

#25
select * from emp where hiredate>1991-1-1;

#---------------26


select * from emp where mgr is null;
#27
select * from emp where hiredate=1991-1-1;

#28
select * from emp where  mgr=7902;

#29
select * from emp where sal/30>100;
#30
select * from emp where hiredate>31-12-99;


#31
select * from emp where sal%2 = (1);
#32

select * from emp where length(sal)=6;
#33
select * from emp where month(hiredate)=4;
#34
select * from emp where day(hiredate)<19;

#35
select * from emp where job="salesman" and timestampdiff(month,hiredate,curdate())>10;
#36
select * from emp where deptno=30 and year(hiredate)=1981;
#37
select * from emp where deptno  =30;
#38
select * from emp where job="clerk" and deptno=30;
#39
 
select * from emp where comm<sal and comm<34000;

select * from emp where job ="salesman" and deptno="30";

#40
select * from emp where  job in ("clerk" ,'manager');
select * from emp where job= 'clerk'  or job ='manager';
#41
select * from emp  where month(hiredate) != "2";
#42
select * from emp  where year(hiredate) = "1981";
select * from emp where hiredate between "1981-01-01" and "1981-12-12"; 
#43
SELECT *
FROM emp
WHERE hiredate = '1981-02-20';
select * from  emp where date_format(hiredate,"%Y-%m")="1981-02";
#44
select * from emp where sal between "2000" and "5000";
#45
select * from emp where hiredate="1981-02-20" or hiredate="1991-03-12";

#46

select * from emp where mgr in ("7902","7698");

#47
select * from emp where date_format(hiredate,"%Y-%m")>"1981-06";

select * from emp where hiredate between "1981-12-15" and curdate();

#48
select	 * from emp where year(hiredate)="1981";

#49
#50
#51
select	* from emp where year(hiredate) !=1991;
#52
select * from emp e ,dept d where e.deptno=d.deptno;
#53

select e.empno,e.job,e.sal*12 as annual_sal,d.deptno,d.dname,d.loc     from emp e, dept d where e.deptno=d.deptno and job!="analyst";

#54

#55
select * from  emp e ,dept d where e.deptno=d.deptno  and sal between 2000 and 5000 and d.loc="Dallas";

#56

#--------------57

select * from emp e,emp d where e.mgr=d.empno and d.ename="Smith"