import re

def getLexicon(path2Lexicon='input/data_gold.txt'):
    '''
        Lay Lexicon bang bieu thuc chinh quy

    '''

    with open(path2Lexicon, 'r') as f:
        
        data = f.read()

    list_Lexicons = re.findall('(\w+\s\w+)', data) 
    
    print(re.findall('(PU\s\W)', data))

    list_Lexicons += re.findall('(PU\s\W)', data)
    return list(set(list_Lexicons))


#  with open("input/Lexicon.txt", 'w') as f:
    #  list_Lexicons = getLexicon()
    #  for lexicon in list_Lexicons:
    #      f.write(lexicon.replace(' ', ' -> '))
#          f.write('\n')

def getLabel(path2Label='input/data_gold.txt'):
    '''
        Lay Label cua tu bang bieu thuc chinh quy

    '''

    pass
