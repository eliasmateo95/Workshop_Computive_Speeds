from Neuron_Group import *

plt.figure(figsize=(14, 10), dpi= 80, facecolor='w', edgecolor='k')
plt.subplot(3, 1, 1)
for ii in range(0,N_Cells_IO):
    plot(IO_Statemon_Coupled.t/ms,IO_Statemon_Coupled.Vs[ii]/mV, label='IO_Cell'+str(ii+1))
title('Membrane Potential Coupled')
ylabel('V [mV]')
plt.subplot(3, 1, 2)
for ii in range(0,N_Cells_IO):
    plot(IO_Statemon_Medium_Coupled.t/ms,IO_Statemon_Medium_Coupled.Vs[ii]/mV, label='IO_Cell'+str(ii+1))
#     legend()
title('Membrane Potential Medium Coupling')
ylabel('V [mV]')
plt.subplot(3, 1, 3)
for ii in range(0,N_Cells_IO):
    plot(IO_Statemon_Uncoupled.t/ms,IO_Statemon_Uncoupled.Vs[ii]/mV, label='IO_Cell'+str(ii+1))
title('Membrane Potential Uncoupled')
xlabel('Time [ms]')
ylabel('V [mV]')
show()