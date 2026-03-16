1/1:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
 1/2:
url='https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2018/2018-09-04/fastfood_calories.csv'
df=pd.read_csv(url)
df.head()
 1/3:
print(df.shape)
print(df.describe())
 1/4:
plt.figure()
sns.histplot(df['calories'], bins=30)
plt.title('Calories Distribution')
plt.show()
 1/5:
features=['total_fat','cholesterol','sodium','total_carb','protein']
X=df[features]
y=df['calories']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
model=LinearRegression()
model.fit(X_train,y_train)
pred=model.predict(X_test)
print('R2:',r2_score(y_test,pred))
 2/1: print"hello|"
 2/2: print"hello"
 2/3: print("hello")
 4/1:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
 4/2:
url='https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2018/2018-09-04/fastfood_calories.csv'
df=pd.read_csv(url)
df.head()
 4/3:
print(df.shape)
print(df.describe())
 4/4:
plt.figure()
sns.histplot(df['calories'], bins=30)
plt.title('Calories Distribution')
plt.show()
 4/5:
features=['total_fat','cholesterol','sodium','total_carb','protein']
X=df[features]
y=df['calories']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
model=LinearRegression()
model.fit(X_train,y_train)
pred=model.predict(X_test)
print('R2:',r2_score(y_test,pred))
 5/1:




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
 5/2:
url='https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2018/2018-09-04/fastfood_calories.csv'
df=pd.read_csv(url)
df.head()
 5/3:
print(df.shape)
print(df.describe())
 5/4:
plt.figure()
sns.histplot(df['calories'], bins=30)
plt.title('Calories Distribution')
plt.show()
 5/5:
features=['total_fat','cholesterol','sodium','total_carb','protein']
X=df[features]
y=df['calories']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
model=LinearRegression()
model.fit(X_train,y_train)
pred=model.predict(X_test)
print('R2:',r2_score(y_test,pred))
 6/1:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
 6/2:
# Load dataset
df = pd.read_csv('student_study_hours_dataset.csv')
df.head()
 8/1:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
 8/2:
# Load dataset
df = pd.read_csv('student_study_hours_dataset.csv')
df.head()
 9/1:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
 9/2:
# Load dataset
df = pd.read_csv('student_study_hours_dataset.csv')
df.head()
 9/3:
# Basic info
df.info()
df.describe()
 9/4:
# Scatter plot
plt.scatter(df['Hours'], df['Scores'])
plt.xlabel('Study Hours')
plt.ylabel('Exam Scores')
plt.title('Study Hours vs Exam Scores')
plt.show()
 9/5:
# Correlation
df.corr()
 9/6:
# Prepare data for ML model
X = df[['Hours']]
y = df['Scores']
 9/7:
# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
 9/8:
# Train model
model = LinearRegression()
model.fit(X_train, y_train)
 9/9:
# Predictions
predictions = model.predict(X_test)
9/10:
# Model evaluation
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print('MAE:', mae)
print('R2 Score:', r2)
9/11:
# Regression line visualization
plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.xlabel('Study Hours')
plt.ylabel('Exam Scores')
plt.title('Regression Line')
plt.show()
10/1:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
10/2:
url='https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2018/2018-09-04/fastfood_calories.csv'
df=pd.read_csv(url)
df.head()
10/3:
print(df.shape)
print(df.describe())
10/4:
plt.figure()
sns.histplot(df['calories'], bins=30)
plt.title('Calories Distribution')
plt.show()
10/5:
features=['total_fat','cholesterol','sodium','total_carb','protein']
X=df[features]
y=df['calories']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
model=LinearRegression()
model.fit(X_train,y_train)
pred=model.predict(X_test)
print('R2:',r2_score(y_test,pred))
11/1: !pip install pandas numpy matplotlib seaborn scikit-learn
11/2:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Optional: set plot style
sns.set(style="whitegrid")
11/3:
# Simulate dataset
np.random.seed(42)  # for reproducibility
study_hours = np.random.uniform(1, 10, 50)  # 50 students, study hours between 1 and 10
# Exam marks roughly correlated with study hours + some randomness
exam_marks = study_hours * 10 + np.random.normal(0, 5, 50)  

