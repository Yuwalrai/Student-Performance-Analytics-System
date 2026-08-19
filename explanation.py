
from constants import (
    HIGH_RISK_THRESHOLD,
    MEDIUM_RISK_THRESHOLD,
    LOW_ATTENDANCE_THRESHOLD,
    HIGH_ATTENDANCE_THRESHOLD,
    MIN_STUDY_HOURS,
    WEAK_SUBJECT_THRESHOLD,
    RISK_TEMPLATES_SHORT,
    RISK_TEMPLATES_DETAILED,
    ENGAGEMENT_TEMPLATES_SHORT,
    ENGAGEMENT_TEMPLATES_DETAILED,
    ENGAGEMENT_PRIMARY_CONCERN,
    STATUS_TEMPLATES_SHORT,
    STATUS_TEMPLATES_DETAILED,
    STATUS_PRIMARY_CONCERN,
    STATUS_RECOMMENDED_ACTION_SHORT,
    STATUS_RECOMMENDED_ACTION_DETAILED,
    FACTOR_MESSAGES,
    SUBJECT_DISPLAY_NAMES
    )
def generate_risk_reason(row, detail_level) : 
    if detail_level == "short" : 
        return RISK_TEMPLATES_SHORT[row["risk_flag"]].format(average_score=row["average_score"])
    elif detail_level == "detailed" :
        return RISK_TEMPLATES_DETAILED[row["risk_flag"]].format(average_score=row["average_score"],high_risk_threshold = HIGH_RISK_THRESHOLD,medium_risk_threshold = MEDIUM_RISK_THRESHOLD)
    

def generate_risk_primary_concern(row) :   
    if row["weakest_subject_score"] < WEAK_SUBJECT_THRESHOLD :
        if row["weakest_subject"] in SUBJECT_DISPLAY_NAMES :
            weakness_subject_str = SUBJECT_DISPLAY_NAMES[row["weakest_subject"]] + " weakness (" + str(row["weakest_subject_score"]) + ")"
            return weakness_subject_str

def generate_risk_contributing_factors(row) :
    factors_list = []
    if row['attendance'] < LOW_ATTENDANCE_THRESHOLD :
        factors_list.append(FACTOR_MESSAGES['LOW_ATTENDANCE'])
    if row['study_hours'] < MIN_STUDY_HOURS :
        factors_list.append(FACTOR_MESSAGES['LIMITED_STUDY_HOURS'])
    if not  factors_list :
        return FACTOR_MESSAGES['NO_SIGNIFICANT_FACTORS']
    else :
        result = ", ".join(factors_list)    

    return result

    
def generate_engagement_reason(row, detail_level) :
    if detail_level == "short" : 
        return ENGAGEMENT_TEMPLATES_SHORT[row["engagement_level"]]
    elif detail_level == "detailed" :
        return ENGAGEMENT_TEMPLATES_DETAILED[row["engagement_level"]]

def generate_engagement_primary_concern(row):
    attendance_gap = 0
    study_gap = 0
    if  row['attendance'] < LOW_ATTENDANCE_THRESHOLD :
        attendance_gap =(LOW_ATTENDANCE_THRESHOLD - row['attendance']) / LOW_ATTENDANCE_THRESHOLD 
    if row['study_hours'] < MIN_STUDY_HOURS :
        study_gap = (MIN_STUDY_HOURS - row['study_hours']) / MIN_STUDY_HOURS
    if attendance_gap == 0 and study_gap == 0:
        return ENGAGEMENT_PRIMARY_CONCERN['NONE']

    if study_gap > attendance_gap :
        return ENGAGEMENT_PRIMARY_CONCERN['STUDY_HOURS_THRESHOLD'].format(study_hours = row['study_hours'])
    elif attendance_gap > study_gap  : 
        return ENGAGEMENT_PRIMARY_CONCERN['ATTENDANCE_THRESHOLD'].format(attendance = row['attendance'])
    elif study_gap == attendance_gap :
        return ENGAGEMENT_PRIMARY_CONCERN['BOTH_EQUAL']
    else :
        return ENGAGEMENT_PRIMARY_CONCERN['NONE']

def generate_engagement_contributing_factors(row) :    
    factors_list = []
    if row['attendance'] < LOW_ATTENDANCE_THRESHOLD :
        factors_list.append(FACTOR_MESSAGES['LOW_ATTENDANCE'])
    if row['study_hours'] < MIN_STUDY_HOURS :
        factors_list.append(FACTOR_MESSAGES['LIMITED_STUDY_HOURS'])
    if not  factors_list :
        return FACTOR_MESSAGES['NO_SIGNIFICANT_FACTORS']
    else :
        result = ", ".join(factors_list)    

    return result


def generate_status_reason(row, detail_level) :
    if detail_level == "short" : 
        return STATUS_TEMPLATES_SHORT[row["student_status"]]
    elif detail_level == "detailed" :
        return STATUS_TEMPLATES_DETAILED[row["student_status"]]

def generate_status_primary_concern(row) :
    return STATUS_PRIMARY_CONCERN[row["student_status"]] 

def generate_status_recommended_action(row,detail_level) :
    if detail_level == "short" :
        return STATUS_RECOMMENDED_ACTION_SHORT[row["student_status"]]
    elif detail_level == "detailed" :
        return STATUS_RECOMMENDED_ACTION_DETAILED[row["student_status"]]