import pickle

nlp_preds = pickle.load(open('output/nlp_preds.pkl', 'rb'))

i = 11
j = 3

print('CORENLP')
print(nlp_preds[i][0])

cky_preds = pickle.load(open('output/list_preds.pkl', 'rb'))

print('\nCKY')
for idx in range(j):
    print(cky_preds[i][idx])
    print()


