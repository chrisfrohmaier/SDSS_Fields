SDSS_Fields
===========

The Field Selection for the Rate Calculation

##The Query

```
select subtraction.ptffield, count(*) from subtraction,ptffield where ((ujd>2455331 and ujd<2455512) or (ujd>2455696 and ujd<2455879)) and is_sdss='t' and color_excess<0.06 and subtraction.ptffield=ptffield.id and ptffield.is_sdss='t' and filter='R' group by subtraction.ptffield order by count(*) desc;
```