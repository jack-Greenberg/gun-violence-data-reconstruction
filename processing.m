% grab data
data = readmatrix('clean.csv');
data(isnan(data)) = 1; % replaces all NaN values with 1, which assumes that there is a minimum of 1 gun involved

% perform PCA using SVD
sv = 30;
[U, sigma, V] = svds(data, sv);
data_recon = U(:, 1:sv) * sigma(1:sv, 1:sv) * V(:, 1:sv)'

% check for accuracy
data_recon_stack = reshape(data_recon, [1365 1]);
data_stack = reshape(data, [1365 1]);
norm(data_recon_stack - data_stack)