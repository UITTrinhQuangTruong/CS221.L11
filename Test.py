from Tokenizer import maximumMatching

def testToken(path2Raw='input/data_raw.txt'):
    '''
        Test thuat toan tach tu maximum Matching

    '''

    with open(path2Raw, 'r') as f:
        data = f.read()
        list_Lines = data.split('\n')

    list_Tokens = maximumMatching(list_Lines)
    with open('output/result_Token.txt', 'w') as f:
        for line in list_Tokens:
            f.write(line)
            f.write('\n')
    
    with open('input/data_tokenizer.txt', 'r') as f:
        data_gold = f.read()
        list_Golds = data_gold.split('\n')

    ave = 0
    for idx in range(len(list_Tokens)):
        num_words = len(list_Golds[idx].split())
        num_gold = list_Golds[idx].count('_')    
        num_token = list_Tokens[idx].count('_')
        
        sub = abs(num_gold - num_token)
        ave += (num_words - 2*sub)/num_words
        print(idx + 1, (num_words - 2*sub)/num_words)

    ave /= len(list_Tokens)
    return ave

print(testToken())

