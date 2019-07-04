function fase = Desenvolvimiento_Itoh2D(phi)
[renglon, columna] = size(phi);
fase = zeros(renglon, columna);
phi(:,1)=Desenvuelve_Itoh(phi(:,1));
for n=1: renglon
    fase(n,:)=Desenvuelve_Itoh(phi(n,:));
end
end