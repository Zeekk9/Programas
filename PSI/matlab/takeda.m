I=double(imread('5.png'));
%figure,imagesc(abs(I))
If=FT2Dc(I);
% x = 1:length(I(1,:));
% y = 1:length(I(:,1));
% [X,Y] = meshgrid(x,y);
%figure,imagesc(abs(If))
%Se grafica If para ver donde filtrar
%figure,mesh(abs(If))
%Aproximadamente en 330-38-->x;215,260-->y
%Se crea el filtro
Filter=zeros(size(I));
Filter(350:450,300:400)=1;
%figure,mesh(Filter),title('Filtro')
filter_signal=Filter.*If;
figure,mesh(abs(filter_signal))
iff_fs=ifft2(ifftshift(filter_signal));
phase=atan2(imag(iff_fs),real(iff_fs));
figure,mesh(phase)
fase=Desenvolvimiento_Itoh2D(phase);
figure,mesh(fase)
p=polyfit(1:640,fase(200,:),1);
for n=1:480
    portadora(n,:)=p(1)*(1:640)+p(2);
end

psi=fase-portadora;
figure,mesh(psi)