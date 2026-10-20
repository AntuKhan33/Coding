

#59
select * from emp where  job in ("MANAGER","ANALYST") and sal between 3000 and 5000 and comm is null;
#60

select e.empno,e.ename,e.deptno,e.sal,d.loc from emp e ,dept d where e.deptno=d.deptno 
and loc in ("Dallas","Chicago") 
and timestampdiff(month,hiredate,curdate())>10;

#61
select  e.empno,ename,e.deptno,e.sal,d.loc from emp e ,dept d 
where sal between 2000 and 5000 and loc in ("DALLAS");

#62

#63

select * from  emp e ,emp m where e.mgr=m.empno and e.hiredate<m.hiredate;

#64

#66
select * from emp order by	sal asc;

#67
select * from emp order by empno asc,deptno desc;

#68
select * from emp order by job desc;
#69
select *,sal/30 as daily_sal,sal*12 as annaul_sal from emp order by annaul_sal asc;

SELECT deptno, AVG(sal)
FROM emp
GROUP BY deptno;

#70
select *  from emp where job in ("Clerk","Analyst") order by job asc;

#71
select * from emp e ,dept d where e.ename="Scott" and  e.deptno=d.deptno;

#72
select * from emp where  hiredate in ('1991-05-01', '1991-12-03', '1990-01-19');
#73
select * from emp where sal<1000 order by sal asc ;
#74
select * from emp  order by sal asc ;
#75
select * from emp  order by job asc,empno desc ;
#76
select distinct job from emp where deptno in ("20","30")  order by job;
select job from emp where deptno in ("20","30") group by job;
#77
select * from emp 
 where job not in("president","manager")
 order by sal asc;
 #78
SELECT
    ename,
    sal * 12 AS annual_sal
FROM
    emp
WHERE
    sal * 12 < 25000
ORDER BY  
    annual_sal ASC;
#79

select *,sal*12 as annual_sal from emp where job ="salesman"  order by annual_sal;
#80

#81
select * from emp where (hiredate)>'1981-06-30' order by job asc;
#82

#83

#84
#85
#88
select * from emp where hiredate< '1981-05-01';
#89

select * from emp where deptno=20 order by sal asc;
#90
select max(sal)  as max_sal from emp;
#91
select  job,avg(sal),avg(sal+comm)  from emp group by job;
#92
select job,sal*12 as sum from emp;
#93
#96
select mgr,count(*) from emp group by mgr;
#98
select deptno,count(*) from emp group by deptno having count(*)>2;
#102

select d.deptno,count(*) from emp e ,dept d 
where e.deptno=d.deptno 
group by d.deptno
having count(*)>2;
#103
select ename ,count(*) from emp group by ename;
#------------104
select count(*),avg(sal),deptno,job from emp group by deptno,job;

#105 
select ename from emp where length(ename)=6  and ename like "M%";

#107
select ename from emp where length(ename)=6 and ename like "M%N";
#108
select ename from emp where month(hiredate) like "__r%";
#109
select ename from emp where ename like "%mi%";
#110
select * from emp where year(hiredate)=1981;
#111
select * from emp where empno not like "75%";
#112
select * from emp where ename  like "%a%";
#114
SELECT *
FROM emp
WHERE UPPER(MONTHNAME(hiredate)) LIKE '%s%';
#115
SELECT *
FROM emp
WHERE UPPER(MONTHNAME(hiredate)) LIKE '_p%';