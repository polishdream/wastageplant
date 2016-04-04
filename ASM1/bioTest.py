import pickle
import math
import datetime
import time
import os
import database as db
import settler as stlr

class Params(object):
	def __init__(self):
		self.tp = 20/(24.0*3600.0) #sekundy, czas probkowania
		self.tsim = db.selectLast('params','tsim') # czas symulacji w dniach
		self.iter = int(self.tsim/self.tp)
		self.progres = int(self.iter*0.05)

		#BIOREACTOR
		self.q_in= db.selectLast('params','qin') * self.tp #m3/iteracje
		self.q_ir = db.selectLast('params','qir') * self.q_in #sprzezenie zwrotne wewnetrzne
		self.q_r = db.selectLast('params','qr') * self.q_in #sprzezenie zwrotne zewetrzne
		self.q = self.q_in + self.q_ir + self.q_r
		self.so_sat = db.selectLast('params','sosat')
		self.kla3 = db.selectLast('params','kla3')
		self.kla4 = db.selectLast('params','kla4')
		self.kla5 = db.selectLast('params','kla5')

		#SETTLER
		self.q_f = self.q - self.q_ir
		self.q_e = db.selectLast('params','qe')*self.q_in
		self.q_u = self.q_f - self.q_e
		self.q_w = db.selectLast('params','qw')*self.q_in
		self.nr_layers = 10	#ilosc warstw
		self.A = 1500.0 #powierzchnia m2
		self.V = 6000.0 #objetosc m3
		self.h_f = 0.4
		self.X = [0.0] * 10 
		self.dX = [0.0] * 10
		self.X_f = 0.0
		self.X_e = 12.5
		self.X_u = 6394.0
		self.settlerPar = [250.0*self.tp,474.0*self.tp, 0.0005760, 0.00286, 0.00228, 3000.0] #parametry osadnika: v'o,vo, rh, rp, fns, xt		

		self.xTab = []
		self.yTab = []
		self.step = 300 #co ile wartosci pobiera dana do wykresu i aktualizuje go [s]
		self.kompTab = ['C1','C2','C3','C4','C5', 'settler']
		self.fracTab = ['so','sno','snd','snh','ss','si','xh','xa','xs','xnd','xp','xi']

		#parametry do sterowania praca programu
		self.start = db.selectLast('flags','start')
		self.stop = db.selectLast('flags','stop')
		self.updateFlag = db.selectLast('flags','start')
	
	def updateParams(self):
                self.tp = db.selectLast('params','tp')/(24.0*3600.0) #sekundy, czas probkowania
                self.q_in= db.selectLast('params','qin') * self.tp #m3/iteracje
                self.q_ir = db.selectLast('params','qir') * self.q_in #sprzezenie zwrotne wewnetrzne
                self.q_r = db.selectLast('params','qr') * self.q_in #sprzezenie zwrotne zewetrzne
		self.q = self.q_in + self.q_ir + self.q_r
                self.so_sat = db.selectLast('params','sosat')
                self.tsim = db.selectLast('params','tsim') # czas symulacji w dniach
                self.iter = int(self.tsim/self.tp)
                self.kla = db.selectLast('params','kla')

                #parametry do sterowania praca programu
                self.start = db.selectLast('flags','start')
                self.stop= db.selectLast('flags','stop')
                self.updateValues = db.selectLast('flags','refresh')

class Kompartment(Params):	#C
	def __init__(self,params,so,sno,snd,snh,ss,si,xh,xa,xs,xnd,xp,xi,vol=0.0,kla=0.0):
		self.s_o = so	#0
		self.s_no = sno	#1
		self.s_nd = snd	#2
		self.s_nh = snh	#3
		self.s_s = ss	#4
		self.s_i = si	#5
		self.x_h = xh	#6
		self.x_a = xa	#7
		self.x_s = xs	#8
		self.x_nd = xnd	#9
		self.x_p = xp	#10
		self.x_i = xi	#11
		
		self.v = vol
		self.k_la = kla*params.tp
	
	def przepisz(self,Cnew): #n - argument opcjonalny, wsppolczynnik potrzebny np w Cr (cf) 
                self.s_o = Cnew.s_o   #0
                self.s_no = Cnew.s_no #1
                self.s_nd = Cnew.s_nd #2
                self.s_nh = Cnew.s_nh #3
                self.s_s = Cnew.s_s   #4
                self.s_i = Cnew.s_i   #5
                self.x_h = Cnew.x_h   #6
                self.x_a = Cnew.x_a   #7
                self.x_s = Cnew.x_s   #8
                self.x_nd = Cnew.x_nd #9
                self.x_p = Cnew.x_p   #10
                self.x_i = Cnew.x_i   #11

	def stworzRekord(self,par): #par - obiekt klasy params
		self.ts = datetime.datetime.now().replace(microsecond=0)
		r = (self.ts,par.q_in,par.q_ir,par.q_r,self.k_la,self.s_o,self.s_no,self.s_nd,self.s_nh,self.s_s,self.s_i,self.x_h,self.x_a,self.x_s,self.x_nd,self.x_p,self.x_i)
		return r

