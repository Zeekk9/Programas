%% Este programa realiza el Desenvolvimiento
% de fase mediante el metodo de Itoh
% Para que funcione es necesario entregar 
% una matriz W que contenga a fase envuelta
% El resultado en phi la fase desenvuelta

function phi=Desenvuelve_Itoh(W)
%Determinamos el numero de elementos
[renglon columna]=size(W);
%Incializamos e vector de fase desenvueta
phi(1,1)= W(1,1);
%Inicializamos el ciclo de iteracion
for m=2:renglon
    Delta=W(1,m) - W(1,m-1);
    WDelta=atan2(sin(Delta),cos(Delta));
    phi(1,m)=phi(1,m-1) + WDelta;
end

for k=1:renglon
    for p=2:columna
    Delta=W(k,p) - W(k,p-1);
    WDelta=atan2(sin(Delta),cos(Delta));
    phi(k,p)=phi(k,p-1) + WDelta;
    end
end

end 