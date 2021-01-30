from stanfordnlp.server import CoreNLPClient
'''------------------------------------

* File Name : StandfordCore.py

* Purpose :

* Creation Date : 15-01-2021

* Last Modified : 01:00:10 PM, 30-01-2021

* Created By : Trinh Quang Truong

------------------------------------'''

client = CoreNLPClient(start_server=False)


def printTree(tree):
    ret = tree.value
    if len(tree.child) > 0:
        ret = "(" + ret + " "
        for child in tree.child:
            ret = ret + " " + printTree(child)

        ret = ret + ")"

    #  print(ret)
    return ret


def STParser(text):
    ann = client.annotate(text,
                          properties={
                              'annotators': 'parse',
                              'parse.model': 'VnParser2.ser.gz'
                          })
    sentences = ann.sentence
    try:
        sentence = sentences[0]
        temp = printTree(sentence.parseTree).replace('  ', ' ').replace(
            '(ROOT ', '')[:-1]
        return [temp]
    except:
        return ['[ERROR] ' + text]


#  pickle.dump(list_Sen, open('output/nlp_preds.pkl', 'wb'))
