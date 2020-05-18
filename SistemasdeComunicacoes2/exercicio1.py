from scipy.special import erfc
from numpy import linspace,array,sqrt,sin,pi,log2,savetxt
import matplotlib.pyplot as plt,sys
n=8
M = 2*2**array(range(0,n))
M = M.reshape(n,1)
SNR = linspace(1,50,50)
SNR = SNR.reshape(1,50)
Ps_fsk = (M-1)/2*erfc(sqrt(SNR*log2(M)/2))
legenda1=list()
for i in range(len(M)):
	legenda1.append('FSK -- M = '+str(M[i]))
n=4
M = 2*2**array(range(0,n))
M = M.reshape(n,1)
SNR = linspace(1,50,50)
SNR = SNR.reshape(1,50)
Ps_pam = (M-1)/M*erfc(sqrt(3*SNR/(M**2-1)))
legenda2=list()
for i in range(len(M)):
	legenda2.append('PAM -- M = '+str(M[i]))
n=4
M = 8*2**array(range(0,n))
M = M.reshape(n,1)
SNR = linspace(1,50,50)
SNR = SNR.reshape(1,50)
Ps_psk = erfc(sqrt(SNR)*sin(pi/M))
legenda3=list()
for i in range(len(M)):
	legenda3.append('PSK -- M = '+str(M[i]))
n=4
M = 4*4**array(range(0,n))
M = M.reshape(n,1)
SNR = linspace(1,50,50)
SNR = SNR.reshape(1,50)
Ps_qam = (1-1/sqrt(M))*erfc(sqrt(3/2*SNR/(M-1)))
legenda4=list()
for i in range(len(M)):
	legenda4.append('QAM -- M = '+str(M[i]))
legenda = legenda1+legenda2+legenda3+legenda4
plt.loglog(SNR.T,Ps_fsk.T,SNR.T,Ps_pam.T,SNR.T,Ps_psk.T,SNR.T,Ps_qam.T)
plt.xlabel('$\\frac{E_b}{N_0}}$ dB')
plt.ylabel('$P_e$ dB')
plt.title('M-ARIA Probability of Error vs SNR')
plt.subplots_adjust(bottom=0.14)
plt.legend(legenda,fontsize='x-small')
plt.grid()
plt.savefig('todas.png',dpi=250,quality=100)
plt.show()
