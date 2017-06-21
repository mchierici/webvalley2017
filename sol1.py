data_ts = pd.read_csv("data/nb_test.txt.gz", dtype=str, sep='\t', index_col=0)
x_ts = data_ts.values[:, 1:].astype(float)
y_ts = data_ts["class"].values.astype(int)
feat_ts = data_ts.columns[1:].values.astype(str)
samp_ts = data_ts.index.values.astype(str)

