function [corrmap] = xorcorr2d(im, mask)
%[corrmap] = xorcorr2d(im, mask)
% XOR Cross-Correlation function for binary images
%
% im: input image (may be rectangular)
% mask: should be square and odd
% corrmap: cross-correlatioin output. '0' is mean a perfect match

%Find the mask size and verify that it is square
mask_size = size(mask);

if (mask_size(1) != mask_size(2))
	disp("mask is not square");
	return
end
mask_size = mask_size(1);

% Pad the image by 1/2 the mask size (-1)
padding = floor(mask_size/2);
% This assumes square images... needs to be fixed
im_size = size(im);
im_size_x = im_size(1);
im_size_y = im_size(2);
img = zeros(im_size_x+(padding*2),im_size_x+(padding*2));
size(im)
size(img)

img(padding+1:(im_size_x+padding), padding+1:(im_size_y+padding)) = im;
%%%%%%%%%%% Finish padding (should be padded with data, not zeros) %%%%%%%%%%%%

% Correlate the mask against the image
corrmap = 999 * ones(im_size_x,im_size_y);
for x = padding+1:(im_size_x+padding)
	for y = padding+1:(im_size_y+padding)
		corrmap(x-padding, y-padding) = sum(sum(xor(img(x-padding:x+padding,y-padding:y+padding), mask)));
	end
end

