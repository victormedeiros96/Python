from scipy.special import erfc
from numpy import linspace,array,sqrt,sin,pi,log2,savetxt
import matplotlib.pyplot as plt,sys
n=8
M = 2*2**array(range(0,n))
M = M.reshape(n,1)
# Q = lambda x:1/2*erfc(x/sqrt(2))
SNRdB = linspace(-2,25,28)
SNR = 10**(.1*SNRdB)
SNR = SNR.reshape(1,28)
Ps = (M-1)/2*erfc(sqrt(SNR*log2(M)/2))
legenda=list()
for i in range(len(M)):
	legenda.append('M = '+str(M[i]))
lista = [SNRdB]
for i in range(len(Ps)):
	lista.append(Ps[i])
# savetxt('{}_teorico.csv'.format(sys.argv[0][0:3]), array(lista).T, delimiter=',')
# savetxt('{}_teorico2.csv'.format(sys.argv[0][0:3]), array(lista).T, delimiter=' ')
plt.semilogy(SNRdB.T,Ps.T)
plt.xlabel('$\\frac{E_b}{N_0}}$ dB')
plt.ylabel('$P_e$ dB')
plt.title('M-FSK Probability of Error vs SNR')
plt.subplots_adjust(bottom=0.14)
plt.legend(legenda)
plt.grid()
plt.ylim(1e-6,1e-1)
plt.xlim(0,16)
plt.savefig(sys.argv[0][:-3]+'.png',dpi=1000,quality=100)
# plt.show()