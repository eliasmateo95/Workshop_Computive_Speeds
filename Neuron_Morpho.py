from brian2 import *

eqs_IO_V = '''
Im = (-(I_l + I_Na + I_Ca_l + I_K_dr + I_h + I_K_s + I_Ca_h + I_K_Ca + I_c + I_K_a + I_Na_a)) : metre**-2*amp
I_c : metre**-2*amp
Iapp : amp (point current)
'''
eqs_IO_Ca = '''
dCa/dt = (-3*I_Ca_h*((uamp / cm**2)**-1)*mM - 0.075*Ca)/ms : mM
'''
eqs_IO_Isom = '''
I_l    = g_l*(v-V_l)              : metre**-2*amp
I_Na    = g_Na*m_inf**3*h*(v-V_Na)  : metre**-2*amp
I_Ca_l  = g_Ca_l*k*k*k*l*(v-V_Ca)   : metre**-2*amp
I_K_dr  = g_Kdr*n*n*n*n*(v-V_K)     : metre**-2*amp
I_h     = g_h*q*(v-V_h)             : metre**-2*amp
I_K_s   = g_K_s*(x_s**4)*(v-V_K)    : metre**-2*amp
'''
eqs_IO_Iden = '''
I_Ca_h  = g_Ca_h*r*r*(v-V_Ca)       : metre**-2*amp
I_K_Ca  = g_K_Ca*s*(v-V_K)          : metre**-2*amp
'''
eqs_IO_Iax = '''
I_K_a  = g_K_a *x_a**4*(v-V_K)      : metre**-2*amp
I_Na_a = g_Na_a*m_a**3*h_a*(v-V_Na) : metre**-2*amp
'''
eqs_IO_activation = '''
dh/dt = (h_inf - h)/tau_h : 1
dk/dt = (k_inf - k)/tau_k : 1
dl/dt = (l_inf - l)/tau_l : 1
dn/dt = (n_inf - n)/tau_n : 1
dq/dt = (q_inf - q)/tau_q : 1
dr/dt = (r_inf - r)/tau_r : 1
ds/dt = (s_inf - s)/tau_s : 1
m_a = m_inf_a : 1
dh_a/dt = (h_inf_a - h_a)/tau_h_a : 1
dx_a/dt = (x_inf_a - x_a)/tau_x_a : 1
dx_s/dt = (x_inf_s - x_s)/tau_x_s : 1
'''
eqs_IO_inf = '''
m_inf   = alpha_m /(alpha_m+beta_m)        : 1
h_inf   = alpha_h/(alpha_h+beta_h)         : 1
k_inf   = 1/(1+e**(-(v/mvolt+61)/4.2))    : 1
l_inf   = 1/(1+e**((v/mvolt+85.5)/8.5))   : 1
n_inf   = alpha_n/(alpha_n+beta_n)         : 1
q_inf   = 1/(1+e**((v/mvolt+75)/(5.5)))   : 1
r_inf   = alpha_r/(alpha_r + beta_r)       : 1
s_inf   = alpha_s/(alpha_s+beta_s)         : 1
m_inf_a = 1/(1+(e**((-30-v/mvolt)/ 5.5))) : 1
h_inf_a = 1/(1+(e**((-60-v/mvolt)/-5.8))) : 1
x_inf_a = alpha_x_a/(alpha_x_a+beta_x_a)   : 1
x_inf_s = alpha_x_s/(alpha_x_s + beta_x_s) : 1
'''
eqs_IO_tau = '''
tau_h   = 170*msecond/(alpha_h+beta_h)                                          : second
tau_k   = 5*msecond                                                             : second
tau_l   = 1*msecond*(35+(20*e**((v/mvolt+160)/30/(1+e**((v/mvolt+84)/7.3))))) : second
tau_n   = 5*msecond/(alpha_n+beta_n)                                            : second
tau_q   = 1*msecond/(e**((-0.086*v/mvolt-14.6))+e**((0.07*v/mvolt-1.87)))     : second
tau_r   = 5*msecond/(alpha_r + beta_r)                                          : second
tau_s   = 1*msecond/(alpha_s + beta_s)                                          : second
tau_h_a = 1.5*msecond*e**((-40-v/mvolt)/33)                                    : second
tau_x_a = 1*msecond/(alpha_x_a + beta_x_a)                                      : second
tau_x_s = 1*msecond/(alpha_x_s + beta_x_s)                                      : second
'''
eqs_IO_alpha = '''
alpha_m   = (0.1*(v/mvolt + 41))/(1-e**(-(v/mvolt+41)/10)) : 1
alpha_h   = 5.0*e**(-(v/mvolt+60)/15) : 1
alpha_n   = (v/mvolt + 41)/(1-e**(-(v/mvolt+41)/10)) : 1
alpha_r   = 1.7/(1+e**(-(v/mvolt - 5)/13.9)) : 1
alpha_s   = ((0.00002*Ca/mM)*int((0.00002*Ca/mM)<0.01) + 0.01*int((0.00002*Ca/mM)>=0.01)) : 1
alpha_x_a = 0.13*(v/mvolt + 25)/(1-e**(-(v/mvolt+25)/10)) : 1
alpha_x_s = 0.13*(v/mvolt + 25)/(1-e**(-(v/mvolt+25)/10)) : 1
'''

eqs_IO_beta = '''
beta_m = 9.0*e**(-(v/mvolt+60)/20)                        : 1
beta_h = (v/mvolt+50)/(1-e**(-(v/mvolt+50)/10))          : 1
beta_n = 12.5*e**(-(v/mvolt+51)/80)                       : 1
beta_r = 0.02*(v/mvolt + 8.5)/(e**((v/mvolt + 8.5)/5)-1) : 1
beta_s = 0.015                                             : 1
beta_x_a  = 1.69*e**(-0.0125*(v/mvolt + 35))              : 1
beta_x_s  = 1.69*e**(-0.0125*(v/mvolt+ 35))               : 1
'''

eqs_vector = '''
V_Na : volt
V_K  : volt
V_Ca : volt
V_l  : volt
V_h  : volt
g_Na   : siemens/meter**2
g_Kdr  : siemens/meter**2
g_Ca_l : siemens/meter**2
g_h    : siemens/meter**2
g_Ca_h : siemens/meter**2
g_K_Ca : siemens/meter**2
g_l : siemens/meter**2
g_Na_a   : siemens/meter**2
g_K_a   : siemens/meter**2
g_K_s   : siemens/meter**2
'''

eqs_IO = eqs_IO_beta
eqs_IO += eqs_IO_alpha
eqs_IO += eqs_IO_tau
eqs_IO += eqs_IO_inf
eqs_IO += eqs_IO_activation
eqs_IO += eqs_IO_Iax
eqs_IO += eqs_IO_Iden
eqs_IO += eqs_IO_Isom
eqs_IO += eqs_IO_Ca
eqs_IO += eqs_IO_V
eqs_IO += eqs_vector