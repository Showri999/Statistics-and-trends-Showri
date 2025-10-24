"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
 if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""
from corner import corner
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns


def plot_relational_plot(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x='bmi', y='blood_glucose_level', hue='diabetes', palette='coolwarm', ax=ax)
    plt.title('Relationship between BMI and Blood Glucose Level')
    plt.xlabel('BMI')
    plt.ylabel('Blood Glucose Level')
    plt.tight_layout()
    plt.savefig('relational_plot.png')
    plt.show()
    return


def plot_categorical_plot(df):
    fig, ax = plt.subplots(figsize=(6, 5))
    avg_glucose = df.groupby('gender')['blood_glucose_level'].mean().reset_index()
    sns.barplot(data=avg_glucose, x='gender', y='blood_glucose_level', hue='gender', palette='pastel', legend=False, ax=ax)
    plt.title('Average Blood Glucose Level by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Average Blood Glucose Level')
    plt.tight_layout()
    plt.savefig('categorical_plot.png')
    plt.show()
    return


def plot_statistical_plot(df):
    fig, ax = plt.subplots(figsize=(10, 8))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    plt.title('Correlation Heatmap of Features')
    plt.tight_layout()
    plt.savefig('statistical_plot.png')
    plt.show()
    return


def statistical_analysis(df, col: str):
    data = df[col].dropna()
    mean = data.mean()
    stddev = data.std()
    skew = ss.skew(data)
    excess_kurtosis = ss.kurtosis(data)
    return mean, stddev, skew, excess_kurtosis


def preprocessing(df):
   print("Initial dataset shape:", df.shape)

    # Drop duplicates and missing values
    df = df.drop_duplicates().dropna()

    # Convert categorical columns to lowercase
    if 'gender' in df.columns:
        df['gender'] = df['gender'].str.lower()

    print("After cleaning:", df.shape)
    print(df.describe())
    print("\nCorrelation matrix:\n", df.corr(numeric_only=True))
    return df


def writing(moments, col):
    print(f'\nFor the attribute "{col}":')
    print(f'Mean = {moments[0]:.2f}, '
          f'Standard Deviation = {moments[1]:.2f}, '
          f'Skewness = {moments[2]:.2f}, '
          f'Excess Kurtosis = {moments[3]:.2f}')
    skewness = "right-skewed" if moments[2] > 0 
 else "left-skewed" if moments[2] < 0 
 else "not skewed"
    kurtosis_type = "leptokurtic" if moments[3] > 0 
 else "platykurtic" 
 if moments[3] < 0 else "mesokurtic"
    print(f"The data is {skewness} and {kurtosis_type}.")
    return


def main():
    df = pd.read_csv('data.csv')
    df = preprocessing(df)
    col = 'blood_glucose_level'
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments = statistical_analysis(df, col)
    writing(moments, col)
    return


if __name__ == '__main__':
    main()
