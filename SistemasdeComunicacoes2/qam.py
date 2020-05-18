from scipy.special import erfc
from numpy import linspace,array,sqrt,sin,pi,savetxt,log2
import matplotlib.pyplot as plt,sys
Q = lambda x: 0.5*erfc(x/sqrt(2))
n=4
M = 4*4**array(range(0,n))
M = M.reshape(n,1)
SNRdB = linspace(-2,25,28)
SNR = 10**(.1*SNRdB)
SNR = SNR.reshape(1,len(SNR))
aux = Q(sqrt(3*log2(M)*SNR/(M-1)))
Ps = 4*(1-1/sqrt(M))*aux*(1-(1-1/sqrt(M))*aux)
legenda=list()
for i in range(len(M)):
	legenda.append('M = '+str(M[i]))
lista = [SNRdB]
for i in range(len(M)):
	lista.append(Ps[i])
# savetxt('{}_teorico.csv'.format(sys.argv[0][0:3]), array(lista).T, delimiter=',')
# savetxt('{}_teorico2.csv'.format(sys.argv[0][0:3]), array(lista).T, delimiter=' ')
plt.semilogy(SNRdB,Ps.T)
plt.xlabel('$\\frac{E_b}{N_0}}$ dB')
plt.ylabel('$P_e$ dB')
plt.title('M-QAM Probability of Error vs SNR')
plt.subplots_adjust(bottom=0.14)
plt.legend(legenda)
plt.grid()
plt.ylim(1e-6,1e-1)
plt.xlim(-2,25)
plt.savefig(sys.argv[0][:-3]+'.png',dpi=1000,quality=100)
# plt.show()