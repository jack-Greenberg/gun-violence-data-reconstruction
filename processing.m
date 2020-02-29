ktr = load("known_training.csv");
kte = load("known_test.csv");
utr = load("unknown_training.csv");
ute = load("unknown_test.csv");

X = inv(ktr' * ktr) * ktr' * utr;

ute_recon = kte * X;
ute_recon_vector = reshape(ute_recon, [], 1);
ute_vector = reshape(ute, [], 1);

norm(ute_recon_vector - ute_vector)