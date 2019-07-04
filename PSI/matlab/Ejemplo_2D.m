%Determinamos el numero de muestras
Num_muestras=50;
x=linspace(0,10,Num_muestras);
%Fase real a la cual aspiramos
fase=10*sin(3*pi*x);
%Fase envuelta
phi=atan2((sin(fase),cos(fase));
% Desenvolvimiento de fase con Itoh

fase_unw=Desevuelve_