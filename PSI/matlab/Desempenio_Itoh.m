%Determinamos el numero de muestras
Num_muestras=100;
x=linspace(0,1,Num_muestras);
%Fase real a la cual aspiramos
fase=10*sin(3*pi*x);
%Fase envuelta
phi=atan2(sin(fase),cos(fase));
% Desenvolvimiento de fase con Itoh
fase_unw=Desenvuelve_Itoh(phi);

delta_fase=fase(2:Num_muestras)-fase(1:Num_muestras-1);

%Graficamos resultados
subplot(3,1,1)
plot(phi,'+-r'); hold on;
%fase real
plot(fase, 'db-');
%Fase desenvuelta
plot(fase_unw,'sm-'), ylim([-10,10]);
xlabel('Numero de muestra')
ylabel('Fase en radianes'); hold off

subplot(3,1,2)
plot(abs(delta_fase)/pi, 's-')
xlabel('Numero de muestra')
ylabel('Fase normalizada (pi)')
ylim([0,2]), grid on;

subplot(3,1,3)
plot(sin(fase),'*k-'); hold off;

