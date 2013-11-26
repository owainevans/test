



















from numpy import *
from venture.shortcuts import *
v=make_church_prime_ripl()




v.set_seed(1995)
v.assume('t','(lambda (mu var nu) ( (lambda () (normal mu (rt_inv (gamma (* .5 nu) (* var .5 nu)) )) ) ) )') 
v.assume('rt_inv','(lambda (x) (power (/ 1.0 x) 0.5) ) ') 
v.assume('sq','(lambda (x) (power x 2.0))') 
v.assume('get_dm_j','(mem (lambda (j) (make_dir_mult 105 1 1) ) ) ') 
v.assume('get_d_type','(mem (lambda (c j) ((get_dm_j j)) )) ') 
v.assume('alpha','(uniform_continuous 1 2.5)') 







v.assume('cluster_crp','(make_crp alpha)') 
v.assume('get_z','(mem (lambda (i) (cluster_crp) ) ) ') 
v.assume('mu_loc','10') 
v.assume('mu_scale','10') 
v.assume('sigma_scale','.5') 
v.assume('get_mu','(mem (lambda (c j) (normal mu_loc mu_scale)))') 










v.assume('get_sigma','(mem (lambda (c j) (gamma 1 sigma_scale)))') 
v.assume('get_nu','(mem (lambda (c j) (gamma 3 1)))') 
v.assume('noise','(gamma 1 4)') 
v.assume('get_gen','(mem (lambda (c j) ( (lambda (d_type mu sigma nu) (if (= d_type 0) (lambda () (normal mu sigma) ) (if (= d_type 1) (lambda () (t mu (power sigma 2) nu) ) (lambda () (normal (uniform_continuous (- mu (* 2 sigma)) (+ mu (* 2 sigma))) noise ) ) )) ) (get_d_type c j) (get_mu c j) (get_sigma c j) (get_nu c j) ) ) ) ') 
v.assume('get_x','(mem (lambda (i j) ( (get_gen (get_z i) j ) )))') 

n,d=10,2
# test
v.predict('(get_x 1 1)','x11') 
v.report('x11')

x=normal(0,1,(100,2))
[v.observe('(get_x '+str(i[0])+' '+ str(i[1])+')') for i in x]
   
