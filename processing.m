% Import data
data = readmatrix('./clean.csv');

% replaces all NaN values with 1, which assumes that there is a minimum of 1 gun involved
data(isnan(data)) = 1;

% Perform singular value decomposition on the data
sv = 80; % Number of singular vectors to use
[U, sigma, V] = svds(data, sv);

reconstructed_data = U(:, 1:sv) * sigma(1:sv, 1:sv) * V(:, 1:sv)';

% Reshape reconstructed data into a vector
reconstructed_data_stack = reshape(reconstructed_data,...
    [size(reconstructed_data,1)*size(reconstructed_data,2) 1]);

% Reshape original data into a vector
data_stack = reshape(data, [size(data,1)*size(data,2) 1]);

% Measure distance between original data and reconstructed data
norm(reconstructed_data_stack - data_stack)
