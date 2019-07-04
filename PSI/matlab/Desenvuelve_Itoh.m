%% Este programa realiza el Desenvolvimiento
% de fase mediante el metodo de Itoh
% Para que funcione es necesario entregar 
% un vector W que contenga a fase envuelta
% El resultado en phi la fase desenvuelta

function phi=Desenvuelve_Itoh(W)
%Determinamos el numero de elementos
Num_Datos=length(W);
%Incializamos e vector de fase  desenvueta
phi(1)= W(1);
%Inicializamos el ciclo de iteracion
for m=2:Num_Datos
    Delta=W(m) - W(m-1);
    WDelta=atan2(sin(Delta),cos(Delta));
    phi(m)=phi(m-1) + WDelta;
end
end 