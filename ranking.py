from feature_engineering import(
    create_student_rank
)
REPORT_WIDTH = 60       
def build_leaderboard(df, max_rank) :
    report_text = "=" *60 + "\n"
    report_text += "STUDENT LEADERBOARD\n".center(60)
    report_text += "=" *REPORT_WIDTH + "\n"
    leaderboard_df = create_student_rank(df)
    leaderboard_df = leaderboard_df.sort_values (by="student_rank", ascending = True)
    report_text += f"Showing Top {max_rank} Ranks\n"
    report_text +=  "-" * REPORT_WIDTH + "\n"
    report_text += f"{'Rank':<6} {'Roll':<8} {'Name':<20} {'Average':<12} {'Grade':<8}\n"
    report_text += "-" * REPORT_WIDTH + "\n"
    leaderboard_df = leaderboard_df[leaderboard_df["student_rank"] <= max_rank]
    for _, row in leaderboard_df.iterrows():
        report_text += f"{row['student_rank']:<6}  {row['roll no.']:<8}  {row['name']:<20}  {row['average_score']:<12.2f}  {row['grade']:<8}\n"
    report_text +=  "-" * REPORT_WIDTH + "\n"

    report_text +=  "-" * REPORT_WIDTH + "\n"
    report_text += f"Total Students Displayed : {len(leaderboard_df)}\n"
    report_text += "=" *REPORT_WIDTH + "\n"
    return report_text 
