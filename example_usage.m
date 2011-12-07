run setup_sample_image.m
cm = xorcorr2d(i, m);
peaks = simplepeak(cm);

disp("Image:");
i

disp("Mask:");
m

disp("Correlation Result:");
cm

disp("Peaks found:");
peaks
