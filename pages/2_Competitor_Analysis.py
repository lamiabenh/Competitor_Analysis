import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud


sns.set_style("whitegrid")
st.set_page_config(page_title="Competitors Analysis", page_icon=":bar_chart:", layout="wide")
st.title("Competitors Analysis")

st.write("This page presents a data-driven exploration of mobile applications on the Google Play Store, highlighting key metrics such as user ratings, number of installs, and category trends.")
st.write("##")

if 'data' in st.session_state:
    data = st.session_state.data

    apps = st.sidebar.multiselect("Application filter", data['title'].unique())


    cols = st.columns(2) 
    
    #st.columns([1, 1]) #first column is 1.6 x wider than second
    # col1, inter_cols_pace, col2 = st.columns((x, y, z))

    if apps:
        data = data[data['title'].isin(apps)]
    

    with cols[0]:
        
        # Score Distribution plot
        plt.figure(figsize=(8, 5))
        plt.title("Distribution of Applications' Ratings", fontsize=14, alpha=0.75)
        plt.hist(data['score'].dropna(), bins=10, color='skyblue', alpha=0.7)
        plt.xlabel("Rating Score", fontsize=12, alpha=0.75)
        plt.ylabel("Number of Applications", fontsize=12, alpha=0.75)
        plt.grid(False)
        ax = plt.gca()  # Get current axes
        for spine in ax.spines.values():
            spine.set_visible(False)
        st.pyplot(plt.gcf(), use_container_width=True)  # gcf = get current figure

    
        # # Price Distribution plot
        # labels = ['Free', 'Paid']
        # sizes = data['free'].value_counts().sort_index().tolist()
        # plt.figure(figsize=(5, 5))
        # plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=45, colors=sns.color_palette('viridis'), textprops={'color':"w"})
        # plt.title("Free vs Paid Apps", fontsize=14, alpha=0.75)
        # plt.axis('equal')  # Equal aspect ratio ensures pie is circular.
        # st.pyplot(plt.gcf(), use_container_width=True)

        st.write('##')

        plt.figure(figsize=(8, 5))
        plt.title("Applications Genre", fontsize=14, alpha=0.75)
        data['genre'].value_counts().head(10).plot(kind='barh', color='skyblue')
        plt.title("Top 10 App Genres", fontsize=12, alpha=0.75)
        plt.xlabel("Number of Apps", fontsize=12, alpha=0.75)
        plt.ylabel("Genre", fontsize=12, alpha=0.75)
        plt.grid(False)
        ax = plt.gca()  # Get current axes
        ax.invert_yaxis()
        for spine in ax.spines.values():
            spine.set_visible(False)
        st.pyplot(plt.gcf())  # gcf = get current figure


    with cols[1]:
        data['installs_clean'] = data['installs'].str.replace('[+,]', '', regex=True).astype(float)
        plt.figure(figsize=(8, 6))
        plt.scatter(data['installs_clean'], data['score'], alpha=0.6, s=100, c='skyblue')
        plt.title('App Score vs Installs \n \n', fontsize=15, alpha=0.75)
        plt.xlabel('Number of Installs', fontsize=12, alpha=0.75)
        plt.ylabel('App Score', fontsize=12, alpha=0.75)
        plt.xscale('log')  # Install counts span large values
        plt.grid(True)
        plt.tight_layout()
        st.pyplot(plt.gcf(), use_container_width=True)

        # fig, ax = plt.subplots(figsize=(8, 6))
        # sns.heatmap(data[['score', 'installs_clean']].corr(), annot=True, fmt=".2f",  ax=ax)
        # ax.set_title("Correlation Heatmap of App Features")
        # st.pyplot(plt.gcf(), use_container_width=True)
            
        st.write('###')

        plt.figure(figsize=(8, 5))
        plt.title("Word Cloud of App Descriptions \n ", fontsize=12, alpha=0.75)
        wordcloud = WordCloud(background_color='white', width=800, height=400).generate(data['description'].str.cat(sep=' '))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt.gcf(), use_container_width=True)

else:
    st.warning("No data available. Please run the search on the Results Table page first.")








# # from wordcloud import WordCloud
# import matplotlib.pyplot as plt

# # Create some sample text
# text = 'Fun, fun, awesome, awesome, tubular, astounding, superb, great, amazing, amazing, amazing, amazing'



# # Create and generate a word cloud image:
# wordcloud = WordCloud().generate(text)

# # Display the generated image:
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()
# st.pyplot()