class Ro(Params):	#kinetyczne
	def __init__(self,params): #zmienic na parametry opcjonalne!
		self.mi_h = 4.0*params.tp 	#0
		self.b_h = 0.3*params.tp 	#1
		self.k_h = 3.0*params.tp	#2
		self.mi_a = 0.5*params.tp	#3
		self.b_a = 0.05*params.tp	#4
		self.k_a = 0.05*params.tp	#5
		self.k_s = 10.0			#6
		self.k_oh = 0.2			#7
		self.k_no = 0.5			#8
		self.n_g = 0.8			#9
		self.n_h = 0.8			#10
		self.k_x = 0.1			#11
		self.k_nh = 1.0			#12
		self.k_oa = 0.4			#13

	def obliczRo(self, komp):
                self.ro1 = self.mi_h * (komp.s_s / (self.k_s + komp.s_s)) * (komp.s_o / (self.k_oh + komp.s_o)) * komp.x_h
                self.ro2 = self.mi_h * (komp.s_s/(self.k_s + komp.s_s))*(self.k_oh / (self.k_oh + komp.s_o))*(komp.s_no / (komp.s_no+self.k_no)) * self.n_g * komp.x_h
                self.ro3 = self.mi_a*(komp.s_nh/(komp.s_nh+self.k_nh))*(komp.s_o/(komp.s_o+self.k_oa))*komp.x_a
                self.ro4 = self.b_h * komp.x_h
                self.ro5 = self.b_a * komp.x_a
                self.ro6 = self.k_a * komp.s_nd * komp.x_h
                self.ro7 = self.k_h*((komp.x_s/komp.x_h)/(self.k_x+(komp.x_s/komp.x_h)))*((komp.s_o/(komp.s_o+self.k_oh))+self.n_h*(self.k_oh/(self.k_oh+komp.s_o))*(komp.s_no/(komp.s_no+self.k_no)))*komp.x_h
                self.ro8 = self.k_h*((komp.x_s/komp.x_h)/(self.k_x+(komp.x_s/komp.x_h)))*((komp.s_o/(komp.s_o+self.k_oh))+self.n_h*(self.k_oh/(self.k_oh+komp.s_o))*(komp.s_no/(komp.s_no+self.k_no)))*komp.x_h*(komp.x_nd/komp.x_s)
	
	def wyswietl(self):
		print self.mi_h, self.b_h, self.k_h, self.mi_a, self.b_a, self.k_oa

	def wyswietlRo(self):
		print self.ro1, self.ro2, self.ro3, self.ro4, self.ro5, self.ro6, self.ro7, self.ro8

class R(Params):	#stechiometryczne
	def __init__(self,ya=0.24,yh=0.67,fp=0.08,ixb=0.08,ixp=0.06):
		self.y_a = ya		#0
		self.y_h = yh		#1
		self.f_p = fp		#2
		self.i_xb = ixb		#3
		self.i_xp = ixp		#4

	def obliczR(self, ro):
		self.r_so = -((1-self.y_h) / self.y_h) * ro.ro1 - ((4.57 - self.y_a) / self.y_a) * ro.ro3
		self.r_sno = -((1 - self.y_h) / (2.86*self.y_h)) * ro.ro2 + (1 / self.y_a) * ro.ro3
		self.r_snd = -ro.ro6 + ro.ro8
		self.r_snh = -self.i_xb * ro.ro1 - self.i_xb * ro.ro2 - (self.i_xb + (1/self.y_a)) * ro.ro3 + ro.ro6
		self.r_ss = -(1/self.y_h) * ro.ro1 - (1 / self.y_h) * ro.ro2 + ro.ro7
		self.r_si = 0.0
		self.r_xh = ro.ro1 + ro.ro2 - ro.ro4
		self.r_xa = ro.ro3 - ro.ro5
		self.r_xs = (1-self.f_p) * ro.ro4 + (1-self.f_p) * ro.ro5 - ro.ro7
		self.r_xnd = (self.i_xb - self.f_p*self.i_xp) * ro.ro4 + (self.i_xb - self.f_p * self.i_xp) * ro.ro5 - ro.ro8
		self.r_xp = self.f_p * ro.ro4 + self.f_p * ro.ro5
		self.r_xi = 0.0

	def wyswietlR(self):
		print self.r_so, self.r_sno, self.r_snd, self.r_snh, self.r_ss,self.r_si, self.r_xh, self.r_xa, self.r_xs, self.r_xnd, self.r_xp, self.r_xi


	
