from CKY import syntacticAnalyzer
from ckyIO import readSentence
from Tokenizer import maximumMatching
from Vncore import wordTokenzizer
from StandfordCore import STParser
'''------------------------------------

* File Name : ParserModel.py

* Purpose :

* Creation Date : 20-12-2020

* Last Modified : 12:23:05 PM, 30-01-2021

* Created By : Trinh Quang Truong

------------------------------------'''


def Parser(intk, Input, Output, lexicon, grammar, TypeTokenizer, ParserModel,
           TypeOuput):
    s = 0
    if intk:
        n = int(input('Nhap n'))
        list_Sentences = []
        for i in range(n):
            list_Sentences.append(input())
    else:
        if Input:
            list_Sentences = readSentence(Input)
        else:
            list_Sentences = readSentence()

    list_Results = []
    for idx, sentence in enumerate(list_Sentences):
        # Tach tu
        if TypeTokenizer:
            sentence = wordTokenzizer(sentence)
        else:
            sentence = maximumMatching(sentence)

        # Parser
        if ParserModel:
            result = STParser(sentence)
        else:
            result = syntacticAnalyzer(sentence, lexicon, grammar)

        try:
            if TypeOuput:
                list_Results.append(result)
            else:
                list_Results.append([result[0]])
        except:
            list_Results.append([])
        if len(result) > 0:
            s += 1
    if Output:
        with open(Output, 'w') as f:
            for i in range(len(list_Sentences)):
                f.write(list_Sentences[i])
                f.write('\n')
                try:
                    f.writelines(list_Results[i])
                except:
                    pass

                f.write('----------------------------------------------\n')
    else:
        for i in range(len(list_Sentences)):
            print('Num: %d| %s' % (i + 1, list_Sentences[i]))
            try:
                for j in list_Results[i]:
                    print(j)
            except:
                print()
            print('----------------------------------------------\n')
