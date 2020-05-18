# from scipy.special import erfc
from numpy import *
import matplotlib.pyplot as plt,sys
def db2abs(x):
	return power(10,.1*x)
def genbin(n):
	return random.randint(2,size=n)
def nrz(x):
	return (1-2*x)
class A():# BPSK 2PAM
	def __init__(self,m,snrX,numerr):
		super().__init__()
		max_iter = 10000
		SNR = list()
		BER = list()
		for snr_db in range(snrX[0],snrX[1],1):
			snr = db2abs(snr_db) #SBRdB 2 SNR abs
			n,i=self.montecarlo(snr,max_iter,m,numerr)
			ber = n/(i*m)
			print('i:',i,'\tm:',m,'\tber:',ber)
			BER.append(ber)
			SNR.append(snr_db)
		savetxt('montecarlo/bpsk.csv', array([SNR,BER]).T, delimiter='    ')
		# plt.semilogy(SNR,BER)
		# plt.grid()
		# plt.xlabel('$\\frac{E_b}{N_0}$')
		# plt.ylabel('$P_e$ Error Probability')
	def montecarlo(self,snr,max_iter,m,numerr):
		n_error=0
		for i in range(1,max_iter+1):
			msg = genbin(m)
			bpsk = 1-left_shift(msg,1)
			canal = random.normal(0,1/sqrt(2*snr),m)
			npsig = bpsk+canal	#Noise plus Signal
			demod_msg = npsig<0
			n_error += n_error+sum(msg!=demod_msg)
			if n_error>numerr:
				return (n_error,i)
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
		savetxt('montecarlo/4pam.csv', array([SNR,SER]).T, delimiter='    ')
		plt.semilogy(SNR,SER)
		plt.grid()
		plt.xlabel('$\\frac{E_b}{N_0}$')
		plt.ylabel('$P_e$ Error Probability')
	def convert_mod_msg(self,n):
		t1 = (n<-2) #0
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
		# plt.semilogy(SNR,SER)
		# plt.grid()
		# plt.xlabel('$\\frac{E_b}{N_0}$')
		# plt.ylabel('$P_e$ Error Probability')
		savetxt('montecarlo/qpsk.csv', array([SNR,SER]).T, delimiter='    ')
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
class D():
	def __init__(self,m,snrX,numerr):
		super().__init__()
		max_iter = 10000
		SNR = list()
		SER = list()
		for snr_db in range(snrX[0],snrX[1],1):
			snr = db2abs(snr_db) #SBRdB 2 SNR abs
			n,i=self.montecarlo(snr,max_iter,m,numerr)
			ser = n/(i*m)
			print('SNR:',snr_db,'i:',i,'\tm:',m,'\tber:',ser)
			SER.append(ser)
			SNR.append(snr_db)
		savetxt('montecarlo/bfsk.csv', array([SNR,SER]).T, delimiter='    ')
		# plt.figure()
		# plt.semilogy(SNR,SER)
		# plt.grid()
		# plt.xlabel('$\\frac{E_b}{N_0}$')
		# plt.ylabel('$P_e$ Error Probability')
	def montecarlo(self,snr,max_iter,m,numerr):
		n_error=0
		for i in range(1,max_iter+1):
			msg = genbin(m)
			aux1 = 1j*(msg==0)
			aux2 = 1*(msg==1)
			bfsk = aux1+aux2
			ch1 = 1*random.normal(0,1/sqrt(2*snr),m)
			ch2 = 1j*random.normal(0,1/sqrt(2*snr),m)
			npsig = bfsk+ch1+ch2	#Noise plus Signal
			demod_msg = real(npsig)>imag(npsig)
			n_error += n_error+sum(msg!=demod_msg)
			if n_error>numerr:
				return (n_error,i)
		return (n_error,i)
a = A(10000000,(-2,11),100)
b = B(10000000,(2,14),100)
c = C(10000000,(-4,11),100)
d = D(10000000,(0,13),100)
plt.show()