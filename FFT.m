Fs = 10000;
t = linspace(-10,10,Fs);
x = t.^2;
x_prim=2*t;
xdft = fftshift(fft(x));
df = Fs/length(x);
freq = -Fs/2:df:Fs/2-df;
fd=ifft(fft(x)*2*i.*freq*pi);
subplot(211)
plot(t,real(fd))
title('FFT derivate')
subplot(212)
plot(t,x_prim)
title('Analytical derivate')