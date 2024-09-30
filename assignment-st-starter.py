# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
# show the title
st.title('Titanic App by Zhilan Ding')

# read csv and show the dataframe
df = pd.read_csv('train.csv')
st.subheader('Titanic Dataset')
st.write(df.head(10))
# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below
st.subheader('Box Plot for Ticket Prices by Passenger Class')
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

sns.boxplot(y='Fare', data=df[df['Pclass'] == 1], ax=axes[0])
axes[0].set_xlabel('PClass =  1')
axes[0].set_ylabel('Fare')

sns.boxplot(y='Fare', data=df[df['Pclass'] == 2], ax=axes[1])
axes[1].set_xlabel('PClass  = 2')
axes[1].set_ylabel('Fare')

sns.boxplot(y='Fare', data=df[df['Pclass'] == 3], ax=axes[2])
axes[2].set_xlabel('PClass = 3')
axes[2].set_ylabel('Fare')

st.pyplot(fig)