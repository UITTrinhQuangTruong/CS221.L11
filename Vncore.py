from vncorenlp import VnCoreNLP

rdrsegmenter = VnCoreNLP("vncorenlp/VnCoreNLP-1.1.1.jar",
                         annotators="wseg",
                         max_heap_size='-Xmx1g')


def wordTokenzizer(sentence):
    '''

    Tach tu voi thu vien VnCoreNLP

    '''
    token = [i for j in rdrsegmenter.tokenize(sentence) for i in j]
    return ' '.join(token)


def wordsTokenzizer(path2Raw='input/data_raw.txt'):
    '''

    Tach nhieu cau thanh tu voi thu vien VnCoreNLP

    '''
    list_Tokens = []
    list_LinesTokens = []
    with open(path2Raw, 'r') as f:
        data = f.read()

        list_Lines = data.split('\n')
        for line in list_Lines:
            token = [i for j in rdrsegmenter.tokenize(line) for i in j]
            list_LinesTokens.append(' '.join(token))
            list_Tokens.append(token)

    return list_Tokens, list_LinesTokens


#  list_Tokens, list_LinesTokens = wordsTokenzizer()
#  pickle.dump(list_Tokens, open('output/VnCore_Tokens.pkl', 'wb'))
#
#  with open('output/VnCore_Lines.txt', 'w') as f:
#      for line in list_LinesTokens:
#          f.write(line)
#          f.write('\n')
#
