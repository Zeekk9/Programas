clc
close all
clear
npoints=512;
perc=1;
dt=6*1E-7/(npoints*perc);  % Tempo di campionamento
df=1/(npoints*dt); % Frequenza di campionamento

t(1)=0;
f(1)=0;
for k=2:npoints/2
    t(k)=(k-1)*dt;
    t(npoints-k+2)=-t(k);
    f(k)=(k-1)*df;
    f(npoints-k+2)=-f(k);
end
t(npoints/2+1)=t(npoints/2+2)-dt;
f(npoints/2+1)=f(npoints/2+2)-df;

ts=ifftshift(t);
fs=fftshift(f);

figure
[X,Y]=meshgrid(ts,ts);

D = npoints/2;        % to indicate origin at the center of the function
a = 5;          % change it to enlarge or reduce the pulse
y = repmat(1:npoints,npoints,1);
x = y';
rect = zeros(npoints);
rect(D-a:D+a-1,D-a:D+a-1) = ones(2*a);
rect=(rect);
surf(X,Y,rect);
shading interp
axis tight
title ('Rect 3D');
rect=ifftshift(rect);
figure, surf(X,Y,rect);
shading interp
axis tight
title ('Rect 3D shifted');