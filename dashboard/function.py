import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def barChart(data,x,y,hue,palette,title,xlabel,ylabel):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data, x=x, y=y,hue=hue, palette=palette, legend=False)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    st.pyplot(plt)

def linePlot (data,x,y,hue,title,palette=None):
    plt.figure(figsize=(10,6))
    sns.lineplot(data=data, x=x, y=y, hue=hue, marker='o', palette=palette)
    plt.title(title)
    plt.xticks(ticks=range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.legend(title='Year')
    plt.grid(True)
    st.pyplot(plt)