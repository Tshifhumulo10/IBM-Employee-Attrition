import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.read_csv('file.csv')

st.title("Attrition Prediction")
st.image('Images\Attrition.jpg',use_column_width=True)

st.sidebar.header('Input parameters')

def input_values():
    global data
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
    PerformanceRating=st.sidebar.slider('PerformanceRating', int(data.PerformanceRating.min()), int(data.PerformanceRating.max()), int(data.PerformanceRating.mean()))
    RelationshipSatisfaction=st.sidebar.slider('RelationshipSatisfaction', int(data.RelationshipSatisfaction.min()), int(data.RelationshipSatisfaction.max()), int(data.RelationshipSatisfaction.mean()))
    StockOptionLevel=st.sidebar.slider('StockOptionLevel', int(data.StockOptionLevel.min()),int(data.StockOptionLevel.max()), int(data.StockOptionLevel.mean()))
    TotalWorkingYears=st.sidebar.slider('TotalWorkingYears', int(data.TotalWorkingYears.min()), int(data.TotalWorkingYears.max()), int(data.TotalWorkingYears.mean()))
    TrainingTimesLastYear=st.sidebar.slider('TrainingTimesLastYear', int(data.TrainingTimesLastYear.min()), int(data.TrainingTimesLastYear.max()), int(data.TrainingTimesLastYear.mean()))
    WorkLifeBalance=st.sidebar.slider('WorkLifeBalance', int(data.WorkLifeBalance.min()), int(data.WorkLifeBalance.max()), int(data.WorkLifeBalance.mean()))
    YearsInCurrentRole=st.sidebar.slider('YearsInCurrentRole', int(data.YearsInCurrentRole.min()), int(data.YearsInCurrentRole.max()), int(data.YearsInCurrentRole.mean()))
    YearsSinceLastPromotion=st.sidebar.slider('YearsSinceLastPromotion', int(data.YearsSinceLastPromotion.min()), int(data.YearsSinceLastPromotion.max()), int(data.YearsSinceLastPromotion.mean()))
    BusinessTravel=st.sidebar.slider('BusinessTravel', int(data.BusinessTravel.min()), int(data.BusinessTravel.max()), int(data.BusinessTravel.mean()))
    Department =st.sidebar.slider('Department',int(data.Department.min()), int(data.Department.max()), int(data.Department.mean()))
    EducationField=st.sidebar.slider('EducationField', int(data.EducationField.min()), int(data.EducationField.max()), int(data.EducationField.mean()))
    Gender=st.sidebar.slider('Gender', int(data.Gender.min()), int(data.Gender.max()), int(data.Gender.mean()))
    JobRole=st.sidebar.slider('JobRole', int(data.JobRole.min()),int(data.JobRole.max()), int(data.JobRole.mean()))
    OverTime=st.sidebar.slider('OverTime', int(data.OverTime.min()), int(data.OverTime.max()), int(data.OverTime.mean()))
    MaritalStatus=st.sidebar.slider('MaritalStatus', int(data.MaritalStatus.min()), int(data.MaritalStatus.max()), int(data.MaritalStatus.mean()))
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
DF=input_values()

st.subheader('Specified input parameters')
st.write(DF)