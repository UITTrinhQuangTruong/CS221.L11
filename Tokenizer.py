import pickle


def getDictionary(path2Dictionary='input/Dictionary.pkl'):
    list_Words = pickle.load(open(path2Dictionary, 'rb'))
    return list_Words


def maximumMatching(sentence, maxlen=4):
    '''

        Thuat toan tach tu bang Maximum Matching

    '''

    dictionary = getDictionary()

    my_list = []
    list_Words = sentence.split()
    len_now = len(list_Words)
    i = 0
    maxl = maxlen
    while i < len_now:
        wordCheck = '_'.join(list_Words[i:maxlen + i])

        while wordCheck not in dictionary:
            #  print(wordCheck)
            if maxl > 1:
                wordCheck = '_'.join(list_Words[i:i + maxl])
            elif maxl == 1:
                wordCheck = list_Words[i]
            elif maxl == 0:
                break
            maxl -= 1
        if maxl > 0:
            i += maxl
        i += 1
        #  print('TRUE {} | Len: {}'.format(wordCheck, maxl))
        my_list.append(wordCheck)
        maxl = min(len_now - i, maxlen)

    line = ' '.join(my_list)

    return line


def maximumsMatching(lines, maxlen=4):
    '''

        Tach nhieu cau bang Maximum Matching

    '''
    dictionary = getDictionary()

    list_Tokenizer = []
    list_Lines = []
    for line in lines:
        my_list = []
        list_Words = line.split()
        len_now = len(list_Words)
        i = 0
        maxl = maxlen
        while i < len_now:
            wordCheck = '_'.join(list_Words[i:maxlen + i])

            while wordCheck not in dictionary:
                #  print(wordCheck)
                if maxl > 1:
                    wordCheck = '_'.join(list_Words[i:i + maxl])
                elif maxl == 1:
                    wordCheck = list_Words[i]
                elif maxl == 0:
                    break
                maxl -= 1
            if maxl > 0:
                i += maxl
            i += 1
            #  print('TRUE {} | Len: {}'.format(wordCheck, maxl))
            my_list.append(wordCheck)
            maxl = min(len_now - i, maxlen)

        list_Tokenizer.append(' '.join(my_list))
        list_Lines.append(my_list)

    return list_Lines, list_Tokenizer


#  with open('input/data_raw.txt', 'r') as f:
#      data = f.read()
#      lines = data.split('\n')
#  list_Tokens, list_LinesTokens = maximumsMatching(lines)
#  pickle.dump(list_Tokens, open('output/maximumMatching.pkl', 'wb'))
#
#  with open('output/maximumMatching.txt', 'w') as f:
#      for line in list_LinesTokens:
#          f.write(line)
#          f.write('\n')
