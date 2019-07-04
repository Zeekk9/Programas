%---------------------------------------------------------%
%--Basic High pass and Low pass filter--------------------%
%---------------------------------------------------------%

clc
close all
clear all

I=imread('5.png');

%I=rgb2gray(RGB); % convert the image to grey 

A = fft2(double(I)); % compute FFT of the grey image
Y=fftshift(A); % frequency scaling


 
[M N]=size(A); % image size
D=30; % filter size parameter 

% defining a typical low pass filter response H(f)
% Low pass filter has value=1  in the 
% low frequency region and value=0 in the high freq
% region

Lo(1:M,1:N)=0;
Lo(0.5*M-D:0.5*M+D,0.5*N-D:0.5*N+D)=1;

% defining a typical high pass filter response H(f)
% High pass filter has value=1 in
% the high frequency region and value=0 in the low
% frequency region

Hi(1:M,1:N)=1;
Hi(0.5*M-D:0.5*M+D,0.5*N-D:0.5*N+D)=0;

% Filtered image=filter response*fft(original image)

J=Y.*Lo;
J1=ifftshift(J);
B1=ifft2(J1);

K=Y.*Hi;
K1=ifftshift(K);
B2=ifft2(K1);
