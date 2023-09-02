import streamlit as st
import pandas as pd
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import plotly.express as px



data = pd.read_csv('file.csv')
train = pd.read_csv('train.csv')
import pickle
# Save the model to a file using pickle
with open('model.pickle', 'rb') as file:
    loaded_model = pickle.load(file)
with open('enc.pickle', 'rb') as file:
    load_encoder= pickle.load(file)
page = st.sidebar.radio("Select Page", ["Overview", "Prediction", "Insights"])


if page == "Overview":
    st.title('Attrition Analysis and Prediction')
    st.image('AttritionApp.jpeg',use_column_width=True)
    st.write('In the dynamic landscape of modern businesses, the departure of employees, known as attrition, presents both challenges and opportunities for organizations. The reasons behind employee attrition are diverse, ranging from tangible factors like unsatisfactory pay and poor workplace conditions to intangible ones such as personal circumstances like illness, loss, and relocation. Understanding and mitigating attrition is a critical endeavor for companies striving to cultivate a motivated, productive, and cohesive workforce.')
    st.write(' ')
    st.write('In my ambitious undertaking, I delve into the realm of human resources analytics to explore the multifaceted nature of employee attrition. Leveraging the rich and comprehensive IBM data, I embarked on a transformative journey of insight discovery and prediction. My aim is twofold: first, to gain a profound understanding of the underlying factors that contribute to attrition within organizations, and second, to develop a powerful predictive model capable of forecasting attrition patterns with remarkable accuracy.')
    
    st.subheader('About the data')
    st.write('The data was downloaded on kaggle: https://www.kaggle.com/datasets/rohitsahoo/employee')
    Education={1:'Below College', 2:'College',  3:'Bachelor', 4:'Master', 5:'Doctor'}
    EnvironmentSatisfaction={1:'Low', 2:'Medium', 2:'High', 3:'Very High'}
    JobInvolvement={1:'Low', 2:'Medium', 3: 'High', 4 :'Very High'}
    JobSatisfaction={1:'Low', 2:'Medium', 3:'High', 4:'Very High'}
    PerformanceRating={1:'Low', 2:'Good', 3: 'Excellent', 4: 'Outstanding'}
    RelationshipSatisfaction= {1:'Low', 2:'Medium', 3:'High', 4:'Very High'}
    WorkLifeBalance= {1:'Bad', 2:'Good', 3:'Better', 4:'Best'}
    Attrition={0:"No", 1: "Yes"}

                     
    st.write('Education')
    with st.expander('Click here to read more'):
            st.write(pd.DataFrame(list(Education.items()), columns=['Code', 'Education Level']))
    st.write('Environment Satisfaction ')
    with st.expander('Click here to read more'):
            st.write(pd.DataFrame(list(EnvironmentSatisfaction.items()), columns=['Code', 'Environment Satisfaction']))
    st.write('Job Involvement')
    with st.expander('Click here to read more'):
            st.write(pd.DataFrame(list(JobInvolvement.items()), columns=['Code', 'Job Involvement Level']))
    st.write('Job Satisfaction')
    with st.expander('Click here to read more'):
            st.write(pd.DataFrame(list(JobSatisfaction.items()), columns=['Code', 'Job Satisfaction Level']))
    st.write('Performance Rating')
    with st.expander('Click here to read more'):
            st.write(pd.DataFrame(list(PerformanceRating.items()), columns=['Code', 'Performance Rating']))
    st.write('Relationship Satisfaction')
    with st.expander('Click here to read more'):
            st.write(pd.DataFrame(list(RelationshipSatisfaction.items()), columns=['Code', 'Relationship Satisfaction']))
    st.write('WorkLife Balance')
    with st.expander('Click here to read more'):
            st.write(pd.DataFrame(list(WorkLifeBalance.items()), columns=['Code', 'Worklife Balance']))
    
    
