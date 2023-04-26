import openpyxl
from tokenise import Input,Positives,Negatives,complex_words,pronouns_counts,sentences
# data extraction from websites from data_extraction.py file and the text files are stored in '/extracted_data' directory


#Get the path to the extraction script. the data is already extracted so no need to run the below commented lines.


### if extracted_data folder is missing in your directory run the below commented lines as well ###

# import os
# data_extraction_path = os.path.join(os.path.dirname(__file__), 'data_extraction.py')
# # Execute the extraction script
# exec(open(data_extraction_path).read())



###### get the required parameters scores

for index,id in enumerate(Input):
    pos_score=0
    neg_score=0 
    Words_count=len(Input[id])
    syllables=0
    characters=0
    for word in Input[id]:
        for letter in word:
            characters+=1
            if letter in ['a','e','i','o','u']:
                syllables+=1
        if 'es' in word:
            syllables-=1
        elif 'ed' in word:
            syllables-=1  
        else:
            pass

        try:
            if Positives[word]:
                pos_score+=1
        except:
            try:
                if Negatives[word]:
                    neg_score+=1
            except:
                pass
    polarity_score=(pos_score-neg_score)/((pos_score+neg_score)+0.000001)
    subjectivity_score=(pos_score+neg_score)/(Words_count+0.000001)
    average_sentence_length=Words_count/sentences[id]
    try:
        percentage_complex_words=complex_words[id]/Words_count
    except:
        percentage_complex_words=0
    Fog_index=0.4*(average_sentence_length+percentage_complex_words)
    avg_number_of_words_per_sentence=average_sentence_length
    try:
        syllables_per_word=syllables/Words_count
        average_word_length=characters/Words_count
    except:
        syllables_per_word=0
        average_word_length=0

    # Add the data to the sheet

    # Open the workbook and select the sheet
    wb=openpyxl.load_workbook('output.xlsx')
    sheet = wb.active

    #update data into output.xlsx
    sheet['c'+str(index+2)] = pos_score
    sheet['d'+str(index+2)] = neg_score
    sheet['e'+str(index+2)] = polarity_score
    sheet['f'+str(index+2)] = subjectivity_score
    sheet['g'+str(index+2)] = average_sentence_length
    sheet['h'+str(index+2)] = percentage_complex_words
    sheet['i'+str(index+2)] = Fog_index
    sheet['j'+str(index+2)] = avg_number_of_words_per_sentence
    sheet['k'+str(index+2)] = complex_words[id]
    sheet['l'+str(index+2)] = Words_count
    sheet['m'+str(index+2)] = syllables_per_word
    sheet['n'+str(index+2)] = pronouns_counts[id]
    sheet['o'+str(index+2)] =  average_word_length
    # Save the workbook
    wb.save('output.xlsx')