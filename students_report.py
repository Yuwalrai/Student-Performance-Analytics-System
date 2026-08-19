def build_risk_section(row, detail_level) :
    section = "--------------------------------------------------\n"
    section += " ACADEMIC RISK\n"
    section += "-------------------------------------------------\n"

    section += f" Risk Level              :{row['risk_flag']}\n"
    reason_column = "risk_reason_" + detail_level
    section += f" Reason                   :{row[reason_column]}\n"
    section += f" Primary Concern          :{row['risk_primary_concern']}\n"
    section += f" Contributing Factors     :{row['risk_contributing_factors']}\n"  
    return section

def build_engagement_section(row, detail_level) :
    section = "--------------------------------------------------\n"
    section += " ENGAGEMENT\n"
    section += "--------------------------------------------------\n"

    section += f" Engagement Level          :{row['engagement_level']}\n"
    engagement_column = "engagement_reason_" + detail_level
    section += f" Reason                    :{row[engagement_column]}\n"
    section += f" Primary Reason            :{row['engagement_primary_concern']}\n"        
    section += f" Contributing Factors     :{row['engagement_contributing_factors']}\n"  
    return section

def build_status_section(row, detail_level) :
    section = "--------------------------------------------------\n"
    section += " OVERALL STATUS\n"
    section += "--------------------------------------------------\n"

    section += f" Status                    :{row['student_status']}\n"
    status_column = "status_reason_" + detail_level
    section += f" Reason                    :{row[status_column]}\n"

    section += f" Primary Reason            :{row['status_primary_concern']}\n" 
    recommend_column = "status_recommended_action_" + detail_level
    section += f"Recommended Action      :{row[recommend_column]}\n"
    return section

def find_student(df, roll_no) :
    student = df[df["roll no."] == roll_no]
    if student.empty:
        return None

    row = student.iloc[0]
    return row

def display_student_report(df, roll_no, detail_level) :
    row = find_student(df,roll_no)
    if row is None:
        return "Student not found."
    report_text = "==================================================\n"
    report_text += "            STUDENT PERFORMANCE REPORT\n"
    report_text += "==================================================\n"

    report_text += f" Student Name :{row['name']}\n"
    report_text += f" Roll Number  :{roll_no}\n"

    report_text += build_risk_section(row, detail_level)
    report_text += build_engagement_section(row, detail_level)
    report_text += build_status_section(row, detail_level)
    
    report_text  += "=================================================="
    return report_text

DETAIL_LEVEL_MAP = {
    "1": "short",
    "2": "detailed"
}

def search_student_menu(df,roll_no, choice_no) :
    section = "=====================================\n"
    section += "STUDENT PERFORMANCE ANALYTICS SYSTEM\n"
    section +="=====================================\n"

    section += f"Enter Roll Number: {roll_no}\n"

    row = find_student(df,roll_no)
    if row is None:
        return "Student not found." 

    section += "Select Report Detail\n"
    section += "1. short\n"
    section += "2. detailed\n"

    section += f"Choice: {choice_no}\n"
    VALID_CHOICES = {"1", "2"}
    if choice_no not in VALID_CHOICES :
        print("⚠️ Warning: Invalid choice detected. Forcing fallback to '1' (short).")
        choice_no = "1"

    section += f"Generating {DETAIL_LEVEL_MAP[choice_no]} report...\n"
    section += display_student_report(df, roll_no, DETAIL_LEVEL_MAP[choice_no])
    section += "\n=====================================\n"
    section += "    STUDENT PERFORMANCE REPORT\n"
    section +=  "=====================================\n"
    return section