elif page == "Prediction":
    st.title('Predictions')
    
    st.sidebar.header('Input parameters')
    def input_values():
        global data
        Gender=st.sidebar.selectbox('Gender', ('Female', 'Male'))
        MaritalStatus=st.sidebar.selectbox('MaritalStatus', ('Single', 'Married', 'Divorced'))
        BusinessTravel=st.sidebar.selectbox('BusinessTravel',('Travel_Rarely', 'Travel_Frequently', 'Non-Travel'))
        Department =st.sidebar.selectbox('Department',('Sales', 'Research & Development', 'Human Resources'))
        EducationField=st.sidebar.selectbox('EducationField',('Life Sciences', 'Other', 'Medical', 'Marketing','Technical Degree', 'Human Resources' ))
        JobRole=st.sidebar.selectbox('JobRole', ('Sales Executive', 'Research Scientist', 'Laboratory Technician','Manufacturing Director', 'Healthcare Representative', 'Manager','Sales Representative', 'Research Director', 'Human Resources'))
        OverTime=st.sidebar.selectbox('OverTime', ('Yes', 'No'))
        Age= st.sidebar.slider('Age', int(data.Age.min()), int(data.Age.max()), int(data.Age.mean()))
        DailyRate= st.sidebar.slider('DailyRate', int(data.DailyRate.min()), int(data.DailyRate.max()), int(data.DailyRate.mean()))
        DistanceFromHome=st.sidebar.slider('DistanceFromHome', int(data.DistanceFromHome.min()), int(data.DistanceFromHome.max()), int(data.DistanceFromHome.mean()))
        Education=st.sidebar.slider('Education', int(data.Education.min()),int(data.Education.max()), int(data.Education.mean()))
        EnvironmentSatisfaction=st.sidebar.slider('EnvironmentSatisfaction', int(data.EnvironmentSatisfaction.min()), int(data.EnvironmentSatisfaction.max()), int(data.EnvironmentSatisfaction.mean()))
        HourlyRate=st.sidebar.slider('HourlyRate', int(data.HourlyRate.min()), int(data.HourlyRate.max()), int(data.HourlyRate.mean()))
        JobInvolvement=st.sidebar.slider('JobInvolvement', int(data.JobInvolvement.min()), int(data.JobInvolvement.max()), int(data.JobInvolvement.mean()))
        JobSatisfaction=st.sidebar.slider('JobSatisfaction', int(data.JobSatisfaction.min()), int(data.JobSatisfaction.max()), int(data.JobSatisfaction.mean()))
        MonthlyRate=st.sidebar.slider('MonthlyRate', int(data.MonthlyRate.min()), int(data.MonthlyRate.max()), int(data.MonthlyRate.mean()))
        NumCompaniesWorked=st.sidebar.slider('NumCompaniesWorked', int(data.NumCompaniesWorked.min()), int(data.NumCompaniesWorked.max()), int(data.NumCompaniesWorked.mean()))
        PerformanceRating=st.sidebar.slider('PerformanceRating', 1, 4, 2)
        RelationshipSatisfaction=st.sidebar.slider('RelationshipSatisfaction', int(data.RelationshipSatisfaction.min()), int(data.RelationshipSatisfaction.max()), int(data.RelationshipSatisfaction.mean()))
        StockOptionLevel=st.sidebar.slider('StockOptionLevel', int(data.StockOptionLevel.min()),int(data.StockOptionLevel.max()), int(data.StockOptionLevel.mean()))
        TotalWorkingYears=st.sidebar.slider('TotalWorkingYears', int(data.TotalWorkingYears.min()), int(data.TotalWorkingYears.max()), int(data.TotalWorkingYears.mean()))
        TrainingTimesLastYear=st.sidebar.slider('TrainingTimesLastYear', int(data.TrainingTimesLastYear.min()), int(data.TrainingTimesLastYear.max()), int(data.TrainingTimesLastYear.mean()))
        WorkLifeBalance=st.sidebar.slider('WorkLifeBalance', int(data.WorkLifeBalance.min()), int(data.WorkLifeBalance.max()), int(data.WorkLifeBalance.mean()))
        YearsInCurrentRole=st.sidebar.slider('YearsInCurrentRole', int(data.YearsInCurrentRole.min()), int(data.YearsInCurrentRole.max()), int(data.YearsInCurrentRole.mean()))
        YearsSinceLastPromotion=st.sidebar.slider('YearsSinceLastPromotion', int(data.YearsSinceLastPromotion.min()), int(data.YearsSinceLastPromotion.max()), int(data.YearsSinceLastPromotion.mean()))
        df= {'Age': Age,
            'BusinessTravel': BusinessTravel, 
            'DailyRate': DailyRate,
            'Department': Department, 
            'DistanceFromHome': DistanceFromHome,
            'Education': Education, 
            'EducationField': EducationField, 
            'EnvironmentSatisfaction': EnvironmentSatisfaction,
            'Gender': Gender,
            'HourlyRate': HourlyRate,
            'JobInvolvement': JobInvolvement, 
            'JobRole': JobRole,
            'JobSatisfaction': JobSatisfaction,
            'MaritalStatus': MaritalStatus,
            'MonthlyRate': MonthlyRate, 
            'NumCompaniesWorked': NumCompaniesWorked,
            'OverTime': OverTime,
            'PerformanceRating': PerformanceRating,
            'RelationshipSatisfaction': RelationshipSatisfaction, 
            'StockOptionLevel': StockOptionLevel,
            'TotalWorkingYears': TotalWorkingYears,
            'TrainingTimesLastYear':  TrainingTimesLastYear, 
            'WorkLifeBalance': WorkLifeBalance,
            'YearsInCurrentRole': YearsInCurrentRole,
            'YearsSinceLastPromotion': YearsSinceLastPromotion}
        features=pd.DataFrame(df, index=[0])
        return features
    Df=input_values()

    st.header('Upload data for predictions')
    Data_up =st.file_uploader('Upload CSV using the format of the specified parameters below')
    st.write('---')

    st.header('Specified Input Parameters')
    st.write(Df)
    st.write('---')

    Df[['BusinessTravel','Department','EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'OverTime']]= load_encoder.fit_transform(Df[['BusinessTravel','Department','EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'OverTime']])

    st.header('Predictions')
    if loaded_model.predict(Df) == 1:
        st.write('The employee is predicted to leave the company  \U0001F625')
        st.image("leaving.jpeg",use_column_width=True)
    else:
        st.write('The employee is predicted to stay in the company \U0001F604')
        st.image("staying.jpeg",use_column_width=True)
    st.write('---')

    st.header('Data used for Model training')
    st.write(data.head(10))
    st.write('---')
    
