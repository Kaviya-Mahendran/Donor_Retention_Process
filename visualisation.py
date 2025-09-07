import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_retention_curve(df):
    """
    Creates and displays a cohort retention curve.
    """
    # Define a reference date for the end of the analysis period
    # This should be a recent date, or the latest date in your data
    reference_date = pd.to_datetime('2024-12-31')

    # Convert 'DonationDate' and 'FirstDonationDate' to datetime if not already done
    df['DonationDate'] = pd.to_datetime(df['DonationDate'])
    df['FirstDonationDate'] = pd.to_datetime(df['FirstDonationDate'])

    # Create a 'CohortYear' column based on the year of the first donation
    df['CohortYear'] = df['FirstDonationDate'].dt.year

    # Create a 'DonationYear' column based on the year of each donation
    df['DonationYear'] = df['DonationDate'].dt.year

    # Calculate the number of unique donors in each cohort and donation year
    retention_counts = df.groupby(['CohortYear', 'DonationYear'])['DonorID'].nunique().reset_index()

    # Calculate the size of the initial cohort (number of donors in their first year)
    cohort_sizes = retention_counts[retention_counts['CohortYear'] == retention_counts['DonationYear']].set_index('CohortYear')['DonorID']

    # Create a pivot table for the retention matrix
    retention_pivot = retention_counts.pivot(index='CohortYear', columns='DonationYear', values='DonorID')

    # Divide by cohort size to get the retention rate as a percentage
    retention_rates = retention_pivot.divide(cohort_sizes, axis=0) * 100

    # Plot the retention curves
    plt.figure(figsize=(12, 8))
    sns.lineplot(data=retention_rates.T, markers=True, style='CohortYear', dashes=False)
    plt.title('Donor Retention Curves by Cohort Year', fontsize=16)
    plt.xlabel('Donation Year', fontsize=12)
    plt.ylabel('Retention Rate (%)', fontsize=12)
    plt.grid(True)
    plt.legend(title='Cohort Year', loc='upper right')
    plt.show()

def create_retention_curve(df):
    """
    Creates and displays a cohort retention curve.
    """
    # Define a reference date for the end of the analysis period
    # This should be a recent date, or the latest date in your data
    reference_date = pd.to_datetime('2024-12-31')

    # Convert 'DonationDate' and 'FirstDonationDate' to datetime if not already done
    df['DonationDate'] = pd.to_datetime(df['DonationDate'])
    df['FirstDonationDate'] = pd.to_datetime(df['FirstDonationDate'])

    # Create a 'CohortYear' column based on the year of the first donation
    df['CohortYear'] = df['FirstDonationDate'].dt.year

    # Create a 'DonationYear' column based on the year of each donation
    df['DonationYear'] = df['DonationDate'].dt.year

    # Calculate the number of unique donors in each cohort and donation year
    retention_counts = df.groupby(['CohortYear', 'DonationYear'])['DonorID'].nunique().reset_index()

    # Calculate the size of the initial cohort (number of donors in their first year)
    cohort_sizes = retention_counts[retention_counts['CohortYear'] == retention_counts['DonationYear']].set_index('CohortYear')['DonorID']

    # Create a pivot table for the retention matrix
    retention_pivot = retention_counts.pivot(index='CohortYear', columns='DonationYear', values='DonorID')

    # Divide by cohort size to get the retention rate as a percentage
    retention_rates = retention_pivot.divide(cohort_sizes, axis=0) * 100

    # Plot the retention curves
    plt.figure(figsize=(12, 8))
    sns.lineplot(data=retention_rates.T, markers=True, dashes=False) # 'style' argument was removed here
    plt.title('Donor Retention Curves by Cohort Year', fontsize=16)
    plt.xlabel('Donation Year', fontsize=12)
    plt.ylabel('Retention Rate (%)', fontsize=12)
    plt.grid(True)
    plt.legend(title='Cohort Year', loc='upper right')
    plt.show()

# To run the visualizations, you would need to load the data first.
if __name__ == '__main__':
    try:
        # Correct file name
        df_for_plots = pd.read_csv('donor_dataset.csv')
        create_retention_curve(df_for_plots)
        create_donation_by_channel_chart(df_for_plots)
    except FileNotFoundError:
        print("Error: Please make sure 'donor_dataset.csv' is in the same directory.")
    except Exception as e:
        print(f"An error occurred during visualization: {e}")