run random_walk_08p_01.m

i = map;
home = a;

mask = grabmask(home, 5, i);
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
