import matplotlib.pyplot as plt

def risk_bar_charts(df):
    plt.figure() # Added to prevent window locking
    risk_counts = df["risk_flag"].value_counts()
    risk_counts.plot(kind="bar", color="tomato")
    plt.title("Risk Flag Distribution")
    plt.xlabel("Risk Level")
    plt.ylabel("Number of Students")
    plt.show()

def engagement_bar_charts(df):
    plt.figure() # Added to prevent window locking
    engagement_counts = df["engagement_level"].value_counts()
    engagement_counts.plot(kind="bar", color="skyblue")
    plt.title("Engagement Level Distribution")
    plt.xlabel("Engagement Level")
    plt.ylabel("Number of Students")
    plt.show()
