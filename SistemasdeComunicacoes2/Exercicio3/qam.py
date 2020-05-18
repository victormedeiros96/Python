from numpy import *
import matplotlib.pyplot as plt,sys
import pandas as pd 
def db2abs(x):
	return power(10,.1*x)
def genbin(n):
	return random.randint(2,size=n)
def nrz(x):
	return (1-2*x)
class C():# QAM -- QPSK
	def __init__(self,m,snrX,numerr):
		super().__init__()
		max_iter = 1000
		SNR = list()
		SER = list()
		for snr_db in arange(snrX[0],snrX[1],1):
			snr = db2abs(snr_db) #SBRdB 2 SNR abs
			n,i=self.montecarlo(snr,max_iter,m,numerr)
			ser = n/(i*m)
			print('SNR:',snr_db,'\ti:',i,'\tm:',m,'\tber:',ser)
			SER.append(ser)
			SNR.append(snr_db)
		savetxt('qpsk1.csv', array([SNR,SER]).T, delimiter=' ')
	def montecarlo(self,snr,max_iter,m,numerr):
		n_error=0
		for i in range(1,max_iter+1):
			msgQ = genbin(m)
			msgI = genbin(m)
			qamI = (left_shift(msgI,1)-1)*1j
			qamQ = left_shift(msgQ,1)-1
			canalQ = random.normal(0,1/sqrt(2*snr),m)
			canalI = 1j*random.normal(0,1/sqrt(2*snr),m)
			npsig = qamQ+qamI+canalQ+canalI
			demod_Q = real(npsig)>0
			demod_I = imag(npsig)>0
			n_error += n_error+sum(logical_or((msgQ!=demod_Q),(msgI!=demod_I)))
			if n_error>numerr:
				return (n_error,i)
class D():# QAM -- QPSK
	def __init__(self,m,snrX,numerr):
		super().__init__()
		max_iter = 1000
		SNR = list()
		SER = list()
		for snr_db in arange(snrX[0],snrX[1],1):
			snr = db2abs(snr_db) #SBRdB 2 SNR abs
			n,i=self.montecarlo(snr,max_iter,m,numerr)
			ser = n/(i*m)
			print('SNR:',snr_db,'\ti:',i,'\tm:',m,'\tber:',ser)
			SER.append(ser)
			SNR.append(snr_db)
		savetxt('qpsk2.csv', array([SNR,SER]).T, delimiter=' ')
	def montecarlo(self,snr,max_iter,m,numerr):
		n_error=0
		for i in range(1,max_iter+1):
			msgQ = genbin(m)
			msgI = genbin(m)
			qamI = (1-left_shift(msgI,1))*1j
			qamQ = 1-left_shift(msgQ,1)
			canalQ = random.normal(0,1/sqrt(2*snr),m)
			canalI = 1j*random.normal(0,1/sqrt(2*snr),m)
			npsig = qamQ+qamI+canalQ+canalI
			demod_Q = real(npsig)<0
			demod_I = imag(npsig)<0
			n_error += n_error+sum(logical_or((msgQ!=demod_Q),(msgI!=demod_I)))
			if n_error>numerr:
				return (n_error,i)
c = C(10000000,(-4,11),100)
d = D(10000000,(-4,11),100)
d1 = pd.read_csv("qpsk1.csv",sep=' ')
d2 = pd.read_csv("qpsk2.csv",sep=' ')
s1 = d1.to_numpy().T[0]
s2 = d2.to_numpy().T[0]
p1 = d1.to_numpy().T[1]
p2 = d2.to_numpy().T[1]
plt.semilogy(s1,p1)
plt.semilogy(s2,p2)
plt.ylim([1e-6,1e-1])
plt.legend(['Mapeamento Natural','Mapeamento Gray'])
plt.title("4-QAM Comparativo Entre Mapeamento Natural e Gray")
plt.xlabel("$E_b/N_0$")
plt.ylabel("$P_b$")
plt.savefig('QAM3.png',dpi=200,quality=100)
plt.show()