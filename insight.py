def generate_summary_report(df):

    report = {} 
    detailed_column = ["roll no.", "name", "average_score", "attendance", "risk_flag"]
    sort_column = ["average_score", "attendance"]
    n  = 20

    report["risk flag"] = {
        "high risk" : (df["risk_flag"] == "HIGH_RISK").sum(),
        "medium risk" : (df["risk_flag"] == "MEDIUM_RISK").sum(),
        "safe" : (df["risk_flag"] == "SAFE").sum(),
           
    }
    report["detailed risk flag"] = {
         "high risk students" : df[df["risk_flag"] == "HIGH_RISK"][detailed_column].sort_values(sort_column,ascending = [True, True]).head(n),
        "medium risk students" : df[df["risk_flag"] == "MEDIUM_RISK"][detailed_column].sort_values(sort_column,ascending = [True, True]).head(n)
    }
    report["engagement level"] = {
        "low engagement" : (df["engagement_level"] == "LOW_ENGAGEMENT").sum(),
        "medium engagement" : (df["engagement_level"] == "MEDIUM_ENGAGEMENT").sum(),
        "high engagement" : (df["engagement_level"] == "HIGH_ENGAGEMENT").sum()
    }

    report["student status"] = {
        "critical support" : (df["student_status"] == "CRITICAL_SUPPORT_NEEDED").sum(),
        "monitor progress" : (df["student_status"] == "MONITOR_PROGRESS").sum(),
        "high potential" : (df["student_status"] == "HIGH_POTENTIAL").sum(),
        "general" : (df["student_status"] == "GENERAL").sum()
    }
    report["Detailed student status"] = {
        "detailed critical support" : (df[df["student_status"] == "CRITICAL_SUPPORT_NEEDED"]
        .sort_values(sort_column,ascending = [True, True])
        [["roll no.", "name", "average_score", "risk_flag", "engagement_level"]].head(n)),
        "detailed monitor progress" : (df[df["student_status"] == "MONITOR_PROGRESS"]
        [["roll no.", "name", "average_score","best_subject","best_subject_score","weakest_subject","weakest_subject_score"]]
        .sort_values("average_score",ascending = True).head(n)),
        "detailed high potential" : (df[df["student_status"] == "HIGH_POTENTIAL"]
        [["roll no.", "name", "average_score","best_subject","best_subject_score"]]
        .sort_values("average_score",ascending = False).head(n))
    }

    return report


all_column =  ["science", "math", "english", "nepali","attendance", "study_hours","average_score"]
subject_column =  ["science", "math", "english", "nepali"]

def generate_correlation(df):
    correlation = df[all_column].corr()

    return correlation

def display_report(report) :
    print("RISK REPORT")
    print("----------")
    # Print the formatted text
    risk_data = report["risk flag"]
    print(f"High Risk: {risk_data['high risk']}")
    print(f"Medium Risk: {risk_data['medium risk']}")
    print(f"Safe: {risk_data['safe']}")

    print("High Risk Students")
    print(report["detailed risk flag"]["high risk students"])

    print("Medium Risk Student")
    print(report["detailed risk flag"]["medium risk students"])

    print("ENGAGEMENT REPORT")
    print("-----------------")
    engagement_data = report["engagement level"]
    print(f"Low Engagement: {engagement_data['low engagement']}")
    print(f"Medium Engagement: {engagement_data['medium engagement']}")
    print(f"High Engagement: {engagement_data['high engagement']}\n")

    print("STUDENT STATUS REPORT")
    print("---------------------")
    status_data = report["student status"]
    print(f"Critical Support: {status_data['critical support']}")
    print(f"Monitor Progress: {status_data['monitor progress']}")
    print(f"High Potential: {status_data['high potential']}")
    print(f"General: {status_data['general']}\n")

    print("Detailed Critical Support")
    print(report["Detailed student status"]["detailed critical support"])

    print("Detailed Monitor Progress")
    print(report["Detailed student status"]["detailed monitor progress"])

    print("Detailed High Potential")
    print(report["Detailed student status"]["detailed high potential"])


