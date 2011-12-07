run setup_sample_image.m
mask = grabmask([5 5], 5, i);
cm = xorcorr2d(i, mask);
peaks = simplepeak(cm);

disp("Image:");
i

disp("Mask:");
mask

disp("Correlation Result:");
cm

disp("Peaks found:");
peaks
