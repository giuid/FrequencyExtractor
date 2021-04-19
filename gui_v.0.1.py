#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 17:28:53 2021

@author: guido
"""
try:
    from tkinter import *
    from tkinter.filedialog import askopenfilename, askdirectory,asksaveasfile
    import pandas as pd
    from pandastable import Table
    from nltk.corpus import stopwords
    from nltk.tokenize import RegexpTokenizer
    import nltk
    import re
    import openpyxl
except:
    import install_dependecies


root = Tk()
root.geometry('+%d+%d'%(350,10))
header = Frame(root, width=800, height=40, bg="white")
header.grid(columnspan=3, rowspan=2, row=0)
main_content = Frame(root, width=800, height=40, bg="#20bebe")
main_content.grid(columnspan=3, rowspan=2, row=4)
table_content = Frame(root, width=800, height=275, bg="white")
table_content.grid(columnspan=3, rowspan=2, row=6)

csv = None 
frequency = None
def open_file():
    browse_text.set("loading...")
    file = askopenfilename(parent=root)
    if file:
        global csv
        if file.endswith(".xls") or file.endswith(".xlsx") :
            csv = pd.read_excel(file)
        elif file.endswith(".csv"):
            csv = pd.read_csv(file, sep=";")
        else:
            print("File format is not supported")
            return
        print ('file loaded' + file)
        browse_text.set("Browse")
        pt = Table(table_content, dataframe=csv,showtoolbar=True, showstatusbar=True)
        pt.show()   
        freq_text = StringVar()
        freq_btn = Button(root, textvariable=freq_text, command=lambda:calc_frequency(), font=("Raleway",12), bg="#20bebe", fg="white", height=1, width=15)
        freq_text.set("Calculate Frequency")
        freq_btn.grid(column=2, row=5, sticky=NE, padx=50)

    def calc_frequency():
            #stemmer = SnowballStemmer('italian')
            #stop_words = set(stopwords.words('italian'))
            custom_tokenizer = RegexpTokenizer('\w+')   
            
            # dictionary of Italian stop-words
            it_stop_words = nltk.corpus.stopwords.words('italian')
    
            file=csv
            file['Testo'] =  [re.sub(r'\[[^()]*\]','', str(x)) for x in file['Testo']]
            all_words =[]
            for i in range(len(file)):
             
                all_words  += custom_tokenizer.tokenize(file.Testo.iloc[i])
            all_words = [x for x in all_words if x not in it_stop_words]    
            fdist = nltk.FreqDist(all_words)
            
            mostcomm = fdist.most_common(50)
            
            wrd = []
            frq = []
            for el in fdist.most_common():
                wrd.append(el[0])
                frq.append(el[1])
            global frequency
            frequency = pd.DataFrame(list(zip(wrd, frq)), columns= ['Word','Frequency'])
            
            def save_freq():
                global frequency
                path= asksaveasfile(defaultextension='.csv')
                frequency.to_csv(f'{path.name}',index=False, sep = ';')
        
            def show_freq():
                pt = Table(table_content, dataframe=frequency,showtoolbar=True, showstatusbar=True)
                pt.show()  
                show_freq_text.set("Show Original")
                show_freq_btn.configure(command = lambda:show_original())
            
            def show_original():
                pt = Table(table_content, dataframe=csv,showtoolbar=True, showstatusbar=True)
                pt.show()  
                show_freq_text.set("Show Frequency")
                show_freq_btn.configure(command = lambda:show_freq())
            
            
            
            save_freq_text = StringVar()
            save_freq_btn = Button(root, textvariable=save_freq_text, command=lambda:save_freq(), font=("Raleway",12), bg="#20bebe", fg="white", height=1, width=15)
            save_freq_text.set("Save Frequency")
            save_freq_btn.grid(column=1, row=5, sticky=NE, padx=50)
            
            show_freq_text = StringVar()
            show_freq_btn = Button(root, textvariable=show_freq_text, command=lambda:show_freq(), font=("Raleway",12), bg="#20bebe", fg="white", height=1, width=15)
            show_freq_text.set("Show Frequency")
            show_freq_btn.grid(column=0, row=5, sticky=NE, padx=50)
        

    
browse_text = StringVar()
browse_btn = Button(root, textvariable=browse_text, command=lambda:open_file(), font=("Raleway",12), bg="#20bebe", fg="white", height=1, width=15)
browse_text.set("Browse")
browse_btn.grid(column=2, row=1, sticky=NE, padx=50)


root.mainloop()