#==================================================================================== MAIN =======================================================================================
#parametry, ktore nie moga sie znajdowac w params
m = 0.0 #ograniczenie wartosci (funkcja max)
path = '/var/www/demo/baza.db' #sciezka do bazy danych
db.connect(path) #polaczenie z baza
sym = open('/var/www/demo/ASM1/symulacje.txt', 'a')
sym.write('Rozpoczynam dzialanie. start = ' + str(start) + ' ' +  str(datetime.datetime.now()) + '\n')

licz = 0 #licznik zapisanych rekordow
os.remove('/var/www/demo/ASM1/progres.txt')
params = Params()

#wyczyszczenie bazy danych
db.clearDb()
# ASM1
C1 = Kompartment(params,0.0,5.37,1.22,7.92,2.81,30.0,2552.0,148.0,82.1,5.28,449.0,1149.0,vol=1000.0)
C2 = Kompartment(params,0.0,3.66,0.882,8.34,1.46,30.0,2553.0,148.0,76.4,5.03,450.0,1149.0,vol=1000.0)
C3 = Kompartment(params,1.72,6.54,0.829,5.55,1.15,30.0,2557.0,149.0,64.9,4.39,45.0,1149.0,vol=1333.0,kla=params.kla3) #ostatnie parametry K_la, vol opcjonalne - domysln$
C4 = Kompartment(params,2.43,9.30,0.767,2.97,0.995,30.0,2559.0,150.0,55.7,3.88,451.0,1149.0,vol=1333.0,kla=params.kla4)
C5 = Kompartment(params,0.491,10.4,0.688,1.73,0.889,30.0,2559.0,150.0,49.3,3.53,452.0,1149.0,vol=1333.0,kla=params.kla5)

C1_new = Kompartment(params,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)
C2_new = Kompartment(params,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)
C3_new = Kompartment(params,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)
C4_new = Kompartment(params,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)
C5_new = Kompartment(params,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)

C_in = Kompartment(params,0.0,0.0,6.95,31.56,69.5,30.00,28.17,0.0,202.32,10.59,0.0,51.20)
C_ir = Kompartment(params,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)
C_ir.przepisz(C5)

#settler
C_u = Kompartment(params,0.491,10.4,0.688,1.73,0.889,30.0,5005.0,293.0,96.4,6.90,884.0,2247.0)
C_r = Kompartment(params,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)
C_r.przepisz(C_u)
C_e = Kompartment(params,0.491,10.4,0.688,1.73,0.889,30.0,9.78,0.573,0.188,0.0135,1.73,4.39)

Ro1 = Ro(params)
Ro2 = Ro(params)
Ro3 = Ro(params)
Ro4 = Ro(params)
Ro5 = Ro(params)

R1 = R()
R2 = R()
R3 = R()
R4 = R()
R5 = R()

#POZOSTALE PARAMETRY
sym.write(str(params.iter) + '\n')
sym.close()
r = range(params.iter)

