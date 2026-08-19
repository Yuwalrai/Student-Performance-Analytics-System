line_width = 60
def build_overview_section(df):
    total_students = len(df)
    average_score = df["average_score"].mean()
    highest_score = df["average_score"].max()
    lowest_score = df["average_score"].min()
    avg_study_hours = df["study_hours"].mean()
    avg_attendance = df["attendance"].mean()

    section = "-" * line_width + "\n"
    section += "DATASET OVERVIEW\n"
    section += "-" * line_width + "\n"
    section += f"Total Students : {total_students}\n"
    section += f"Average Score : {average_score:.2f}\n"
    section += f"Highest Score : {highest_score:.2f}\n"
    section += f"Lowest Score  : {lowest_score:.2f}\n"
    section += f"Average Attendance  : {avg_attendance:.2f}%\n"
    section += f"Average Study Hours : {avg_study_hours:.2f} hrs/day\n"

    return section

def build_distribution_section(df, section_title, column_name) : 
    category_counts = df[column_name].value_counts()

    section = "-" * line_width + "\n"
    section += f"{section_title} DISTRIBUTION\n"
    section += "-" * line_width + "\n"
    for category, counts in category_counts.items() :
        section += f"{category:10} {counts}\n"

    return section

def build_grade_distribution_section(df) :
    section = build_distribution_section(df,'GRADE','grade')
    return section

def build_risk_distribution_section(df) :
    section = build_distribution_section(df,'RISK LEVEL','risk_flag')
    return section

def build_engagement_distribution_section(df) :
    section = build_distribution_section(df,'ENGAGEMENT LEVEL','engagement_level')
    return section

def build_status_distribution_section(df) :
    section = build_distribution_section(df,'STUDENT STATUS','student_status')
    return section

def build_dashboard(df) :
    section = "=" * line_width + "\n"
    section += "STUDENT PERFORMANCE DASHBOARD".center(line_width) + "\n"
    section += "=" * line_width + "\n"

    dataset_overview = build_overview_section(df)
    section += dataset_overview

    grade_distribution = build_grade_distribution_section(df)
    section += grade_distribution

    risk_level_distribution = build_risk_distribution_section(df)
    section += risk_level_distribution

    engagement_level_distribution = build_engagement_distribution_section(df)
    section += engagement_level_distribution

    student_status_distribution = build_status_distribution_section(df)
    section += student_status_distribution

    section += "=" * line_width + "\n"
    section += "END OF DASHBOARD".center(line_width) + "\n"
    section += "=" * line_width + "\n"

    return section

