%% Programa que verifica el funcionamiento del m�todo de Itoh
% para desenvolver la fase
%% Creamos la fase envuelta 
t=linspace(0,1,200);
fase=2*pi*3*(t-0.5).^2;
% Fase envuelta
W=atan2(sin(fase),cos(fase));
phi=Desenvuelve_Itoh(W);
plot(fase/pi)
hold on
plot(W/pi,'>r')
plot(phi/pi,'g')
grid on
ylim([-2,6])
hold off
 