elif page == "Insights":
    st.title('INSIGHTS')
    st.image('insights.jpeg',use_column_width=True)

    Attrition = pd.Series(train['Attrition'].value_counts())
    attrition_df = pd.DataFrame({'Count': Attrition.values}, index=Attrition.index)
    fig = px.pie(attrition_df, values='Count', names=attrition_df.index, 
                title='Percentage of Attrition in IBM', 
                color_discrete_sequence=['blue', 'red'],
                labels={'index': 'Attrition'})
    fig.update_traces(textinfo='percent+label', pull=[0, 0.1])
    fig.update_layout(legend_title_text='Attrition', legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1))
    st.plotly_chart(fig)
    st.write('Observation:')
    with st.expander('Click here to read more'):
            st.write('Out of 1058 employees, 16.9%/ of the employees left IBM. Employees leave for various reasons and some factors that contribute to attrition are analysed below.')
        
    Data = pd.crosstab(index=train['Age'].replace('Age'), columns=train['Attrition'], normalize=False)
    Data = Data.reset_index()
    fig = px.line(Data, x='Age', y=[0, 1], title="Relationship between Age and Attrition", labels={'value': 'Count'})
    fig.update_layout(
        xaxis_title="Age",
        yaxis_title="Count",
        legend_title="Attrition",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
    st.plotly_chart(fig) 
    st.write('Observation:')
    with st.expander('Click here to read more'):
            st.write('Most employees who leaves are on their late twenties and early thirties. In their late twenties and early thirties, many employees are in a stage of their careers where they seek rapid growth and advancement. Moreover, Younger employees often prioritize skill development and continuous learning to enhance their marketability and expertise.')
    
    No = train[train["Attrition"] == 0]
    Yes = train[train["Attrition"] == 1]
    fig = px.histogram(train, x="MonthlyIncome", color="Attrition",
                    title="Distribution of Monthly Income for Attrition",
                    marginal="rug",  
                    color_discrete_sequence=["red", "blue"],
                    opacity=0.7,
                    labels={"MonthlyIncome": "Monthly Income", "Attrition": "Attrition"})
    fig.update_layout(barmode="overlay") 
    fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
    fig.update_yaxes(showline=True, linewidth=2, linecolor='black')
    st.plotly_chart(fig) 
    st.write('Observation:')
    with st.expander('Click here to read more'):
            st.write("The graph above illustrates that employees who earn less income are prone to leave the company in search for greener pastures compared to those who earn more money. Employees with lower incomes may face greater financial pressures, such as paying bills, supporting their families, or dealing with debt. They may be more inclined to explore higher-paying job opportunities to improve their financial situation. Higher income often correlates with greater job satisfaction, as it can lead to a sense of financial security and recognition for one's contributions.")


    Data = pd.crosstab(index=train['OverTime'].replace('OverTime'), columns=train['Attrition'], normalize=False)
    Data = Data.reset_index()
    fig = px.bar(Data, x='OverTime', y=[0, 1], title="OverTime versus Attrition",
                labels={'value': 'Count', 'OverTime': 'OverTime'},
                color_discrete_sequence=['blue', 'red'],
                opacity=0.7,
                barmode='stack')
    fig.update_layout(
        xaxis_title="OverTime",
        yaxis_title="Count",
        legend_title="Attrition",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
    st.plotly_chart(fig)
    st.write('Observation:')
    with st.expander('Click here to read more'):
            st.write("Despite the majority of employees not working overtime, the attrition rate for those who do work overtime is higher than for those who don't. This means that employees who work additional hours beyond their regular schedules are more likely to leave the organization. One possible explanation for the higher attrition rate among employees who work a lot of overtime is a poor work-life balance.Employees who consistently work overtime might feel overworked or underappreciated for their efforts.")
        




            