# Create DataFrame
data = pd.DataFrame({
    "StudyHours": study_hours,
    "ExamMarks": exam_marks
})

# Clip exam marks between 0 and 100
data['ExamMarks'] = data['ExamMarks'].clip(0, 100)

# Save to CSV (optional)
data.to_csv("student_study_hours_dataset.csv", index=False)

# Show first 5 rows
data.head()
11/4:
# Summary statistics
print("Summary statistics:")
print(data.describe())

# Correlation
print("\nCorrelation between StudyHours and ExamMarks:")
print(data.corr())

# Scatter plot
plt.figure(figsize=(8,6))
sns.scatterplot(x='StudyHours', y='ExamMarks', data=data, color='blue', s=80)
plt.title("Study Hours vs Exam Marks")
plt.xlabel("Study Hours")
plt.ylabel("Exam Marks")
plt.show()
11/5:
# Split data into training and testing sets
X = data[['StudyHours']]
y = data['ExamMarks']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("R² Score:", r2_score(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

# Regression line visualization
plt.figure(figsize=(8,6))
plt.scatter(X, y, color='blue', label="Actual Marks", s=80)
plt.plot(X_test, y_pred, color='red', linewidth=2, label="Regression Line")
plt.title("Linear Regression: Study Hours vs Exam Marks")
plt.xlabel("Study Hours")
plt.ylabel("Exam Marks")
plt.legend()
plt.show()
11/6:
- There is a strong positive correlation between study hours and exam marks.
- The regression model predicts exam marks reasonably well (check R² value).
- Students studying less than ~3 hours tend to score low marks (<40).
- Students studying more than 7–8 hours often score high (>75).
11/7:
plt.figure(figsize=(8,6))
sns.histplot(data['StudyHours'], bins=10, kde=True, color='skyblue')
plt.title("Histogram of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Frequency")
plt.show()
12/1: !pip install pandas numpy matplotlib seaborn openpyxl scikit-learn
12/2:
import pandas as pd

# Load the Excel dataset
df = pd.read_excel("students_academic_performance.xlsx")

# Show shape & first few rows
print("Shape:", df.shape)
df.head()
13/1: !pip install pandas numpy matplotlib seaborn openpyxl scikit-learn
13/2:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")  # nice plot style
13/3:
try:
    df = pd.read_excel("Students Academic Performance Evaluation.xlsx")
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("File not found. Make sure the Excel file is in the same folder as this notebook.")
13/4:
# df = pd.read_excel("C:/Users/Nethsara/Downloads/Students Academic Performance Evaluation.xlsx")
# print("Dataset loaded successfully!")
13/5:
print("Shape of dataset:", df.shape)
print("\nColumns in dataset:", df.columns)
df.head()
14/1: !pip install pandas numpy matplotlib seaborn openpyxl scikit-learn
14/2:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")  # Nice plot style
14/3:
try:
    df = pd.read_excel("Students Academic Performance Evaluation.xlsx")
    print("✅ Dataset loaded successfully!")
except FileNotFoundError:
    print("❌ File not found. Make sure the Excel file is in the same folder as this notebook!")
14/4:
# Example: replace with the path on your computer
# df = pd.read_excel("C:/Users/Nethsara/Downloads/Students Academic Performance Evaluation.xlsx")
# print("✅ Dataset loaded successfully!")
14/5:
print("Shape of dataset:", df.shape)
print("\nColumns in dataset:", df.columns)
df.head()
14/6:
import pandas as pd

try:
    df = pd.read_excel("students.xlsx")  # Make sure the filename matches exactly
    print("✅ Dataset loaded successfully!")
except FileNotFoundError:
    print("❌ File not found. Make sure the Excel file is in the same folder as this notebook!")
14/7:
print("Shape of dataset:", df.shape)
print("\nColumns in dataset:", df.columns)
df.head()
14/8: !pip install tk
14/9:
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Hide the main Tk window
Tk().withdraw()  

# Open a file dialog to select your Excel file
file_path = askopenfilename(title="Select the Excel dataset", filetypes=[("Excel files", "*.xlsx *.xls")])

# Load the dataset
if file_path:
    df = pd.read_excel(file_path)
    print("✅ Dataset loaded successfully!")
    print("Shape:", df.shape)
    print("Columns:", df.columns)
else:
    print("❌ No file selected. Please select your Excel dataset.")
14/10: df.head()
15/1: students.xlsx.xlsx
15/2: students.xlsx
   1: students.xlsx.xlsx
   2: !pip install pandas numpy matplotlib seaborn scikit-learn openpyxl
   3:
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)
   4:
file_path = "students.xlsx.xlsx"   # change this only if your file name is different

df = pd.read_excel(file_path)

print("Dataset loaded successfully.")
print("Shape:", df.shape)
print("\nFirst 5 rows:")
display(df.head())
   5:
print("Column names:\n")
for i, col in enumerate(df.columns, start=1):
    print(f"{i}. {col}")

print("\nData types:\n")
display(df.dtypes)

print("\nMissing values:\n")
display(df.isnull().sum())
   6:
# Remove extra spaces from column names
df.columns = [col.strip() for col in df.columns]

# Standardize inconsistent text values
df["Do you have any health issues?"] = (
    df["Do you have any health issues?"]
    .astype(str)
    .str.strip()
    .str.title()
    .replace({"N": "No"})
)

df["What is your relationship status?"] = (
    df["What is your relationship status?"]
    .astype(str)
    .str.strip()
    .replace({"In a relationship": "Relationship"})
)

# Convert attendance to numeric
df["Average attendance on class"] = pd.to_numeric(
    df["Average attendance on class"], errors="coerce"
)

# Fill missing skill values
df["What are the skills do you have ?"] = df["What are the skills do you have ?"].fillna("Unknown")

print("Cleaning completed.")
print("\nMissing values after cleaning:\n")
display(df.isnull().sum())
   7:
# Remove extra spaces from column names
df.columns = [col.strip() for col in df.columns]

# Standardize inconsistent text values
df["Do you have any health issues?"] = (
    df["Do you have any health issues?"]
    .astype(str)
    .str.strip()
    .str.title()
    .replace({"N": "No"})
)

df["What is your relationship status?"] = (
    df["What is your relationship status?"]
    .astype(str)
    .str.strip()
    .replace({"In a relationship": "Relationship"})
)

# Convert attendance to numeric
df["Average attendance on class"] = pd.to_numeric(
    df["Average attendance on class"], errors="coerce"
)

# Fill missing skill values
df["What are the skills do you have ?"] = df["What are the skills do you have ?"].fillna("Unknown")

print("Cleaning completed.")
print("\nMissing values after cleaning:\n")
display(df.isnull().sum())
   8:
print("Numerical summary:")
display(df.describe())

print("Categorical summary:")
display(df.describe(include="object"))
   9:
study_col = "How many hour do you study daily?"
target_col = "What is your current CGPA?"

print("Research Question:")
print("How much do daily study hours affect students' current CGPA?")
  10:
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x=study_col, y=target_col)
plt.title("Daily Study Hours vs Current CGPA")
plt.xlabel("Daily Study Hours")
plt.ylabel("Current CGPA")
plt.show()
  11:
