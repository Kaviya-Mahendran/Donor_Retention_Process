import pandas as pd
import os
def save_results_to_file(df):
    """
    Performs data analysis and saves all results to text and CSV files.
    """
    # Data Cleaning & Transformation (Steps 2-5 from the case study)
    df['DonationDate'] = pd.to_datetime(df['DonationDate'])
    df['FirstDonationDate'] = pd.to_datetime(df['FirstDonationDate'])
    df['DonationYear'] = df['DonationDate'].dt.year
    df['CohortYear'] = df['FirstDonationDate'].dt.year
    # Data Analysis
    total_raised = df['DonationAmount'].sum()
    avg_gift = df['DonationAmount'].mean()
    donations_by_year = df.groupby('DonationYear')['DonationAmount'].sum()
    donations_by_channel = df.groupby('Channel')['DonationAmount'].sum()
    at_risk_donors = df.groupby('DonorID').filter(lambda x: x['DonationDate'].max() < pd.Timestamp.now() - pd.DateOffset(months=12))['DonorID'].nunique()
    # Cohort Retention Analysis
    retention_counts = df.groupby(['CohortYear', 'DonationYear'])['DonorID'].nunique().reset_index()
    cohort_sizes = retention_counts[retention_counts['CohortYear'] == retention_counts['DonationYear']].set_index('CohortYear')['DonorID']
    retention_pivot = retention_counts.pivot(index='CohortYear', columns='DonationYear', values='DonorID')
    retention_rates = retention_pivot.divide(cohort_sizes, axis=0) * 100
    # Save results to a text file
    output_text_file = 'donor_analysis_results.txt'
    with open(output_text_file, 'w') as f:
        f.write("Donor Analysis Report\n")
        f.write("========================\n\n")
        f.write(f"Total raised: £{total_raised:,.2f}\n")
        f.write(f"Average gift: £{avg_gift:,.2f}\n")
        f.write(f"Number of 'at-risk' donors: {at_risk_donors}\n\n")
        f.write("Donations by Year:\n")
        f.write(donations_by_year.to_string() + "\n\n")
        f.write("Donations by Channel:\n")
        f.write(donations_by_channel.to_string() + "\n\n")
        f.write("Retention Rate Matrix (%):\n")
        f.write(retention_rates.to_string() + "\n")
    # Save the Cohort Analysis to a separate CSV file
    output_csv_file = 'donor_retention_cohort_analysis.csv'
    retention_rates.to_csv(output_csv_file)
    print(f"Analysis results saved to: {os.path.abspath(output_text_file)}")
    print(f"Cohort analysis saved to: {os.path.abspath(output_csv_file)}")
if __name__ == '__main__':
    try:
        # Load the data with the correct file name
        df = pd.read_csv('donor_dataset.csv')
        save_results_to_file(df)
    except FileNotFoundError:
        print("Error: The file 'donor_dataset.csv' was not found. Please make sure it's in the same directory.")
    except Exception as e:
        print(f"An error occurred: {e}")