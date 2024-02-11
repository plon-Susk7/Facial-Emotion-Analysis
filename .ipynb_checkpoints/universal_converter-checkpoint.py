import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict

def dataframe_refiner(df):

    emotion_lst = df['emotions'].unique()
    emotion_lst.sort()
    for emotion in emotion_lst:
        df[emotion] = [0 for i in range(df.shape[0])]
    df['RESULT'] = ['NA' for i in range(df.shape[0])]

    return df

def facs_to_index_converter(column_list):
    
    facs_to_index = defaultdict()

    for index,column_name in enumerate(column_list):
        facs_to_index[column_name.strip()] = index

    return facs_to_index

def emotion_prediction(df,facs_to_index,thresold):
    for index in range(df.shape[0]):

    # We are using AU description as provided in radboud paper

    #This is for nuetral
        if df.iloc[index,facs_to_index['AU01_r']] <= thresold and df.iloc[index,facs_to_index['AU02_r']] <= thresold and df.iloc[index,facs_to_index['AU04_r']] <= thresold and df.iloc[index,facs_to_index['AU05_r']] <= thresold and df.iloc[index,facs_to_index['AU06_r']] <= thresold and df.iloc[index,facs_to_index['AU07_r']] <= thresold and df.iloc[index,facs_to_index['AU09_r']] <= thresold and df.iloc[index,facs_to_index['AU10_r']] <= thresold and df.iloc[index,facs_to_index['AU12_r']] <= thresold and df.iloc[index,facs_to_index['AU14_r']] <= thresold and df.iloc[index,facs_to_index['AU15_r']] <= thresold and df.iloc[index,facs_to_index['AU17_r']] <= thresold and df.iloc[index,facs_to_index['AU20_r']] <= thresold and df.iloc[index,facs_to_index['AU23_r']] <= thresold and df.iloc[index,facs_to_index['AU25_r']] <= thresold and df.iloc[index,facs_to_index['AU26_r']] <= thresold and df.iloc[index,facs_to_index['AU45_r']] <= thresold:
            df.iloc[index,facs_to_index['NUT']] = 1
            if df.iloc[index,facs_to_index['emotions']] == 'NUT':# and df.iloc[index,facs_to_index['RESULT']]=='NA':
                df.iloc[index,facs_to_index['RESULT']] = 'T'
                
            else:
                df.iloc[index,facs_to_index['RESULT']] = 'F'
        
        #This is for angry
        elif df.iloc[index,facs_to_index['AU04_r']] >= thresold and df.iloc[index,facs_to_index['AU05_r']] >= thresold and df.iloc[index,facs_to_index['AU23_r']] >= thresold and df.iloc[index,facs_to_index['AU17_r']] >= thresold and df.iloc[index,facs_to_index['AU07_r']] >= thresold:
            df.iloc[index,facs_to_index['ANG']] = 1 
            if df.iloc[index,facs_to_index['emotions']] == 'ANG':
                df.iloc[index,facs_to_index['RESULT']] = 'T'
                
            else:
                df.iloc[index,facs_to_index['RESULT']] = 'F'
    
            
    
    
        # This is for fearful
        elif df.iloc[index,facs_to_index['AU04_r']] >= thresold and df.iloc[index,facs_to_index['AU01_r']] >= thresold and df.iloc[index,facs_to_index['AU02_r']] >= thresold and df.iloc[index,facs_to_index['AU05_r']] >= thresold and df.iloc[index,facs_to_index['AU25_r']] >= thresold and df.iloc[index,facs_to_index['AU20_r']] >= thresold:
            df.iloc[index,facs_to_index['FER']] = 1
            if df.iloc[index,facs_to_index['emotions']] == 'FER':# and df.iloc[index,facs_to_index['RESULT']]=='NA':
                df.iloc[index,facs_to_index['RESULT']] = 'T'
                
            else:
                df.iloc[index,facs_to_index['RESULT']] = 'F'
            
        # This is for sad
        elif df.iloc[index,facs_to_index['AU04_r']] >= thresold and df.iloc[index,facs_to_index['AU01_r']] >= thresold and df.iloc[index,facs_to_index['AU15_r']] >= thresold and df.iloc[index,facs_to_index['AU17_r']] >= thresold:
            df.iloc[index,facs_to_index['SAD']] = 1
            if df.iloc[index,facs_to_index['emotions']] == 'SAD':# and df.iloc[index,facs_to_index['RESULT']]=='NA':
                df.iloc[index,facs_to_index['RESULT']] = 'T'
                
            else:
                df.iloc[index,facs_to_index['RESULT']] = 'F'
            
        # This is for surprised
        elif df.iloc[index,facs_to_index['AU01_r']] >= thresold and df.iloc[index,facs_to_index['AU05_r']] >= thresold and df.iloc[index,facs_to_index['AU02_r']] >= thresold and df.iloc[index,facs_to_index['AU26_r']] >= thresold:
            df.iloc[index,facs_to_index['SUR']] = 1
            if df.iloc[index,facs_to_index['emotions']] == 'SUR':# and df.iloc[index,facs_to_index['RESULT']]=='NA':
                df.iloc[index,facs_to_index['RESULT']] = 'T'
            else:
                df.iloc[index,facs_to_index['RESULT']] = 'F'
            
                
        # This is for Disgusted
        # elif df.iloc[index,facs_to_index['AU09_r']] >= thresold and df.iloc[index,facs_to_index['AU025_r']] >= thresold and df.iloc[index,facs_to_index['AU010_r']] >= thresold:
        #     df.iloc[index,facs_to_index['DIS']] = 1 
        #     if df.iloc[index,facs_to_index['emotions']] == 'DIS':# and df.iloc[index,facs_to_index['RESULT']]=='NA' :
        #         df.iloc[index,facs_to_index['RESULT']] = 'T'
                
        #     else:
        #         df.iloc[index,facs_to_index['RESULT']] = 'F'
            
    
        # This is for Happy
        elif df.iloc[index,facs_to_index['AU06_r']] >= thresold and df.iloc[index,facs_to_index['AU12_r']] >= thresold and df.iloc[index,facs_to_index['AU25_r']] >= thresold:
            df.iloc[index,facs_to_index['HPY']] = 1
            if df.iloc[index,facs_to_index['emotions']] == 'HPY':# and df.iloc[index,facs_to_index['RESULT']]=='NA':
                df.iloc[index,facs_to_index['RESULT']] = 'T'
                
            else:
                df.iloc[index,facs_to_index['RESULT']] = 'F'
            
        # else:
        #     df.iloc[index,facs_to_index['NUT']] = 1
        #     if df.iloc[index,facs_to_index['emotions']] == 'NUT':# and df.iloc[index,facs_to_index['RESULT']]=='NA':
        #         df.iloc[index,facs_to_index['RESULT']] = 'T'
                
        #     else:
        #         df.iloc[index,facs_to_index['RESULT']] = 'F'
    return df

