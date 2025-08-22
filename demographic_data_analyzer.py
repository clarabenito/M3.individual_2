import pandas as pd


def calculate_demographic_data(print_data: bool = True):
    df = pd.read_csv("adult.data.csv")

    df.columns = df.columns.str.strip()
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()

    race_count = df["race"].value_counts()

    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    percentage_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)

    higher_ed = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    lower_ed = ~higher_ed

    higher_education_rich = round(
        (
            df[higher_ed & (df["salary"] == ">50K")].shape[0]
            / df[higher_ed].shape[0]
        ) * 100,
        1,
    )

    lower_education_rich = round(
        (
            df[lower_ed & (df["salary"] == ">50K")].shape[0]
            / df[lower_ed].shape[0]
        ) * 100,
        1,
    )

    min_work_hours = df["hours-per-week"].min()

    min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round((min_workers["salary"] == ">50K").mean() * 100, 1)

    country_totals = df["native-country"].value_counts()
    country_rich = df[df["salary"] == ">50K"]["native-country"].value_counts()
    rich_ratio = (country_rich / country_totals * 100).fillna(0)

    highest_earning_country = rich_ratio.idxmax()
    highest_earning_country_percentage = round(rich_ratio.max(), 1)

    india_rich = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
    top_IN_occupation = india_rich["occupation"].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
