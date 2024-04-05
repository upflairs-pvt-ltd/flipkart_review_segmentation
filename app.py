import streamlit as st 
import numpy as np 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentiment_analyzer = SentimentIntensityAnalyzer()
def filter_prob(neg,pos,neu):
    if neg>pos and neg>neu:
        st.header("You have Negative Review 😥")
    elif pos>neg and pos>neu:
        st.header("You have a Positive Review 😍")
    elif neu>neg and neu>pos:
        st.header("You have a Neutral Review 😐🤔 ")
    else:
        st.header(" No idea ")

    
st.header("Flipkart Review Segmentation app")
st.subheader('Past review and find the positive or negative review')
input_text1 = st.text_input('Past Review Header',key='input_text1')
input_text2 = st.text_input('Plz paste your review',key='input_text2')
input_text3 = input_text1+" "+input_text2
submit = st.button("submit")
if submit:
    score = sentiment_analyzer.polarity_scores(input_text3)
    filter_prob(score['neg'],score['pos'],score['neu'])