avg_cgpa_by_study = df.groupby(study_col)[target_col].mean().reset_index()

display(avg_cgpa_by_study)

plt.figure(figsize=(10, 5))
sns.barplot(data=avg_cgpa_by_study, x=study_col, y=target_col)
plt.title("Average CGPA by Daily Study Hours")
plt.xlabel("Daily Study Hours")
plt.ylabel("Average Current CGPA")
plt.show()
  12:
numeric_df = df.select_dtypes(include=[np.number])

corr_matrix = numeric_df.corr()

display(corr_matrix[[target_col]].sort_values(by=target_col, ascending=False))

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=False, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
  13:
cgpa_corr = corr_matrix[target_col].sort_values(ascending=False)

print("Top correlations with Current CGPA:")
display(cgpa_corr)
  14:
target = "What is your current CGPA?"

# Drop target and constant/useless column
drop_columns = [target, "Program"]

X = df.drop(columns=drop_columns)
y = df[target]

categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()
numeric_cols = X.select_dtypes(exclude=["object"]).columns.tolist()

print("Number of numeric columns:", len(numeric_cols))
print("Number of categorical columns:", len(categorical_cols))

print("\nNumeric columns:")
print(numeric_cols)

print("\nCategorical columns:")
print(categorical_cols)
  15:
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training set size:", X_train.shape)
print("Testing set size:", X_test.shape)
  16:
numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(transformers=[
    ("num", numeric_transformer, numeric_cols),
    ("cat", categorical_transformer, categorical_cols)
])
  17:
linear_model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", LinearRegression())
])

linear_model.fit(X_train, y_train)
linear_pred = linear_model.predict(X_test)

linear_mae = mean_absolute_error(y_test, linear_pred)
linear_rmse = np.sqrt(mean_squared_error(y_test, linear_pred))
linear_r2 = r2_score(y_test, linear_pred)

print("Linear Regression Results")
print("MAE :", round(linear_mae, 4))
print("RMSE:", round(linear_rmse, 4))
print("R²  :", round(linear_r2, 4))
  18:
rf_model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", RandomForestRegressor(
        n_estimators=300,
        random_state=42,
        n_jobs=-1
    ))
])

rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

rf_mae = mean_absolute_error(y_test, rf_pred)
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))
rf_r2 = r2_score(y_test, rf_pred)

print("Random Forest Results")
print("MAE :", round(rf_mae, 4))
print("RMSE:", round(rf_rmse, 4))
print("R²  :", round(rf_r2, 4))
  19:
results = pd.DataFrame({
    "Model": ["Linear Regression", "Random Forest"],
    "MAE": [linear_mae, rf_mae],
    "RMSE": [linear_rmse, rf_rmse],
    "R2 Score": [linear_r2, rf_r2]
})

display(results.sort_values(by="R2 Score", ascending=False))
  20:
best_pred = rf_pred  # Random Forest performed better during inspection

plt.figure(figsize=(8, 5))
plt.scatter(y_test, best_pred)
plt.xlabel("Actual CGPA")
plt.ylabel("Predicted CGPA")
plt.title("Actual vs Predicted CGPA (Random Forest)")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()])
plt.show()
  21:
# Fit again to safely extract details
rf_model.fit(X_train, y_train)

# Get feature names after preprocessing
ohe = rf_model.named_steps["preprocessor"].named_transformers_["cat"].named_steps["onehot"]
encoded_cat_features = list(ohe.get_feature_names_out(categorical_cols))
all_features = numeric_cols + encoded_cat_features

importances = rf_model.named_steps["model"].feature_importances_

feature_importance_df = pd.DataFrame({
    "Feature": all_features,
    "Importance": importances
}).sort_values(by="Importance", ascending=False)

display(feature_importance_df.head(15))

plt.figure(figsize=(10, 6))
sns.barplot(
    data=feature_importance_df.head(10),
    x="Importance",
    y="Feature"
)
plt.title("Top 10 Most Important Features for Predicting Current CGPA")
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.show()
  22:
study_hours_corr = corr_matrix.loc[study_col, target_col]

print("Correlation between daily study hours and current CGPA:", round(study_hours_corr, 4))

if study_hours_corr > 0.3:
    print("There is a meaningful positive relationship between study hours and CGPA.")
elif study_hours_corr > 0:
    print("There is a weak positive relationship between study hours and CGPA.")
elif study_hours_corr < 0:
    print("There is a negative relationship between study hours and CGPA.")
else:
    print("There is almost no linear relationship between study hours and CGPA.")
  23:
print("FINAL INTERPRETATION")
print("- This dataset was used to study factors affecting students' current CGPA.")
print("- Daily study hours alone do not appear to be the strongest predictor of CGPA.")
print("- Previous SGPA is the strongest predictor of current CGPA.")
print("- Other useful factors include completed credits, attendance, and skill development time.")
print("- Random Forest performs better than Linear Regression because student performance depends on multiple interacting factors.")