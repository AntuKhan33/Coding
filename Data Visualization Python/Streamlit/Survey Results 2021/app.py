import pandas as pd 
import streamlit as st 
import plotly.express as px
from PIL import Image
from streamlit_autorefresh import st_autorefresh
st.set_page_config(page_title="Survey_Results")
st.header("Survey_Results 2021")
st.subheader("Hello")


excel_file='Survey_Results.xlsx'
sheet_name="DATA" 

df=pd.read_excel(excel_file,sheet_name=sheet_name,usecols='B:D',header=3)
df_participants=pd.read_excel(excel_file,sheet_name=sheet_name,usecols="F:G",header=3)

df_participants.dropna(inplace=True)

department = df['Department'].unique().tolist()
ages = df['Age'].unique().tolist()



age_selection=st.slider("Age:",
                        min_value=min(ages),
                        max_value=max(ages),
                        value=(min(ages),max(ages) ))


department_selection=st.multiselect("Department:",department,default=department)

mask=(df["Age"].between(*age_selection)) & (df['Department'].isin(department_selection))
number_of_result=df[mask].shape[0]
st.markdown(f'* Available Results: {number_of_result}')


df_grouped=df[mask].groupby(by=["Rating"]).count()[["Age"]]
df_grouped=df_grouped.rename(columns={"Age":"Votes"})
df_grouped = df_grouped.reset_index()


bar_chart = px.bar(df_grouped,
                   x='Rating',
                   y='Votes',
                   text='Votes',
                   color_discrete_sequence = ['#F63366']*len(df_grouped),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)


col1,col2=st.columns(2)
col1.dataframe(df)
col2.dataframe(df_participants)


pie_chart = px.pie(df_participants,
                title="Total No of Participant",
                names='Departments',
                values="Participants"
                
                )

st.plotly_chart(pie_chart)

bar_chart = px.bar(df_participants, x='Departments', y='Participants',title="Total No of Participant",color="Departments")

st.plotly_chart(bar_chart)
# image=Image.open('My project-1 copy.jpg')
# st.image(image,caption="Designed by nazis",use_column_width=True)











# st.set_page_config(page_title="Survey_Results")
# st.header("Survey_Results 2021")
# st.subheader("Hello")

# excel_file="Survey_Results.xlsx"
# sheet_name="DATA"

# df=pd.read_excel(excel_file,sheet_name=sheet_name,usecols="B:D",header=3)
# df_participants=pd.read_excel(excel_file,sheet_name=sheet_name,usecols="F:G",header=3)

# df_participants.dropna(inplace=True)
# department = df['Department'].unique().tolist()
# ages = df['Age'].unique().tolist()

# age_selection=st.slider("Age:",min_value=min(ages),max_value=max(ages),value=(min(ages),max(ages)))

# department_selection=st.multiselect("Department: ",department,default=department)

# mask=(df["Age"].between(*age_selection)) & (df ["Department"].isin(department_selection))
# number_of_result=df[mask].shape[0]
# st.markdown(f"Available Results: {number_of_result}")

# df_grouped=df[mask].groupby(by=['Rating']).count()[["Age"]]
# df_grouped=df_grouped.rename(columns={"Age":"Votes"})
# df_grouped=df_grouped.reset_index()
# bar_chart = px.bar(df_grouped,
#                    x='Rating',
#                    y='Votes',
#                    text='Votes',
#                    color_discrete_sequence = ['#F63366']*len(df_grouped),
#                    template= 'plotly_white')
# st.plotly_chart(bar_chart)

# col1,col2=st.columns(2)
# col1.dataframe(df)
# col2.dataframe(df_participants)



# pie_chart=px.pie(df_participants,title="Total No of Participants",values="Participants",names="Departments")
# st.plotly_chart(pie_chart)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .css-1rs6os {visibility: hidden;}
            .css-17ziqus {visibility: hidden;}
            """
st.markdown(hide_st_style,unsafe_allow_html=True)


# pie_chart=px.pie(df_participants,title="Total No of Participants",
#                  values="Participants",names="Departments")

# st.plotly_chart(pie_chart)