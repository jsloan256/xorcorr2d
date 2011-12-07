function [peaks] = xorcorr2d(corrmap)
%[peaks] = xorcorr2d(corrmap)
% A simple peak detector (just looks for zeros)
%
% corrmap: cross-correlatioin input
% peaks: a list of peak coordinates [[x1 y1]; [x2 y2]; ... ]

corr_size = size(corrmap);
corr_size_x = corr_size(1);
corr_size_y = corr_size(2);

peaks = 0;

for x = 1:corr_size_x
	for y = 1:corr_size_y
		if corrmap(x,y) == 0
			if peaks == 0
				peaks = [x y];
			else
				peaks = [peaks; [x y]];
			end
		end
	end
end
