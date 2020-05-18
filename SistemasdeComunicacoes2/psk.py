from scipy.special import erfc
from numpy import linspace,logspace,array,sqrt,sin,pi,log2,power,log10,savetxt
import matplotlib.pyplot as plt,sys
Q = lambda x:1/2*erfc(x/sqrt(2))
SNRdB = linspace(-2,25,28)
SNR = 10**(.1*SNRdB)
SNRdB = SNRdB.reshape(1,28)
SNR = SNR.reshape(1,28)
##################### 2
Pe2 = Q(sqrt(2*SNR))
##################### 4
Pe4 = 1-power((1-Q(sqrt(2*SNR))),2)
##################### +
M = array([8,16]).reshape(2,1)
Pe_n = 2*Q(sqrt(2*log2(M)*power(sin(pi/M),2)*SNR))
lista = [SNRdB[0],Pe2[0],Pe4[0]]
for i in range(len(Pe_n)):
	lista.append(Pe_n[i])
legenda=['M = 2','M = 4']
for i in range(len(M)):
	legenda.append('M = '+str(M[i]))
# savetxt('{}_teorico.csv'.format(sys.argv[0][0:3]), array(lista).T, delimiter=',')
# savetxt('{}_teorico2.csv'.format(sys.argv[0][0:3]), array(lista).T, delimiter=' ')
plt.semilogy(SNRdB.T,Pe2.T)
plt.semilogy(SNRdB.T,Pe4.T)
plt.semilogy(SNRdB.T,Pe_n.T)
plt.xlabel('$\\frac{E_b}{N_0}}$ dB')
plt.ylabel('$P_e$ dB')
plt.title('M-PSK Probability of Error vs SNR')
plt.subplots_adjust(bottom=0.14)
plt.legend(legenda)
plt.grid()
plt.ylim(1e-6,1e-1)
plt.xlim(-2,20)
plt.savefig(sys.argv[0][:-3]+'.png',dpi=1000,quality=100)
# plt.show()