for i in r:	#rozpoczecie obliczen
#BIOREACTOR
	#kompartment 1
	Ro1.obliczRo(C1)
	R1.obliczR(Ro1)
	C1_new.s_o =  max(m,(params.q_in/C1.v)*(C_in.s_o-C1.s_o) + (params.q_ir/C1.v)*(C_ir.s_o-C1.s_o) + (params.q_r/C1.v)*(C_r.s_o-C1.s_o) + R1.r_so + C1.s_o)
	C1_new.s_no = max(m,(params.q_in/C1.v)*(C_in.s_no-C1.s_no) + (params.q_ir/C1.v)*(C_ir.s_no-C1.s_no) + (params.q_r/C1.v)*(C_r.s_no-C1.s_no) + R1.r_sno + C1.s_no)
	C1_new.s_nd = max(m,(params.q_in/C1.v)*(C_in.s_nd-C1.s_nd) + (params.q_ir/C1.v)*(C_ir.s_nd-C1.s_nd) + (params.q_r/C1.v)*(C_r.s_nd-C1.s_nd) + R1.r_snd + C1.s_nd)
	C1_new.s_nh = max(m,(params.q_in/C1.v)*(C_in.s_nh-C1.s_nh) + (params.q_ir/C1.v)*(C_ir.s_nh-C1.s_nh) + (params.q_r/C1.v)*(C_r.s_nh-C1.s_nh)+R1.r_snh + C1.s_nh)
	C1_new.s_s =  max(m,(params.q_in/C1.v)*(C_in.s_s-C1.s_s) + (params.q_ir/C1.v)*(C_ir.s_s-C1.s_s) + (params.q_r/C1.v)*(C_r.s_s-C1.s_s)+R1.r_ss + C1.s_s)
	C1_new.s_i =  max(m,(params.q_in/C1.v)*(C_in.s_i-C1.s_i) + (params.q_ir/C1.v)*(C_ir.s_i-C1.s_i) + (params.q_r/C1.v)*(C_r.s_i-C1.s_i)+R1.r_si + C1.s_i)
	C1_new.x_h =  max(m,(params.q_in/C1.v)*(C_in.x_h-C1.x_h) + (params.q_ir/C1.v)*(C_ir.x_h-C1.x_h) + (params.q_r/C1.v)*(C_r.x_h-C1.x_h)+R1.r_xh + C1.x_h)
	C1_new.x_a =  max(m,(params.q_in/C1.v)*(C_in.x_a-C1.x_a) + (params.q_ir/C1.v)*(C_ir.x_a-C1.x_a) + (params.q_r/C1.v)*(C_r.x_a-C1.x_a)+R1.r_xa + C1.x_a)
	C1_new.x_s =  max(m,(params.q_in/C1.v)*(C_in.x_s-C1.x_s) + (params.q_ir/C1.v)*(C_ir.x_s-C1.x_s) + (params.q_r/C1.v)*(C_r.x_s-C1.x_s)+R1.r_xs + C1.x_s)
	C1_new.x_nd = max(m,(params.q_in/C1.v)*(C_in.x_nd-C1.x_nd) + (params.q_ir/C1.v)*(C_ir.x_nd-C1.x_nd) + (params.q_r/C1.v)*(C_r.x_nd-C1.x_nd) + R1.r_xnd + C1.x_nd)
	C1_new.x_p =  max(m,(params.q_in/C1.v)*(C_in.x_p-C1.x_p) + (params.q_ir/C1.v)*(C_ir.x_p-C1.x_p)+(params.q_r/C1.v)*(C_r.x_p-C1.x_p)+R1.r_xp + C1.x_p)
	C1_new.x_i =  max(m,(params.q_in/C1.v)*(C_in.x_i-C1.x_i) + (params.q_ir/C1.v)*(C_ir.x_i-C1.x_i)+(params.q_r/C1.v)*(C_r.x_i-C1.x_i)+R1.r_xi + C1.x_i)

	#kompartment 2
	Ro2.obliczRo(C2)
     	R2.obliczR(Ro2)
     	C2_new.s_o =  max(m,(params.q/C2.v) * (C1.s_o-C2.s_o)+R2.r_so + C2.s_o)
       	C2_new.s_no = max(m,(params.q/C2.v) * (C1.s_no-C2.s_no)+R2.r_sno + C2.s_no)
        C2_new.s_nd = max(m,(params.q/C2.v) * (C1.s_nd-C2.s_nd)+R2.r_snd + C2.s_nd)
        C2_new.s_nh = max(m,(params.q/C2.v) * (C1.s_nh-C2.s_nh)+R2.r_snh + C2.s_nh)
      	C2_new.s_s =  max(m,(params.q/C2.v) * (C1.s_s-C2.s_s)+R2.r_ss + C2.s_s)
        C2_new.s_i =  max(m,(params.q/C2.v) * (C1.s_i-C2.s_i)+R2.r_si + C2.s_i)
        C2_new.x_h =  max(m,(params.q/C2.v) * (C1.x_h-C2.x_h)+R2.r_xh + C2.x_h)
        C2_new.x_a =  max(m,(params.q/C2.v) * (C1.x_a-C2.x_a)+R2.r_xa + C2.x_a)
        C2_new.x_s =  max(m,(params.q/C2.v) * (C1.x_s-C2.x_s)+R2.r_xs + C2.x_s)
        C2_new.x_nd = max(m,(params.q/C2.v) * (C1.x_nd-C2.x_nd)+R2.r_xnd + C2.x_nd)
        C2_new.x_p =  max(m,(params.q/C2.v) * (C1.x_p-C2.x_p)+R2.r_xp + C2.x_p)
        C2_new.x_i =  max(m,(params.q/C2.v) * (C1.x_i-C2.x_i)+R2.r_xi + C2.x_i)

	#kompartment 3
        Ro3.obliczRo(C3)
        R3.obliczR(Ro3)
        C3_new.s_o =  max(m,(params.q/C3.v) * (C2.s_o-C3.s_o)+R3.r_so + C3.s_o + C3.k_la * (params.so_sat-C3.s_o))
        C3_new.s_no = max(m,(params.q/C3.v) * (C2.s_no-C3.s_no)+R3.r_sno + C3.s_no)
        C3_new.s_nd = max(m,(params.q/C3.v) * (C2.s_nd-C3.s_nd)+R3.r_snd + C3.s_nd)
        C3_new.s_nh = max(m,(params.q/C3.v) * (C2.s_nh-C3.s_nh)+R3.r_snh + C3.s_nh)
        C3_new.s_s =  max(m,(params.q/C3.v) * (C2.s_s-C3.s_s)+R3.r_ss  + C3.s_s)
        C3_new.s_i =  max(m,(params.q/C3.v) * (C2.s_i-C3.s_i)+R3.r_si + C3.s_i)
        C3_new.x_h =  max(m,(params.q/C3.v) * (C2.x_h-C3.x_h)+R3.r_xh + C3.x_h)
        C3_new.x_a =  max(m,(params.q/C3.v) * (C2.x_a-C3.x_a)+R3.r_xa + C3.x_a)
        C3_new.x_s =  max(m,(params.q/C3.v) * (C2.x_s-C3.x_s)+R3.r_xs + C3.x_s)
        C3_new.x_nd = max(m,(params.q/C3.v) * (C2.x_nd-C3.x_nd)+R3.r_xnd + C3.x_nd)
        C3_new.x_p =  max(m,(params.q/C3.v) * (C2.x_p-C3.x_p)+R3.r_xp + C3.x_p)
        C3_new.x_i =  max(m,(params.q/C3.v) * (C2.x_i-C3.x_i)+R3.r_xi + C3.x_i)

	#kompartment 4
        Ro4.obliczRo(C4)
        R4.obliczR(Ro4)
        C4_new.s_o =  max(m,(params.q/C4.v) * (C3.s_o-C4.s_o)+R4.r_so + C4.s_o + C4.k_la*(params.so_sat-C4.s_o))
        C4_new.s_no = max(m,(params.q/C4.v) * (C3.s_no-C4.s_no)+R4.r_sno + C4.s_no)
        C4_new.s_nd = max(m,(params.q/C4.v) * (C3.s_nd-C4.s_nd)+R4.r_snd + C4.s_nd)
        C4_new.s_nh = max(m,(params.q/C4.v) * (C3.s_nh-C4.s_nh)+R4.r_snh + C4.s_nh)
        C4_new.s_s =  max(m,(params.q/C4.v) * (C3.s_s-C4.s_s)+R4.r_ss + C4.s_s)
        C4_new.s_i =  max(m,(params.q/C4.v) * (C3.s_i-C4.s_i)+R4.r_si + C4.s_i)
        C4_new.x_h =  max(m,(params.q/C4.v) * (C3.x_h-C4.x_h)+R4.r_xh + C4.x_h)
        C4_new.x_a =  max(m,(params.q/C4.v) * (C3.x_a-C4.x_a)+R4.r_xa + C4.x_a)
        C4_new.x_s =  max(m,(params.q/C4.v) * (C3.x_s-C4.x_s)+R4.r_xs + C4.x_s)
        C4_new.x_nd = max(m,(params.q/C4.v) * (C3.x_nd-C4.x_nd)+R4.r_xnd + C4.x_nd)
        C4_new.x_p =  max(m,(params.q/C4.v) * (C3.x_p-C4.x_p)+R4.r_xp + C4.x_p)
        C4_new.x_i =  max(m,(params.q/C4.v) * (C3.x_i-C4.x_i)+R4.r_xi + C4.x_i)

	#kompartment 5
        Ro5.obliczRo(C5)
        R5.obliczR(Ro5)
        C5_new.s_o =  max(m,(params.q/C5.v) * (C4.s_o-C5.s_o)+R5.r_so + C5.s_o + C5.k_la*(params.so_sat-C5.s_o))
        C5_new.s_no = max(m,(params.q/C5.v) * (C4.s_no-C5.s_no)+R5.r_sno + C5.s_no)
        C5_new.s_nd = max(m,(params.q/C5.v) * (C4.s_nd-C5.s_nd)+R5.r_snd + C5.s_nd)
        C5_new.s_nh = max(m,(params.q/C5.v) * (C4.s_nh-C5.s_nh)+R5.r_snh + C5.s_nh)
        C5_new.s_s =  max(m,(params.q/C5.v) * (C4.s_s-C5.s_s)+R5.r_ss + C5.s_s)
        C5_new.s_i =  max(m,(params.q/C5.v) * (C4.s_i-C5.s_i)+R5.r_si + C5.s_i)
        C5_new.x_h =  max(m,(params.q/C5.v) * (C4.x_h-C5.x_h)+R5.r_xh + C5.x_h)
        C5_new.x_a =  max(m,(params.q/C5.v) * (C4.x_a-C5.x_a)+R5.r_xa + C5.x_a)
        C5_new.x_s =  max(m,(params.q/C5.v) * (C4.x_s-C5.x_s)+R5.r_xs + C5.x_s)
        C5_new.x_nd = max(m,(params.q/C5.v) * (C4.x_nd-C5.x_nd)+R5.r_xnd + C5.x_nd)
        C5_new.x_p =  max(m,(params.q/C5.v) * (C4.x_p-C5.x_p)+R5.r_xp + C5.x_p)
        C5_new.x_i =  max(m,(params.q/C5.v) * (C4.x_i-C5.x_i)+R5.r_xi + C5.x_i)

