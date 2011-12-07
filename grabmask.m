function [mask] = grabmask(position, mask_size, img)
%[mask] = grabmask(position, mask_size, img)
% Grab a mask from the input image
%
% position: location of the center of the mask ([x y])
% mask_size: side of the square shaped mask
% img: input image (2D matrix)
% [mask]: A size X size matrix cropped from the input image

pos_x = position(1);
pos_y = position(2);
mask = img(pos_x-floor(mask_size/2):pos_x+floor(mask_size/2), pos_y-floor(mask_size/2):pos_y+floor(mask_size/2));
