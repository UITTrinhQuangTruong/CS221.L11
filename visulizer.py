import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def countTag(path2Input):
    '''

        Dem so tag trong data

    '''

    with open(path2Input) as f:
        data = f.read().replace('\n', ' ')

    list_Tags = re.findall('[(](\w+)', data)
    
    Tags, counts = np.unique(np.array(list_Tags), return_counts=True)

    x = dict(zip(Tags, counts))
    return {k: v for k, v in sorted(x.items(), key=lambda item: item[1])[::-1]} 

def visulizePlot(path2Input):
    countTags = countTag(path2Input)
#      plt.barh(list(countTags.keys()), list(countTags.values()))
    #  plt.xlabel('Num of Tag')
    #  plt.ylabel("Tag's name")
#      plt.show()
    fig = plt.figure(figsize=(15,8))
    sns.barplot(y=list(countTags.keys()), x=list(countTags.values()), orient='h')
    plt.xlabel('Num of Tags')
    plt.ylabel("Tag's name")
    plt.show()

visulizePlot('input/data_gold.txt')
