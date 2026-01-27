import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def analyze_purchase_data(file_path):
    print("\n--- A1: Purchase Data Analysis ---")

    df = pd.read_excel(file_path, sheet_name="Purchase data")

    features = df[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']].values
    target = df['Payment (Rs)'].values

    print("Feature Matrix:\n", features)
    print("Target Vector:\n", target)

    print("Vector Space Dimension:", features.shape[1])
    print("Total Records:", features.shape[0])
    print("Rank of Feature Matrix:", np.linalg.matrix_rank(features))

    pseudo_inverse = np.linalg.pinv(features)
    item_costs = pseudo_inverse.dot(target)

    print("Estimated Item Costs [Candies, Mangoes, Milk]:")
    print(item_costs)


def classify_customers_by_payment(file_path):
    print("\n--- A2: Rich / Poor Classification ---")

    df = pd.read_excel(file_path, sheet_name="Purchase data")

    df['Class'] = df['Payment (Rs)'].apply(
        lambda val: "RICH" if val > 200 else "POOR"
    )

    print(df[['Payment (Rs)', 'Class']])
    print("Rule Applied: Payment > 200 = RICH, else POOR")


def analyze_irctc_stock_data(file_path):
    print("\n--- A3: IRCTC Stock Analysis ---")

    df = pd.read_excel(file_path, sheet_name="IRCTC Stock Price")
    prices = df['Price'].values

    print("Mean Price:", np.mean(prices))
    print("Variance:", np.var(prices))

    def manual_mean(arr):
        total = 0
        for x in arr:
            total += x
        return total / len(arr)

    def manual_variance(arr):
        m = manual_mean(arr)
        total = 0
        for x in arr:
            total += (x - m) ** 2
        return total / len(arr)

    print("Custom Mean:", manual_mean(prices))
    print("Custom Variance:", manual_variance(prices))

    wednesday_data = df[df['Day'] == 'Wed']
    print("Wednesday Mean Price:", wednesday_data['Price'].mean())

    april_data = df[df['Month'] == 'Apr']
    print("April Mean Price:", april_data['Price'].mean())

    probability_loss = len(df[df['Chg%'] < 0]) / len(df)
    print("Probability of Loss:", probability_loss)

    wednesday_profit = wednesday_data[wednesday_data['Chg%'] > 0]
    print("Probability of Profit on Wednesday:",
          len(wednesday_profit) / len(df))

    print("Conditional P(Profit | Wednesday):",
          len(wednesday_profit) / len(wednesday_data))

    plt.scatter(df['Day'], df['Chg%'])
    plt.title("Change % vs Day")
    plt.xlabel("Day")
    plt.ylabel("Change %")
    plt.show()


def explore_thyroid_dataset(file_path):
    print("\n--- A4: Thyroid Data Exploration ---")

    df = pd.read_excel(file_path, sheet_name="thyroid0387_UCI")

    print("Column Data Types:\n", df.dtypes)
    print("\nMissing Values:\n", df.isnull().sum())
    print("\nStatistical Summary:\n", df.describe())


def compute_jaccard_and_smc(file_path):
    print("\n--- A5: Jaccard and Simple Matching Coefficient ---")

    df = pd.read_excel(file_path, sheet_name="thyroid0387_UCI")

    numeric_df = df.select_dtypes(include=[np.number]).fillna(0)
    binary_df = (numeric_df != 0).astype(int)

    vec1 = binary_df.iloc[0].values
    vec2 = binary_df.iloc[1].values

    f11 = np.sum((vec1 == 1) & (vec2 == 1))
    f10 = np.sum((vec1 == 1) & (vec2 == 0))
    f01 = np.sum((vec1 == 0) & (vec2 == 1))
    f00 = np.sum((vec1 == 0) & (vec2 == 0))

    jaccard_denominator = f01 + f10 + f11
    jaccard = f11 / jaccard_denominator if jaccard_denominator != 0 else 1.0

    smc_denominator = f00 + f01 + f10 + f11
    smc = (f11 + f00) / smc_denominator if smc_denominator != 0 else 0.0

    print("f00 =", f00, "f01 =", f01, "f10 =", f10, "f11 =", f11)
    print("Jaccard Coefficient:", jaccard)
    print("Simple Matching Coefficient:", smc)


def compute_cosine_similarity(file_path):
    print("\n--- A6: Cosine Similarity ---")

    df = pd.read_excel(file_path, sheet_name="thyroid0387_UCI")
    numeric_data = df.select_dtypes(include=[np.number]).fillna(0)

    vec1 = numeric_data.iloc[0].values
    vec2 = numeric_data.iloc[1].values

    denominator = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    cosine_similarity = (
        np.dot(vec1, vec2) / denominator if denominator != 0 else 0.0
    )

    print("Cosine Similarity:", cosine_similarity)


def plot_similarity_heatmap(file_path):
    print("\n--- A7: Similarity Heatmap ---")

    df = pd.read_excel(file_path, sheet_name="thyroid0387_UCI")
    numeric_data = df.select_dtypes(include=[np.number]).fillna(0).iloc[:20]

    similarity_matrix = np.zeros((20, 20))

    for i in range(20):
        for j in range(20):
            a = numeric_data.iloc[i].values
            b = numeric_data.iloc[j].values
            denom = np.linalg.norm(a) * np.linalg.norm(b)

            similarity_matrix[i][j] = (
                np.dot(a, b) / denom if denom != 0 else 0.0
            )

    sns.heatmap(similarity_matrix, annot=False)
    plt.title("Cosine Similarity Heatmap")
    plt.show()


def run_lab2_analysis():
    file_path = "Lab2 Session Data.xlsx"

    analyze_purchase_data(file_path)
    classify_customers_by_payment(file_path)
    analyze_irctc_stock_data(file_path)
    explore_thyroid_dataset(file_path)
    compute_jaccard_and_smc(file_path)
    compute_cosine_similarity(file_path)
    plot_similarity_heatmap(file_path)


if __name__ == "__main__":
    run_lab2_analysis()
