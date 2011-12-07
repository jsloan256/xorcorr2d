run random_walk_08p_01.m

i = map;
home = my_hill;
e_hills = [e1_hill; e2_hill; e3_hill; e4_hill; e5_hill; e6_hill; e7_hill];

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

disp("Hills:");
e_hills
