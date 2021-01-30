from Tokenizer import maximumMatching


def readGrammar(path2Grammar='input/Grammar.txt'):
    '''
        Doc Grammar co trong thu muc input

        Moi 1 Grammar la 1 dictionary gom X, Y1 va Y2

    '''

    with open(path2Grammar, 'r') as f:
        list_lines = f.read().split('\n')
        list_Grammars = []
        for idx, line in enumerate(list_lines):
            if line.startswith('#') or line == '':
                continue
            list_Words = line.split()
            if len(list_Words) == 4:

                grammar = dict()
                # x -> y1 y2
                grammar['X'] = list_Words[0]
                grammar['Y1'] = list_Words[2]
                grammar['Y2'] = list_Words[3]
                list_Grammars.append(grammar)

            else:
                print('[Grammar] Error at line %d' % (idx + 1))

        return list_Grammars

    print('[Grammar] Error not find Grammar file!!!')
    return []


def readLexicon(path2Lexicon='input/Lexicon.txt'):
    '''
        Doc Lexicon co trong thu muc input

        Moi 1 Lexicon la 1 dictionary gom X va Y

    '''
    with open(path2Lexicon, 'r', encoding='utf-8') as f:
        list_lines = f.read().split('\n')
        list_Lexicons = []
        for idx, line in enumerate(list_lines):
            if line.startswith('#') or line == '':
                continue
            list_Words = line.split()
            if len(list_Words) == 3:

                lexicon = dict()
                # X -> Y
                lexicon['X'] = list_Words[0]
                lexicon['Y'] = list_Words[2]

                list_Lexicons.append(lexicon)

            else:
                print('[Lexicon] Error at line {}'.format(idx + 1))

        return list_Lexicons

    print('[Lexicon] Error not find Lexicon file!!!')
    return []


def readSentence(path2Sentence='input/Sentence.txt'):
    '''
        Doc Sentence tu thu muc input

        Tokenizer theo tung dong
    '''

    with open(path2Sentence, 'r', encoding='utf-8') as f:
        list_Lines = f.read().split('\n')
        #  list_Sentences = maximumsMatching(list_Lines)

    if list_Lines:
        return list_Lines

    print('[Sentence] Error not find Sentence file!!!')
    return []
