from cleaning import clean_df
import visualization
from insight import (
    generate_summary_report,
    generate_correlation,
    display_report,
   
)
from feature_engineering import(
    create_average_score,
    create_subject_insights,
    create_grade,
    risk_mask,
    engagement_mask,        
    student_mask,
    create_student_rank,
    create_percentage,
    create_total_students
    )

from explanation import (
  generate_engagement_contributing_factors,
  generate_engagement_primary_concern,
  generate_engagement_reason,
  generate_risk_contributing_factors,
  generate_risk_primary_concern,
  generate_risk_reason,
  generate_status_primary_concern,
  generate_status_reason,
  generate_status_recommended_action
 )

from students_report import (
    display_student_report,
    search_student_menu,
    DETAIL_LEVEL_MAP
)

from reports import (
    build_dashboard
)

from interactive_menu import (
    display_menu,
    display_student_report,
    handle_exit,
    handle_dashboard,
    handle_leaderboard,
    handle_search,
    run_menu  
)
clean_df = create_total_students(clean_df)

clean_df = create_average_score(clean_df)

clean_df = create_percentage(clean_df)

clean_df = create_grade(clean_df)

clean_df = create_subject_insights(clean_df)

clean_df = risk_mask(clean_df)

clean_df = engagement_mask(clean_df)

clean_df = student_mask(clean_df)

clean_df = create_student_rank(clean_df)

report = generate_summary_report(clean_df)

correlation = generate_correlation(clean_df)

dashboard = build_dashboard(clean_df)

# print(display_report(report))
 
 # Generate Explanation Columns
#  -----------------------------------------------
clean_df["risk_contributing_factors"] = clean_df.apply(
    generate_risk_contributing_factors,
    axis=1
)

clean_df["engagement_primary_concern"] = clean_df.apply(
    generate_engagement_primary_concern,
    axis=1
)

clean_df["risk_primary_concern"] = clean_df.apply(
    generate_risk_primary_concern,
    axis=1
)

clean_df["engagement_contributing_factors"] = clean_df.apply(
    generate_engagement_contributing_factors,
    axis=1
)

clean_df["status_primary_concern"] = clean_df.apply(
    generate_status_primary_concern,
    axis=1
)

clean_df["risk_reason_short"] = clean_df.apply(
    lambda row: generate_risk_reason(row, "short"),
    axis=1
)

clean_df["risk_reason_detailed"] = clean_df.apply(
    lambda row: generate_risk_reason(row, "detailed"),
    axis=1
)

clean_df["engagement_reason_short"] = clean_df.apply(
    lambda row: generate_engagement_reason(row, "short"),
    axis=1
)

clean_df["engagement_reason_detailed"] = clean_df.apply(
    lambda row: generate_engagement_reason(row, "detailed"),
    axis=1
)

clean_df["status_reason_short"] = clean_df.apply(
    lambda row: generate_status_reason(row, "short"),
    axis=1
)

clean_df["status_reason_detailed"] = clean_df.apply(
    lambda row: generate_status_reason(row, "detailed"),
    axis=1
)

clean_df["status_recommended_action_short"] = clean_df.apply(
    lambda row: generate_status_recommended_action(row, "short"),
    axis=1
)

clean_df["status_recommended_action_detailed"] = clean_df.apply(
    lambda row: generate_status_recommended_action(row, "detailed"),
    axis=1
)


# ------------------------------

# print(correlation)

# # 3. Visualization / Insights 
# visualization.risk_bar_charts(clean_df)
# visualization.engagement_bar_charts(clean_df)

# print(clean_df["status_recommended_action_detailed"].head(5))
# print(clean_df.head(1))

# Call the function and print the final returned text block
# final_report = display_student_report(clean_df, roll_no=17, detail_level="detailed")
# print(final_report)

# search_report = search_student_menu(clean_df,123, 'detailed')
# print(search_report)

# print(dashboard)

cli_based_menu = run_menu(clean_df)
print(cli_based_menu)