import pickle
from PYEVALB import scorer
from PYEVALB import parser
'''

Su dung thu vien PYEVALB danh gia mo hinh

'''

# Evaluation Tokenizer


def Hand():
    with open('input/data_tokenizer.txt') as f:
        data = f.read()
        lines = data.split('\n')

    tokens = []
    for i in lines:
        token = i.split()
        tokens.append(token)

    pickle.dump(tokens, open('output/data_tokenizer.pkl', 'wb'))


def Token_Eva(path2Tokenizer):
    '''

    Danh gia precision va recall cua tokenizer
    '''
    pre = pickle.load(open(path2Tokenizer, 'rb'))
    hand = pickle.load(open('output/data_tokenizer.pkl', 'rb'))

    precision = 0
    recall = 0

    for idx, i in enumerate(pre):
        inpre = [x for x in i if x not in hand[idx]]

        s = sum([i.count(x) for x in inpre])

        if len(i) - s > 0:
            print(i)
        precision += (len(i) - s) / len(i)
        recall += (len(i) - s) / len(hand[idx])

    precision, recall = precision / len(pre) * 100, recall / len(pre) * 100
    print('Precision : {} | Recall: {}'.format(precision, recall))
    return precision, recall


gold = "(S (S1 (NP (NP (M Một) (NP (N xã) (N đảo))) (NP (NP (A gần) (NP (M 90) (N công_trình))) (VP (V xây_dựng) (A trái_phép)))) (PUP ,)) (S (VP (VP (R sẽ) (V cưỡng_chế)) (NP (M 74) (N công_trình))) (PU .)))"

pred = "(S(S(NP(NP(NP(M Một)(NP(NP(N xã)(N đảo))(A gần)))(M 90))(NP(NP(N công_trình)(V xây_dựng))(A trái_phép)))(VP(VP(PUP ,)(VP(R sẽ)(V cưỡng_chế)))(NP(M 74)(N công_trình))))(PU .))"
#  print(get_match(tree_from_str(gold), tree_from_str(pred)))


def Parser_Eva():

    with open('output/data_gold_NLP.txt', 'r') as f:
        list_Golds = f.read().split('\n')

    list_Preds = pickle.load(open('output/nlp_preds.pkl', 'rb'))
    num_test = len(list_Golds)

    list_Recall = [None] * num_test
    list_Prec = [None] * num_test
    list_Ave = [None] * num_test
    #  print(list_Preds[24][0])
    #  print(list_Recall)
    for idx in range(num_test):
        list_Recall[idx] = []
        list_Prec[idx] = []
        recall = 0
        prec = 0
        if len(list_Preds[idx]) > 0:
            #  print(idx, len(list_Preds[idx]))
            try:
                gold_tree = parser.create_from_bracket_string(list_Golds[idx])
                for j in list_Preds[idx]:
                    test_tree = parser.create_from_bracket_string(j)
                    sc = scorer.Scorer()
                    result = sc.score_trees(gold_tree, test_tree)
                    recall += result.recall
                    prec += result.prec
                    list_Recall[idx].append(result.recall)
                    list_Prec[idx].append(result.prec)

                recall /= len(list_Preds[idx])
                prec /= len(list_Preds[idx])

            except:
                print(idx, list_Golds[idx])
                print(list_Preds[idx][0])

        else:
            list_Recall[idx].append(recall)
            list_Prec[idx].append(prec)
        list_Ave[idx] = [prec, recall]

    pickle.dump(list_Prec, open('output/list_Prec.pkl', 'wb'))
    pickle.dump(list_Recall, open('output/list_Recall.pkl', 'wb'))
    pickle.dump(list_Ave, open('output/list_Ave.pkl', 'wb'))

    return list_Ave


list_Ave = Parser_Eva()

#  for i in list_Ave:
#  print('Precision: {} | Recall: {}'.format(i[0],i[1]))
list_Prec = pickle.load(open('output/list_Prec.pkl', 'rb'))
list_Recall = pickle.load(open('output/list_Recall.pkl', 'rb'))
list_Ave = pickle.load(open('output/list_Ave.pkl', 'rb'))

#  print(list_Prec)
sum_st1_recall = 0
sum_st1_prec = 0
sum_ave_prec = 0
sum_ave_recall = 0
lenl = len(list_Recall)

#  p1 = pickle.load(open('output/list_preds.pkl', 'rb'))
#  p2 = pickle.load(open('output/nlp_preds.pkl', 'rb'))

for idx in range(lenl):
    sum_st1_prec += list_Prec[idx][0]
    sum_st1_recall += list_Recall[idx][0]

    sum_ave_prec += list_Ave[idx][0]
    sum_ave_recall += list_Ave[idx][1]

    #  print('ST1: Precision: {} | Recall: {}'.format(list_Prec[idx][0], list_Recall[idx][0]))
    #  print('AVE: Precision: {} | Recall: {}'.format(list_Ave[idx][0],list_Ave[idx][1]))

sum_ave_recall /= lenl
sum_ave_prec /= lenl
sum_st1_prec /= lenl
sum_st1_recall /= lenl

#print(sum_st1_prec, sum_st1_recall, sum_ave_prec, sum_ave_recall)
Token_Eva('output/VnCore_Tokens.pkl')
