I1=double(imread('Image-4.bmp'));
I2=double(imread('Image-5.bmp'));
I3=double(imread('Image-6.bmp'));
I4=double(imread('Image-7.bmp'));   
phi=atan2(I1-I3,I4-I2);
mesh(phi)
[renglon, columna] = size(phi);
fase=zeros(renglon,columna);
disp(size(renglon(1,:)))
%subplot(2,1,1)
%imagesc(phi)
%subplot(2,1,2)
%imagesc(fase)
fase=Desenvolvimiento_Itoh2D(phi);

p=polyfit(1:512,fase(200,:),1);
for n=1:488
    portadora(n,:)=(1:512)*p(1)+p(2);
end

craneo=fase-portadora;
mesh(craneo)