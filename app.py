import pandas as pd
import streamlit as st
#import joblib
from analysis import logreg, feature_names

#@st.cache_resource
#def load_model():
#    return joblib.load('model.pkl')

#model = load_model()

st.title('Streamlit Checkpoint 2')
st.write('Please input the following parameters and confirm. Based on the trained model, this application will classify whether a bank account is used or not.')

country = st.selectbox("Country:", ['Rwanda', 'Tanzania', 'Kenya', 'Uganda'])
year = float(st.number_input("Enter the year"))
location_type = st.selectbox("Location Type:", ['Rural', 'Urban'])
cellphone_access = st.checkbox("Cell Phone Access?")
household_size = float(st.number_input("Enter the household size"))
age_of_respondent = float(st.number_input("Enter the age"))
gender_of_respondent = st.radio("Gender:", ['Male', 'Female'])
relationship_with_head = st.selectbox("Relationship with head of famiily:", ['Head of Household', 'Spouse', 'Child', 'Parent', 'Other relative', 'Other non-relatives'])
marital_status = st.selectbox("Marital Status:", ['Married/Living together', 'Single/Never Married', 'Widowed', 'Divorced/Seperated', 'Dont know'])
education_level = st.selectbox("Education Level:", ['Primary education', 'No formal education', 'Secondary education', 'Tertiary education', 'Vocational/Specialised training', 'Other/Dont know/RTA'])
job_type = st.selectbox("Job Type:", ['Self employed', 'Informally employed', 'Farming and Fishing', 'Tertiaation', 'Remittance Dependent', 'Other Income', 'Formally employed Private', 'No Income', 'Formally employed Government', 'Government Dependent', 'Dont Know/Refuse to answer'])


     
if(st.button("Classify if Bank Account is used or not")):
    # data = pd.DataFrame({
    #                     'country_Kenya': lambda: 1.0 if country == 'Kenya' else 0.0,                             
    #                     'country_Rwanda': lambda: 1.0 if country == 'Rwanda' else 0.0,                            
    #                     'country_Tanzania': lambda: 1.0 if country == 'Tanzania' else 0.0,                          
    #                     'country_Uganda':  lambda: 1.0 if country == 'Uganda' else 0.0,

    #                     'year': year,                            
    #                     'location_type': lambda: 1.0 if location_type == 'Urban' else 0.0,                            
    #                     'cellphone_access': cellphone_access,                           
    #                     'household_size': household_size,     
    #                     'age_of_respondent': age_of_respondent,             
    #                     'gender_of_respondent': lambda: 1.0 if gender_of_respondent == 'Male' else 0.0,

    #                     'marital_status_Divorced/Seperated': lambda: 1.0 if marital_status == 'Divorced/Seperated' else 0.0,         
    #                     'marital_status_Dont know': lambda: 1.0 if marital_status == 'Dont know' else 0.0,                    
    #                     'marital_status_Married/Living together': lambda: 1.0 if marital_status == 'Married/Living together' else 0.0,      
    #                     'marital_status_Single/Never Married': lambda: 1.0 if marital_status == 'Single/Never Married' else 0.0,         
    #                     'marital_status_Widowed': lambda: 1.0 if marital_status == 'Widowed' else 0.0,  
                    
    #                     'relationship_with_head_Child': lambda: 1.0 if relationship_with_head == 'Child' else 0.0,              
    #                     'relationship_with_head_Head of Household': lambda: 1.0 if relationship_with_head == 'Head of Household' else 0.0,   
    #                     'relationship_with_head_Other non-relatives': lambda: 1.0 if relationship_with_head == 'Other non-relatives' else 0.0, 
    #                     'relationship_with_head_Other relative': lambda: 1.0 if relationship_with_head == 'Other relative' else 0.0,      
    #                     'relationship_with_head_Parent': lambda: 1.0 if relationship_with_head == 'Parent' else 0.0,              
    #                     'relationship_with_head_Spouse': lambda: 1.0 if relationship_with_head == 'Spouse' else 0.0, 

    #                     'education_level_No formal education': lambda: 1.0 if education_level == 'No formal education' else 0.0,        
    #                     'education_level_Other/Dont know/RTA': lambda: 1.0 if education_level == 'Other/Dont know/RTA' else 0.0,       
    #                     'education_level_Primary education': lambda: 1.0 if education_level == 'Primary education' else 0.0,         
    #                     'education_level_Secondary education': lambda: 1.0 if education_level == 'Secondary education' else 0.0,       
    #                     'education_level_Tertiary education':  lambda: 1.0 if education_level == 'Tertiary education' else 0.0,             
    #                     'education_level_Vocational/Specialised training': lambda: 1.0 if education_level == 'Vocational/Specialised training' else 0.0,

    #                     'job_type_Dont Know/Refuse to answer': lambda: 1.0 if job_type == 'Dont Know/Refuse to answer' else 0.0,
    #                     'job_type_Farming and Fishing': lambda: 1.0 if job_type == 'Farming and Fishing' else 0.0,
    #                     'job_type_Formally employed Government': lambda: 1.0 if job_type == 'Formally employed Government' else 0.0,
    #                     'job_type_Formally employed Private': lambda: 1.0 if job_type == 'Formally employed Private' else 0.0,
    #                     'job_type_Government Dependent': lambda: 1.0 if job_type == 'Government Dependent' else 0.0,
    #                     'job_type_Informally employed': lambda: 1.0 if job_type == 'Informally employed' else 0.0,
    #                     'job_type_No Income': lambda: 1.0 if job_type == 'No Income' else 0.0,
    #                     'job_type_Other Income': lambda: 1.0 if job_type == 'Other Income' else 0.0,
    #                     'job_type_Remittance Dependent': lambda: 1.0 if job_type == 'Remittance Dependent' else 0.0,
    #                     'job_type_Self employed': lambda: 1.0 if job_type == 'elf employed' else 0.0,
    #             }, index=[0])
    
    data = pd.DataFrame({
        'country': country,                             
        'year': year,                            
        'location_type': location_type,                            
        'cellphone_access': cellphone_access,                           
        'household_size': household_size,     
        'age_of_respondent': age_of_respondent,             
        'gender_of_respondent': gender_of_respondent,
        'marital_status': household_size,
        'relationship_with_head': relationship_with_head,
        'education_level': education_level,
        'job_type': job_type
    }, index=[0])
    data['location_type'] = data['location_type'].map({'Urban':1,'Rural':0})
    data['cellphone_access'] = data['cellphone_access'].map({True: 1, False: 0})
    data['gender_of_respondent'] = data['gender_of_respondent'].map({'Male': 1, 'Female': 0})
    data = pd.get_dummies(data, columns=['country', 'marital_status','relationship_with_head', 'education_level', 'job_type'])
    
    data = data.reindex(columns=feature_names, fill_value=0)
    print(data.head())
    
    y = logreg.predict(data)
    if y==['No']:
        prediction = 'No Bank Account is beind used'
    else:
        prediction = 'A bank account is potentially used'

    st.text(prediction)