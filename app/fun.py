import pandas as pd
import string
from itertools import groupby 


def next_letter(df, *letter):
    #Create df with letters as an index
    df_words= df.loc[letter]
    #Get new row with total letters appears
    total = df_words.sum()
    total.name = 'total'
    # Assign sum of all rows of DataFrame as a new Row
    df_words = df_words.append(total.transpose())
    vowels=["a","e", "i", "o", "u"]
    #Delete vowels and letters from columns and rows
    remove= list(set(vowels+list(*letter)))
    df_words.drop(*letter, axis=0, inplace=True)
    df_words.drop(remove, axis=1, inplace=True)
    #New column with percentajes for each vowel
    df_words= df_words.T[["total"]]
    df_words['per'] = (df_words.total * 100 / df_words.total.sum()).round(4)
    df_words.sort_values(by="total", ascending=False, inplace= True)
    
    #Get recommended letter
    final_word= df_words.total.idxmax()
    df_words.head()
    if (df_words.iloc[0].per - df_words.iloc[1].per) < 1:
        return f'You should choose {final_word} with {df_words.loc[final_word].per.round(3)}% appear or {df_words.iloc[1].name} with {df_words.loc[df_words.iloc[1].name].per.round(3)}% appear'
    else:
        return f'You should choose {final_word} with a {df_words.loc[final_word].per.round(3)}% appear'


def next_vowel(df,*vowel):
    
    #Create df with letters as an index
    df_vowel= df.loc[vowel]
    
    #Get new row with total letters appears    
    total = df_vowel.sum()
    total.name = 'total'
    # Assign sum of all rows of DataFrame as a new Row
    vowels=["a","e", "i", "o", "u"]
    vowels= [i for i in vowels if i not in list(*vowel)]
    df_vowel = df_vowel.append(total.transpose())
    df_vowel = df_vowel[[*vowels]].T[["total"]]
    #New column with percentajes for each vowel
    df_vowel['per'] = (df_vowel.total * 100 / df_vowel.total.sum()).round(4)
    df_vowel.sort_values(by="total", ascending=False, inplace= True)
    
    #Get recommended vowel
    final_vowel= df_vowel.total.idxmax()
    df_vowel.head()
    if (df_vowel.iloc[0].per - df_vowel.iloc[1].per) < 1:
        return f'You should choose {final_vowel} with {df_vowel.loc[final_vowel].per.round(3)}% appear or {df_vowel.iloc[1].name} with {df_vowel.loc[df_vowel.iloc[1].name].per.round(3)}% appear'
    else:
        return f'You should choose {final_vowel} with a {df_vowel.loc[final_vowel].per.round(3)}% appear'

def clean_data_letter(df, *letter):
    #Create df with letters as an index
    df_words= df.loc[letter]
    #Get new row with total letters appears
    total = df_words.sum()
    total.name = 'total'
    # Assign sum of all rows of DataFrame as a new Row
    df_words = df_words.append(total.transpose())
    vowels=["a","e", "i", "o", "u"]
    #Delete vowels and letters from columns and rows
    remove= list(set(vowels+list(*letter)))
    df_words.drop(*letter, axis=0, inplace=True)
    df_words.drop(remove, axis=1, inplace=True)
    #New column with percentajes for each vowel
    df_words= df_words.T[["total"]]
    df_words['per'] = (df_words.total * 100 / df_words.total.sum()).round(4).astype(str) + '%'
    df_words.sort_values(by="total", ascending=False, inplace= True)
    
    #Get recommended letter
    final_word= df_words.total.idxmax()
    return df_words

def clean_data_vowel(df, *vowel):
    
    #Create df with letters as an index
    df_vowel= df.loc[vowel]
    
    #Get new row with total letters appears    
    total = df_vowel.sum()
    total.name = 'total'
    # Assign sum of all rows of DataFrame as a new Row
    vowels=["a","e", "i", "o", "u"]
    vowels= [i for i in vowels if i not in list(*vowel)]
    df_vowel = df_vowel.append(total.transpose())
    df_vowel = df_vowel[[*vowels]].T[["total"]]
    #New column with percentajes for each vowel
    df_vowel['per'] = (df_vowel.total * 100 / df_vowel.total.sum()).round(4).astype(str) + '%'
    df_vowel.sort_values(by="total", ascending=False, inplace= True)
    
    #Get recommended vowel
    final_vowel= df_vowel.total.idxmax()
    return df_vowel

