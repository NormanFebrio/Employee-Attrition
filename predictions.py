from tensorflow.keras.models import load_model
import joblib
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=UserWarning)


# Load A Model for Attrition Prediction
model = load_model("model.h5")
model

# Load all the preprocessing files
pcacf = joblib.load("assets/pca_joblevel_monthlyincome_totalworkingyears")
pcapsh = joblib.load("assets/pca_salaryhike_performance")
pcaye = joblib.load("assets/pca_yearsatcompany_currrole_currmanager")
age_transformer = joblib.load("assets/Transformed_Age")
dfh_transformer = joblib.load("assets/Transformed_DistanceFromHome")
env_transformer = joblib.load("assets/Transformed_EnvironmentSatisfaction")
jobsat_transformer = joblib.load("assets/Transformed_JobSatisfaction")
relsat_transformer = joblib.load("assets/Transformed_RelationshipSatisfaction")
numcom_transformer = joblib.load("assets/Transformed_NumCompaniesWorked")
pcacf_transformer = joblib.load("assets/Transformed_PCA_CareerFinance")
pcapsh_transformer = joblib.load("assets/Transformed_PCA_PerformanceSalaryHike")
pcaye_transformer = joblib.load("assets/Transformed_PCA_YearsExperience")
sol_transformer = joblib.load("assets/Transformed_StockOptionLevel")

# Get the employee data
employee_data = {}
employee_data["Age"] = float(input("Age: "))
employee_data["DistanceFromHome"] = float(input("Distance from home to office: "))
employee_data["EnvironmentSatisfaction"] = float(input("Environment Satisfaction (1 - 5): "))
employee_data["JobSatisfaction"] = float(input("Job Satisfaction (1 - 5): "))
employee_data["NumCompaniesWorked"] = float(input("Number of companies ever worked: "))
employee_data["RelationshipSatisfaction"] = float(input("Relationship Satisfaction (1 - 5): "))
employee_data["StockOptionLevel"] = float(input("Stock option level (0 - 3): "))
employee_data["JobLevel"] = float(input("Job level (1 - 5): "))
employee_data["MonthlyIncome"] = float(input("Monthly income (US$): "))
employee_data["TotalWorkingYears"] = float(input("Total working years: "))
employee_data["PercentSalaryHike"] = float(input("Percent salary hike: "))
employee_data["PerformanceRating"] = float(input("PerformanceRating (1 - 5): "))
employee_data["YearsAtCompany"] = float(input("Years in this company: "))
employee_data["YearsInCurrentRole"] = float(input("Years in current role: "))
employee_data["YearsWithCurrManager"] = float(input("Years with current manager: "))

def preprocessing_input(data):
    new_data = data.copy()
    values_ = []

    #PCA
    pcacf_value = pcacf.transform([[new_data["JobLevel"],
                                    new_data["MonthlyIncome"],
                                    new_data["TotalWorkingYears"]
                                   ]])
    pcapsh_value = pcapsh.transform([[new_data["PercentSalaryHike"],
                                      new_data["PerformanceRating"]
                                     ]])
    pcaye_value = pcaye.transform([[new_data["YearsAtCompany"],
                                    new_data["YearsInCurrentRole"],
                                    new_data["YearsWithCurrManager"]
                                   ]])
    key_to_remove = ["JobLevel","MonthlyIncome","TotalWorkingYears",
                     "PercentSalaryHike","PerformanceRating",
                     "YearsAtCompany","YearsInCurrentRole",
                     "YearsWithCurrManager"]
    for key in key_to_remove:
        if key in new_data:
            del new_data[key]

    # PowerTransformer
    new_data["Age"] = age_transformer.transform(np.array(new_data["Age"]).reshape(-1, 1))[0][0]
    new_data["DistanceFromHome"] = dfh_transformer.transform(np.array(
        new_data["DistanceFromHome"]).reshape(-1, 1))[0][0]
    new_data["EnvironmentSatisfaction"] = env_transformer.transform(np.array(
        new_data["EnvironmentSatisfaction"]).reshape(-1,1))[0][0]
    new_data["JobSatisfaction"] = jobsat_transformer.transform(np.array(
        new_data["JobSatisfaction"]).reshape(-1,1))[0][0]
    new_data["NumCompaniesWorked"] = numcom_transformer.transform(np.array(
        new_data["NumCompaniesWorked"]).reshape(-1,1))[0][0]
    new_data["RelationshipSatisfaction"] = relsat_transformer.transform(np.array(
        new_data["RelationshipSatisfaction"]).reshape(-1,1))[0][0]
    new_data["StockOptionLevel"] = sol_transformer.transform(np.array(
        new_data["StockOptionLevel"]).reshape(-1,1))[0][0]
    new_data["transformed_PCA_CareerFinance"] = pcacf_transformer.transform(pcacf_value)[0][0]
    new_data["transformed_PCA_YearsExperience"] = pcaye_transformer.transform(pcaye_value)[0][0]
    new_data["transformed_PCA_PerformanceSalaryHike"] = pcapsh_transformer.transform(pcapsh_value)[0][0]

    for feature_name, feature_value in new_data.items():
        values_.append(feature_value)
    return values_

preprocessed_data = preprocessing_input(employee_data)

result = model.predict([preprocessed_data], verbose=0)

# Only classified as attrition if its probability more than 70%
result = (result > 0.7).astype(int)
if result == 0:
    print("No")
else:
    print("Yes")

