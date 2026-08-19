import pandas as pd

df = pd.read_csv("students.csv")

clean_df = df.copy()
validation_report = {}

validation_report["missing_before"] = (
    clean_df.isnull().sum().to_dict()
)
score_cols = ["science", "math", "english", "nepali"]

# this helps to remove the string or char and make them Nan
for col in score_cols:
    clean_df[col] = pd.to_numeric(clean_df[col], errors="coerce")

clean_df['roll no.'] = pd.to_numeric(clean_df['roll no.'], errors="coerce")

validation_report["duplicate_roll_numbers"] = (
    clean_df["roll no."].duplicated().sum()
)
# filling the nan value with average where score_cols has all subject
for col in score_cols:
    col_mean = clean_df[col].mean()
    clean_df[col] = clean_df[col].fillna(col_mean)
    clean_df[col] = clean_df[col].clip(lower=0, upper=100)

# handling errors in attendance and giving mean to Nan
clean_df["attendance"] = pd.to_numeric(clean_df["attendance"], errors="coerce")
clean_df["attendance"] = clean_df["attendance"].clip(lower=0, upper=100)
attendance_avg = clean_df["attendance"].mean()
clean_df["attendance"] = clean_df["attendance"].fillna(attendance_avg)

# handling errors in study hours and filling with 0
clean_df['study_hours'] = pd.to_numeric(clean_df['study_hours'], errors='coerce')
clean_df['study_hours'] = clean_df['study_hours'].clip(lower=0)
clean_df['study_hours'] = clean_df['study_hours'].fillna(0)
    

range_report = {}

for col in score_cols + ["attendance", "study_hours"]:

    range_report[col] = {
        "min": clean_df[col].min(),
        "max": clean_df[col].max()
    }

validation_report["ranges"] = range_report  

validation_report["missing_after"] = (
    clean_df.isnull().sum().to_dict()
)

print("\nVALIDATION REPORT\n")

for key, value in validation_report.items():

    print(f"--- {key.upper()} ---")

    if isinstance(value, dict):

        for sub_key, sub_value in value.items():

            print(f"{sub_key} : {sub_value}")

    else:
        print(value)

    print()