# global variable for all function
subject_cols = ["science","math","english","nepali"]

# average function
def create_average_score(df):
    df["average_score"] = (
        df[subject_cols].mean(axis=1)
    )

    return df

# Calculating total marks of each student
def create_total_students(df) :
    df["total"] = df["science"] + df["math"] + df["english"] + df["nepali"]
    return df

# Creating percentage of each students 
def create_percentage(df) :
    df["percentage"] = ((df["total"] /300) * 100 ).round(2)
    return df

# creating grade of each students
def create_grade(df) :
    df["grade"] = ""
    df.loc[df["percentage"] >= 80, "grade"] = "A"
    df.loc[(df["percentage"] >=60) & (df["percentage"]< 80), "grade"] = "B"
    df.loc[(df["percentage"] >= 40) & (df["percentage"] <60), "grade"] = "C"
    df.loc[df["percentage"] < 40, "grade"] = "Fail"
    return df

# Finding best and weakest subject
def create_subject_insights(df) :
    df["best_subject_score"] = df[subject_cols].max(axis=1)
    df["weakest_subject_score"] = df[subject_cols].min(axis=1)
    df["best_subject"] = df[subject_cols].idxmax(axis=1)
    df["weakest_subject"] = df[subject_cols].idxmin(axis=1)
    return df

# -----------------------------
# RISK FLAG
# -----------------------------
def risk_mask(df) :
    high_risk_mask = df["average_score"] < 40

    medium_risk_mask = (
        (df["average_score"] >= 40) &
        (df["average_score"] < 60)
    )

    safe_mask = df["average_score"] >= 60


    df.loc[high_risk_mask, "risk_flag"] = "HIGH_RISK"

    df.loc[medium_risk_mask, "risk_flag"] = "MEDIUM_RISK"

    df.loc[safe_mask, "risk_flag"] = "SAFE"

    return df

# -----------------------------
# ENGAGEMENT LEVEL
# -----------------------------
def engagement_mask(df) :
    high_engagement_mask = (
        (df["attendance"] >= 80) &
        (df["study_hours"] >= 3)
    )

    medium_engagement_mask = (
        (df["attendance"] >= 60) &
        (df["attendance"] < 80)
    )

    low_engagement_mask = ~(
        high_engagement_mask |
        medium_engagement_mask
    )


    df.loc[
        high_engagement_mask,
        "engagement_level"
    ] = "HIGH_ENGAGEMENT"

    df.loc[
        medium_engagement_mask,
        "engagement_level"
    ] = "MEDIUM_ENGAGEMENT"

    df.loc[
        low_engagement_mask,
        "engagement_level"
    ] = "LOW_ENGAGEMENT"

    return df

# -----------------------------
# STUDENT STATUS
# -----------------------------

def student_mask(df) :
    df["student_status"] = ""

    critical_support_mask = (
        (df["engagement_level"] == "LOW_ENGAGEMENT") &
        (df["risk_flag"] == "HIGH_RISK")
    )

    monitor_progress_mask = (
        (df["engagement_level"] == "MEDIUM_ENGAGEMENT") &
        (df["risk_flag"] == "MEDIUM_RISK")
    )

    high_potential_mask = (
        (df["engagement_level"] == "HIGH_ENGAGEMENT") &
        (df["risk_flag"] == "SAFE")
    )


    general_mask = ~(
        critical_support_mask |
        monitor_progress_mask |
        high_potential_mask
    )


    df.loc[
        critical_support_mask,
        "student_status"
    ] = "CRITICAL_SUPPORT_NEEDED"

    df.loc[
        monitor_progress_mask,
        "student_status"
    ] = "MONITOR_PROGRESS"

    df.loc[
        high_potential_mask,
        "student_status"
    ] = "HIGH_POTENTIAL"

    df.loc[
        general_mask,
        "student_status"
    ] = "GENERAL"

    return df

# -----------------------------
# STUDENT RANK
# -----------------------------
def create_student_rank(df) :
    ranked_df = df.sort_values(by=["average_score", "roll no."], ascending=[False, True])
    ranked_df["student_rank"] = ranked_df["average_score"].rank(ascending=False, method = "dense").astype(int)
    return ranked_df.sort_index()