def empty_panel(df):
    return f'You should choose {df.iloc[0].name}, {df.iloc[1].name} , {df.iloc[2].name}, {df.iloc[3].name} or  {df.iloc[4].name}'

def empty_consonant(dic, letters):
    dic=list(dic.keys())
    total= dict.fromkeys(string.ascii_lowercase, 0)
    total["-"]=0
    dic = [ele for ele in dic if all(ch not in ele for ch in letters)] 
    for i in dic:
        for x in i:
            total[x]+=1
    df = pd.DataFrame.from_dict(total, orient ='index', columns=["total"])
    df.index.name = "letter"
    df.sort_values(by=['total'], ascending=False, inplace=True)
    vowels=["a","e", "i", "o", "u"]
    df.drop(vowels, axis=0, inplace=True)
    df['per'] = (df.total * 100 / df.total.sum()).round(2)
    final= df.total.idxmax()
    if (df.iloc[0].per - df.iloc[1].per) < 1:
        return f'You should choose {final} with {df.loc[final].per.round(3)}% appear or {df.iloc[1].name} with {df.loc[df.iloc[1].name].per.round(3)}% appear'
    else:
        return f'You should choose {final} with a {df.loc[final].per.round(3)}% appear'

def empty_vowel(dic, vowel):
    dic=list(dic.keys())
    total= dict.fromkeys(string.ascii_lowercase, 0)
    total["-"]=0
    dic = [ele for ele in dic if all(ch not in ele for ch in vowel)] 
    for i in dic:
        for x in i:
            total[x]+=1
    vowels=["a","e", "i", "o", "u"]
    df = pd.DataFrame.from_dict(total, orient ='index', columns=["total"]).loc[vowels]
    df.index.name = "letter"
    df.sort_values(by=['total'], ascending=False, inplace=True)
    df['per'] = (df.total * 100 / df.total.sum()).round(2)
    final= df.total.idxmax()
    if (df.iloc[0].per - df.iloc[1].per) < 1:
        return f'You should choose {final} with {df.loc[final].per.round(3)}% appear or {df.iloc[1].name} with {df.loc[df.iloc[1].name].per.round(3)}% appear'
    else:
        return f'You should choose {final} with a {df.loc[final].per.round(3)}% appear'

def clean_empty_consonant(dic, letters):
    dic=list(dic.keys())
    total= dict.fromkeys(string.ascii_lowercase, 0)
    total["-"]=0
    dic = [ele for ele in dic if all(ch not in ele for ch in letters)] 
    for i in dic:
        for x in i:
            total[x]+=1
    df = pd.DataFrame.from_dict(total, orient ='index', columns=["total"])
    df.index.name = "letter"
    df.sort_values(by=['total'], ascending=False, inplace=True)
    vowels=["a","e", "i", "o", "u"]
    df.drop(vowels, axis=0, inplace=True)
    df['per'] = (df.total * 100 / df.total.sum()).round(2).astype(str) + '%'
    return df
    
def clean_empty_vowel(dic, vowel):
    dic=list(dic.keys())
    total= dict.fromkeys(string.ascii_lowercase, 0)
    total["-"]=0
    dic = [ele for ele in dic if all(ch not in ele for ch in vowel)] 
    for i in dic:
        for x in i:
            total[x]+=1
    vowels=["a","e", "i", "o", "u"]
    df = pd.DataFrame.from_dict(total, orient ='index', columns=["total"]).loc[vowels]
    df.index.name = "letter"
    df.sort_values(by=['total'], ascending=False, inplace=True)
    df['per'] = (df.total * 100 / df.total.sum()).round(2).astype(str) + '%'
    return df
