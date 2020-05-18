from numpy import *
import matplotlib.pyplot as plt,sys
import pandas as pd 
class A():# 4PAM
	def __init__(self,m,snrX,numerr):
		super().__init__()
		max_iter = 10000
		SNR = list()
		SER = list()
		for snr_db in range(snrX[0],snrX[1],1):
			snr = 2*power(10,.1*(snr_db))
			n,i=self.montecarlo(snr,max_iter,m)
			ser = n/(i*m)
			print('snr:',snr_db,'i:',i,'\tm:',m,'\tser:',ser)
			SER.append(ser)
			SNR.append(snr_db)
		savetxt('semgray.csv', array([SNR,SER]).T, delimiter=' ',header='f A')
		# plt.semilogy(SNR,SER)
		# plt.grid()
		# plt.xlabel('$\\frac{E_b}{N_0}$')
		# plt.ylabel('$P_e$ Error Probability')
	def convert_mod_msg(self,n):
		t2 = logical_and(n>=-2,n<0) #1
		t3 = logical_and(n>=0,n<2) #2
		t4 = (n>=2) #3
		x1 = len(n)*[0]
		x2 = len(n)*[0]
		x1 = t3*[1]
		x2 = t2*[1]
		x1 = t4*[1]+x1
		x2 = t4*[1]+x2
		return concatenate([x1,x2])
	def pam4demod(self,n):
		m = self.convert_mod_msg(n)
		return m
	def pam4(self,n):
		t1 = -3*logical_and(n[0,:]==0,n[1,:]==0)
		t2 = -1*logical_and(n[0,:]==0,n[1,:]==1)
		t3 = 1*logical_and(n[0,:]==1,n[1,:]==0)
		t4 = 3*logical_and(n[0,:]==1,n[1,:]==1)
		return t1+t2+t3+t4
	def montecarlo(self,snr,max_iter,m):
		n_error=0
		for i in range(1,max_iter+1):
			msg_orig = random.randint(2,size=2*m)
			msg = resize(msg_orig,(2,m))
			msg_gray = self.pam4(msg)
			canal = random.normal(0,1/sqrt(2*snr),m)
			npsig = msg_gray/sqrt(5)+canal	#Noise plus Signal
			demod_msg = self.pam4demod(sqrt(5)*npsig)		
			n_error = n_error+sum(msg_orig!=demod_msg)
			if n_error>100:
				return (n_error,i)
		return(n_error,i)
class B():# 4PAM
	def __init__(self,m,snrX,numerr):
		super().__init__()
		max_iter = 10000
		SNR = list()
		SER = list()
		for snr_db in range(snrX[0],snrX[1],1):
			snr = 2*power(10,.1*(snr_db))
			n,i=self.montecarlo(snr,max_iter,m)
			ser = n/(i*m)
			print('snr:',snr_db,'i:',i,'\tm:',m,'\tser:',ser)
			SER.append(ser)
			SNR.append(snr_db)
		savetxt('comgray.csv', array([SNR,SER]).T, delimiter=' ',header='f A')
		# plt.semilogy(SNR,SER)
		# plt.grid()
		# plt.xlabel('$\\frac{E_b}{N_0}$')
		# plt.ylabel('$P_e$ Error Probability')
	def convert_mod_msg(self,n):
		t2 = logical_and(n>=-2,n<0) #1
		t3 = logical_and(n>=0,n<2) #3
		t4 = (n>=2) #2
		x1 = len(n)*[0]
		x2 = len(n)*[0]
		x1 = t4*[1]
		x2 = t2*[1]
		x1 = x1+t3*[1]
		x2 = x2+t3*[1]
		return concatenate([x1,x2])
	def pam4demod(self,n):
		m = self.convert_mod_msg(n)
		return m
	def pam4(self,n):
		t1 = -3*logical_and(n[0,:]==0,n[1,:]==0)
		t2 = -1*logical_and(n[0,:]==0,n[1,:]==1)
		t3 = 1*logical_and(n[0,:]==1,n[1,:]==1)
		t4 = 3*logical_and(n[0,:]==1,n[1,:]==0)
		return t1+t2+t3+t4
	def montecarlo(self,snr,max_iter,m):
		n_error=0
		for i in range(1,max_iter+1):
			msg_orig = random.randint(2,size=2*m)
			msg = resize(msg_orig,(2,m))
			msg_gray = self.pam4(msg)
			canal = random.normal(0,1/sqrt(2*snr),m)
			npsig = msg_gray/sqrt(5)+canal	#Noise plus Signal
			demod_msg = self.pam4demod(sqrt(5)*npsig)		
			n_error = n_error+sum(msg_orig!=demod_msg)
			if n_error>100:
				return (n_error,i)
		return(n_error,i)
a = A(10000000,(4,16),100)
b = B(10000000,(4,16),100)
d1 = pd.read_csv("semgray.csv",sep=' ')
d2 = pd.read_csv("comgray.csv",sep=' ')
s1 = d1.to_numpy().T[0]
s2 = d2.to_numpy().T[0]
p1 = d1.to_numpy().T[1]
p2 = d2.to_numpy().T[1]
plt.semilogy(s1,p1)
plt.semilogy(s2,p2)
plt.ylim([1e-6,1e-1])
plt.legend(['Mapeamento Natural','Mapeamento Gray'])
plt.title("4-PAM Comparativo Entre Mapeamento Natural e Gray")
plt.xlabel("$E_b/N_0$")
plt.ylabel("$P_b$")
plt.savefig('PAM3.png',dpi=200,quality=100)
plt.show()