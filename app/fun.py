import pandas as pd


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