#OSADNIK
	params.X_f = 0.75*(C5.x_s+C5.x_p+C5.x_i+C5.x_h+C5.x_a)
	params.X_e = 0.75*(C_e.x_s+C_e.x_p+C_e.x_i+C_e.x_h+C_e.x_a)
	params.X_u = 0.75*(C_u.x_s+C_u.x_p+C_u.x_i+C_u.x_h+C_u.x_a)
		
	stlr.takacs(10,params.A, params.V, params.q_f, params.X_f, params.q_u, params.settlerPar, params.X, params.dX)
	stlr.clarification(C5,C_e,params.X_f,params.X_e)
	stlr.sedimentation(C5,C_u,params.X_f,params.X_u)

	for i in range(len(params.X)):
		params.X[i] = params.X[i] + params.dX[i] 
	#przepisanie obliczonych wartosci
	C1.przepisz(C1_new)
	C2.przepisz(C2_new)
	C3.przepisz(C3_new)
	C4.przepisz(C4_new)
	C5.przepisz(C5_new)
	C_ir.przepisz(C5)
	C_r.przepisz(C_u)
	C_r.s_o = 0.0

	#zapis do bazy
	r = C1.stworzRekord(params)
	db.insert('C1',r)
	r = C2.stworzRekord(params)
        db.insert('C2',r)
	r = C3.stworzRekord(params)
        db.insert('C3',r)
	r = C4.stworzRekord(params)
        db.insert('C4',r)
	r = C5.stworzRekord(params)
        db.insert('C5',r)
	r = C_ir.stworzRekord(params)
        db.insert('internal_recycle',r)
	r = C_r.stworzRekord(params)
        db.insert('external_recycle',r)

	db.insertSettler('settler', params.X)
	db.commitChanges()
	licz = licz +1
	if licz == params.progres:
		f = open('progres.txt','a')
		f.write('/')
		f.close()
		licz = 0

	#db.commitChanges()
	sym = open('/var/www/demo/ASM1/symulacje.txt', 'a')
        sym.write('Symulacja zakonczona ' + str(datetime.datetime.now()) + '\n')
	sym.close()
db.closeConn()