def false_positive_calculator(df,emotion,facs_to_index):

    counter = 0
    for index in range(df.shape[0]):

        if(df.iloc[index,facs_to_index[emotion]]==1 and df.iloc[index,facs_to_index["emotions"]]!=emotion):
            counter+=1
    return counter

def false_negative_calculator(df,emotion,facs_to_index):
    counter = 0
    for index in range(df.shape[0]):

        if(df.iloc[index,facs_to_index[emotion]]!=1 and df.iloc[index,facs_to_index["emotions"]]==emotion):
            counter+=1
    return counter

def true_positive_calculator(df,emotion,facs_to_index):

    counter = 0
    for index in range(df.shape[0]):

        if(df.iloc[index,facs_to_index[emotion]]==1 and df.iloc[index,facs_to_index["emotions"]]==emotion):
            counter+=1
    return counter

if __name__=='__main__':

    print("Enter the file path: ")
    file_path = input()

    print("Enter thresold value: ")
    thres = float(input())

    # Reading the csv file
    df = pd.read_csv(file_path)
    
    emotions = []
    for x in df['filename']:
        emotions.append(x[-7:-4])
    
    df['emotions'] = emotions
    # Appending emotions
    df = dataframe_refiner(df)

    emotion_list = list(df['emotions'].unique())
    
    facs_to_index = facs_to_index_converter(df.columns)

    # Now filling binary values in dataframe

    modified_df = emotion_prediction(df,facs_to_index,thres)

    #printing NA,T and F values
    print(modified_df['RESULT'].value_counts())

    #printing relevant stats
    TP,FP,FN = 0,0,0
    
    for emotion in emotion_list:
        count1 = false_positive_calculator(modified_df, emotion, facs_to_index)
        count2 = true_positive_calculator(modified_df, emotion, facs_to_index)
        count3 = false_negative_calculator(modified_df, emotion, facs_to_index)
    
        FP += count1
        TP+=count2
        FN+=count3
        
        false_positive_rate = count1 
        false_negative_rate = count3 
        true_positive_rate = count2 
    
        print(f"Emotion: {emotion} ({emotion.lower()})")
        print(f"False Positive : {false_positive_rate}")
        print(f"False Negative : {false_negative_rate}")
        print(f"True Positive : {true_positive_rate}")
        print('\n')
    
    precision = TP/(TP+FP)
    recall = TP/(TP+FN)
    print(f"F1 score : {2*precision*recall/(precision+recall)}")


    