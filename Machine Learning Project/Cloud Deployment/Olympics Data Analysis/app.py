import  pandas as pd
import streamlit as st
import  preprocessor,helper
import plotly.express as px
import  matplotlib.pyplot as plt
import scipy
import  seaborn as sns   
import plotly.figure_factory as ff
df=pd.read_csv("athlete_events.csv")
region_df=pd.read_csv("noc_regions.csv")
df=preprocessor.preprocess(df,region_df)
st.sidebar.title("Olympics Analysis")


user_menu=st.sidebar.radio(

    "select an option",
    ("Medal Tally","Overall Analysis","Country-Wise Analysis","Athlete Wise Analysis")
)
#Basic Header Info
#st.dataframe(df)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year",years)
    selected_country = st.sidebar.selectbox("Select Country", country)


    medal_tally=helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_year=="Overall" and selected_country=="Overall":
        st.title("Overall Tally")
    if selected_year!= "Overall" and selected_country=="Overall":
        st.title("Medal Tally in "+str(selected_year)+" Oplympics")
    if selected_year == "Overall" and selected_country !="Overall":
        st.title(selected_country +" Overall Performance")
    if selected_year != "Overall" and selected_country !="Overall":
        st.title(selected_country + " Performance in "+str(selected_year)+" Olympics")


    st.table(medal_tally)


if user_menu=="Overall Analysis":
    editions=df['Year'].unique().shape[0]-1
    cities=df["City"].unique().shape[0]
    sports=df["Sport"].unique().shape[0]
    events=df["Event"].unique().shape[0]
    athletes = df["Name"].unique().shape[0]
    nations=df["region"].unique().shape[0]

    st.title("Top Statistics")

    col1,col2,col3=st.beta_columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Host")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1,col2,col3=st.beta_columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Atheletes")
        st.title(athletes)

    nations_over_time=helper.data_over_time(df,"region")
    fig = px.line(nations_over_time, x="Edition", y="region")
    st.title("Participating Nations Over the Years")
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df, "Event")
    fig = px.line(events_over_time, x="Edition", y="Event")
    st.title("Events Over the Years")
    st.plotly_chart(fig)

    athletes_over_time = helper.data_over_time(df, "Name")
    fig = px.line(athletes_over_time, x="Edition", y="Name")
    st.title("athletes Over the Years")
    st.plotly_chart(fig)

    st.title("No of Events (Every Sport)")
    fig,ax=plt.subplots(figsize=(25,20))
    x = df.drop_duplicates(["Year", "Sport", "Event"])
    ax=sns.heatmap(x.pivot_table(index="Sport", columns="Year", values="Event", aggfunc='count').fillna(0).astype("int"),
                annot=True
                )
    st.pyplot(fig)


    # st.title("Most Succssful Athletes")
    # sport_list=df["Sport"].unique().tolist()
    # sport_list.sort()
    # sport_list.insert(0,"Overall")
    #
    #
    # selected_sport=st.selectbox("Select a Sport",sport_list)
    # x=helper.most_succesful(df,selected_sport)
    # st.table(x)
    st.title("Most Successful Athletes")
    sport_list=df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')
    selected_sport=st.selectbox("Select a Sport",sport_list)
    x=helper.most_succesful(df,selected_sport)
    st.table(x)


if user_menu=="Country-Wise Analysis":
    st.sidebar.title("Country-Wise Analysis")
    country_list=df["region"].dropna().unique().tolist()
    country_list.sort()
    country_list.insert(0, 'None')
    selected_country=st.sidebar.selectbox("Select a Country",country_list)

    country_df=helper.yearwise_medal_tally(df,selected_country)
    fig=px.line(country_df,x="Year",y="Medal")
    st.title(selected_country+" Medal Tally Over Year")
    st.plotly_chart(fig)

    st.title(selected_country + " excels in the follwing years")
    pt = helper.country_event_heatmap(df, selected_country)
    fig, ax = plt.subplots(figsize=(25, 20))
    ax=sns.heatmap(pt,annot=True)
    st.pyplot(fig)

    st.title("Top 10 Athletes of Country")
    top10_df=helper.most_succesful_countrywise(df,selected_country)
    st.table(top10_df)

if user_menu=="Athlete Wise Analysis":
    st.title("Distribution of Age ")
    athlete_df = df.drop_duplicates(subset=["Name", "region"])
    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()
    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
                             show_hist=False, show_rug=False)
    fig.update_layout(autosize=False,width=700,height=350)
    st.plotly_chart(fig)

    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)
    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=800,height=850)
    st.title("Distribution of Age wrt Sports(Gold Medalist)")
    st.plotly_chart(fig)
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    temp_df=helper.weight_v_height(df,selected_sport)
    fig,ax=plt.subplots()
    ax = sns.scatterplot(x=temp_df["Weight"],y=temp_df["Height"],hue=temp_df["Medal"],style=temp_df["Sex"],s=100)
    st.title("Height vs Weight")
    st.pyplot(fig) 

    st.title("Men Vs Women Participation Over the Years")
    final = helper.men_vs_women(df)
    fig = px.line(final, x="Year", y=["Male", "Female"])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)