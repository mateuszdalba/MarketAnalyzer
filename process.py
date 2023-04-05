import pandas as pd
import pickle

def process(path='elektronika.csv'):
    df = pd.read_csv(path)
    price, neg, loc, date_posted = [], [], [], []
    for i,item in df.iterrows():
        #Price
        price.append(df['Price'][i].split('zł')[0])

        #Negotation status
        if (len(df['Price'][i].split('zł')) == 2):
            if ((df['Price'][i].split('zł')[1] == 'do negocjacji')) :
                neg.append('negotiations_yes')
            elif (df['Price'][i].split('zł')[1] == ''):
                neg.append('negotiations_no')
        else:
            neg.append(df['Price'][i][0])

        print(df['Loc_Date'][i])
        #Location & Date
        l = df['Loc_Date'][i].split('-')
        loc.append(l[0])
        date_posted.append(l[1])


    
    df['Price'], df['Nego'], df['date_posted'], df['location'] = price, neg, date_posted, loc

    df.to_pickle("elektronika.pkl")  

    return df


df = process()
print(df)


