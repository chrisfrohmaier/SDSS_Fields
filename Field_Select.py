import numpy as np
import psycopg2

f=open('Final_Fields.dat','w')

ptffield=np.loadtxt('Good_Fields.dat', delimiter='|', skiprows=2, usecols=(0,), unpack=True)
#print ptffield

con = psycopg2.connect(host='scidb2.nersc.gov', user='subptf', password='p33d$kyy', database='subptf')
cur = con.cursor()


## The Query
#select ujd,seeing_new,ub1_zp_new,lmt_mg_new,ccdid,good_pix_area,ra_ul,dec_ul,ra_ur,dec_ur,ra_lr,dec_lr,ra_ll,dec_ll from subtraction where ptffield=100019 and filter='R';

for field in ptffield:
	fld=int(field)
	cur.execute("SELECT DISTINCT ON (ujd) ujd,seeing_new,ub1_zp_new,lmt_mg_new from subtraction where ptffield=%s and seeing_new<3.5 and lmt_mg_new>20 and filter='R'", (int(fld),))
	m=cur.fetchall()
	if len(m)>0:
		#print m
		dates=[]
		dates.append(m[0][0])
		counter=0
		for ln in m:
			ujd=float(ln[0])
			if ujd-dates[-1]>=0.5:
				counter+=1
				dates.append(ujd)
			if counter>=10:
				f.write(str(fld)+'\n')
				break
