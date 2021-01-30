from ckyIO import readGrammar, readLexicon, readSentence


def parseLexicon(list_Words, lenSentence, TABLE, lexicon):
    '''
        Tim Lexicon cho moi tu trong list_Words

        Tra ve True neu tim duoc tat ca cac Lexicon cua tung tu
        Nguoc lai, tra ve False

    '''

    # Doc file Lexicon
    if lexicon:
        list_Lexicons = readLexicon(lexicon)
    else:
        list_Lexicons = readLexicon()
    # print(lenSentence)
    for i in range(lenSentence):
        count_Word = 0
        # print(list_Words[i])
        for j in range(len(list_Lexicons)):
            # print(list_Lexicons[j])
            if list_Words[i] == list_Lexicons[j]['Y']:
                #print(list_Words[i], list_Lexicons[j]['X'])
                TABLE[i][i].append({
                    ((i, i), (i, i), None, None):
                    list_Lexicons[j]
                })
                count_Word += 1
                #  print('LEXICON', i)
                #  print(TABLE[i][i])
        if count_Word == 0:
            return False

    return True


def parseGrammar(list_Words, lenSentence, TABLE, grammar):
    '''

    Tim Grammar

    '''

    if grammar:
        list_Grammars = readGrammar(grammar)
    else:
        list_Grammars = readGrammar()
    #  print(list_Grammars)
    #  print(lenSentence)
    for j in range(1, lenSentence):
        for i in range(j - 1, -1, -1):
            for k in range(0, j - i):
                if len(TABLE[i][i + k]) != 0 and len(TABLE[i + 1 + k][j]) != 0:
                    #  print(TABLE[i][i+k], TABLE[i+1+k][j])
                    for u in range(0, len(TABLE[i][i + k])):
                        Y1 = list(TABLE[i][i + k][u].values())[0]['X']
                        for v in range(0, len(TABLE[i + 1 + k][j])):
                            Y2 = list(TABLE[i + 1 + k][j][v].values())[0]['X']
                            for t in range(0, len(list_Grammars)):
                                if ((Y1 == list_Grammars[t]['Y1'])
                                        and (Y2 == list_Grammars[t]['Y2'])):
                                    TABLE[i][j].append({
                                        ((i, i + k), (i + 1 + k, j), u, v):
                                        list_Grammars[t]
                                    })
                                    #  if j == 12:
                                    #  print(list_Grammars[t]['X'], i, t)


def checkTree(lenSentence, TABLE):
    if len(TABLE[0][lenSentence - 1]) == 0:
        return False

    num_Trees = 0
    for i in range(0, len(TABLE[0][lenSentence - 1])):
        if (list(TABLE[0][lenSentence - 1][i].values())[0]['X'] == 'S'):
            num_Trees += 1

    if num_Trees > 0:
        return True
    return False


def trackingTree(TABLE, start):
    tree = []
    ih = list(start.keys())[0][0][0]  # Horizontal
    jh = list(start.keys())[0][0][1]
    iv = list(start.keys())[0][1][0]  # Vertical
    jv = list(start.keys())[0][1][1]

    # Truong hop ra 1 Lexicon
    if (ih == jh == iv == jv):
        tree.append('(')
        tree.append(list(start.values())[0]['X'])
        tree.append(' ')
        tree.append(list(start.values())[0]['Y'])
        tree.append(')')

    # Truong hop ra Grammar
    else:
        tree.append('(')
        tree.append(list(start.values())[0]['X'])
        tree.append(
            trackingTree(
                TABLE, TABLE[list(start.keys())[0][0][0]][list(
                    start.keys())[0][0][1]][list(start.keys())[0][2]]))
        tree.append(
            trackingTree(
                TABLE, TABLE[list(start.keys())[0][1][0]][list(
                    start.keys())[0][1][1]][list(start.keys())[0][3]]))
        tree.append(')')
    return tree


def rebuiltResult(list_trees):
    '''

        De quy de lay lai ket qua

    '''
    string = ''
    #  print(list_trees)
    for i in list_trees:
        try:
            string = string + i
        except:
            string = string + rebuiltResult(i)
    return string


def printTable(lenSentence, TABLE):
    # Print Table
    for i in range(0, lenSentence):
        print("----------------------------- ")
        for j in range(0, lenSentence):
            if j >= i:
                for k in range(0, len(TABLE[i][j])):
                    print('Row %d\t Column ' % i, j,
                          list(TABLE[i][j][k].values())[0]['X'])


def syntacticAnalyzer(sentence, lexicon, grammar):
    '''
        Xay dung cay cu phap tu 1 sentence

    '''

    # Lay danh sach tu trong 1 sentence
    list_Words = sentence.split()
    # Lay do dai cua cau
    lenSentence = len(list_Words)
    # Dinh nghia Table CKY
    TABLE = [[[] for i in range(lenSentence)] for j in range(lenSentence)]

    # Kiem tra Lexicon
    checkParse = parseLexicon(list_Words, lenSentence, TABLE, lexicon)

    #  printTable(lenSentence, TABLE)

    list_Results = []
    if checkParse:
        # parse grammar
        parseGrammar(list_Words, lenSentence, TABLE, grammar)

        #  printTable(lenSentence, TABLE)
        if checkTree(lenSentence, TABLE):
            for i in range(0, len(TABLE[0][lenSentence - 1])):
                if (list(TABLE[0][lenSentence -
                                  1][i].values())[0]['X'] == 'S'):
                    result = rebuiltResult(
                        trackingTree(TABLE, TABLE[0][lenSentence - 1][i]))
                    #  printTable(lenSentence, TABLE)
                    #result = '(ROOT'+result+')'
                    list_Results.append(result)

        else:

            # Loi khong phan tich duoc cay cu phap
            result = '[ERROR 1] %s' % sentence
            #  printTable(lenSentence, TABLE)
            return [result]
    else:
        # Loi khong dien het duoc Lexicon
        result = '[ERROR 2] %s' % sentence
        #  print(result)
        return [result]
    return list_Results


