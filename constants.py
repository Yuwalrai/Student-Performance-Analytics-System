# risk threshold
HIGH_RISK_THRESHOLD = 40
MEDIUM_RISK_THRESHOLD = 60

LOW_ATTENDANCE_THRESHOLD = 60
HIGH_ATTENDANCE_THRESHOLD = 80

MIN_STUDY_HOURS = 3

WEAK_SUBJECT_THRESHOLD = 60

RISK_TEMPLATES_SHORT = {
    "HIGH_RISK": "Average score below intervention threshold ({average_score}).",
    "MEDIUM_RISK": "Average score in monitoring range ({average_score}).",
    "SAFE": "Average score meets academic expectations ({average_score})."
}

RISK_TEMPLATES_DETAILED = {
    'HIGH_RISK' : 'Average score of {average_score} is below the intervention threshold of {high_risk_threshold}, indicating significant academic risk and the need for intervention.',
    'MEDIUM_RISK' : 'Average score of {average_score} falls within the monitoring range of {high_risk_threshold}–{medium_risk_threshold}, suggesting that academic performance should be observed and supported to prevent further decline.',
    'SAFE' : 'Average score of {average_score} meets expected academic standards and does not currently indicate academic risk.'
}

ENGAGEMENT_TEMPLATES_SHORT = {
    "LOW_ENGAGEMENT" : "Low attendance and/or study participation.",
    "MEDIUM_ENGAGEMENT" : "Engagement requires improvement.",
    "HIGH_ENGAGEMENT" :"Strong attendance and study habits."
}

ENGAGEMENT_TEMPLATES_DETAILED = {
'LOW_ENGAGEMENT' : 'Attendance and study participation are below expected levels, which may negatively affect academic performance and long-term progress.',
'MEDIUM_ENGAGEMENT' : 'Student demonstrates moderate engagement but would benefit from improved attendance and study consistency.',
'HIGH_ENGAGEMENT' : 'Student demonstrates strong attendance and consistent study habits, indicating a positive level of academic engagement.'
}

ENGAGEMENT_PRIMARY_CONCERN = {
'ATTENDANCE_THRESHOLD' : "Attendance deficiency ({attendance}%)",
'STUDY_HOURS_THRESHOLD' : "Limited study participation ({study_hours} hrs/day)",
"BOTH_EQUAL" : "Attendance and study participation contribute equally to low engagement.",
'NONE' : "No significant engagement concerns"
}

STATUS_TEMPLATES_SHORT = {
    "CRITICAL_SUPPORT_NEEDED" : "High academic risk combined with low engagement.",
    "MONITOR_PROGRESS" : "Performance and engagement require monitoring.",
    "HIGH_POTENTIAL" : "Strong performance and engagement." ,
    "GENERAL" : "Performing within expected range."
}

STATUS_TEMPLATES_DETAILED = {
'CRITICAL_SUPPORT_NEEDED' : 'The combination of high academic risk and low engagement indicates an immediate need for academic and behavioral support.',
'MONITOR_PROGRESS' : 'Current academic performance and engagement levels suggest that progress should be monitored to prevent future risk.',
'HIGH_POTENTIAL' : 'Strong academic performance and engagement indicate that the student may benefit from enrichment opportunities and advanced learning activities',
'GENERAL' : 'Current performance and engagement levels fall within expected ranges and do not require targeted intervention at this time.'
}

STATUS_PRIMARY_CONCERN = {
'CRITICAL_SUPPORT_NEEDED' : "Immediate academic and engagement intervention required.",
'MONITOR_PROGRESS' : "Student shows moderate academic and engagement concerns requiring continued monitoring.",
'HIGH_POTENTIAL' : "Student demonstrates strong academic performance and sustained engagement.",
'GENERAL' : "No significant academic or engagement concerns requiring targeted intervention."
}

STATUS_RECOMMENDED_ACTION_SHORT = {
'CRITICAL_SUPPORT_NEEDED' : "Begin immediate academic intervention.",
'MONITOR_PROGRESS' : "Monitor academic progress regularly.",
'HIGH_POTENTIAL' : "Provide enrichment opportunities.",
'GENERAL' : "Continue current learning plan."   
}

STATUS_RECOMMENDED_ACTION_DETAILED = {
'CRITICAL_SUPPORT_NEEDED' : "Provide academic tutoring, closely monitor attendance, involve parents or guardians when appropriate, and review progress weekly.",
'MONITOR_PROGRESS' : "Monitor academic performance regularly, encourage consistent attendance and study habits, and review progress periodically.",
'HIGH_POTENTIAL' : "Offer advanced learning opportunities, leadership activities, and academic enrichment programs to maintain growth.",
'GENERAL' : "Maintain current academic support, encourage regular attendance, and continue monitoring normal progress."
}
FACTOR_MESSAGES = {
    "LOW_ATTENDANCE": "Low attendance",
    "LIMITED_STUDY_HOURS": "Limited study hours",
    "NO_SIGNIFICANT_FACTORS": "No significant contributing factors"
    }

SUBJECT_DISPLAY_NAMES = {
    'math': 'Mathematics',
    'english': 'English',
    'science': 'Science',   
    'nepali': 'Nepali'
} 

