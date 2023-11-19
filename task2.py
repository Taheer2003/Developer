import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    def _init_(self, data_path):
        self.df = pd.read_csv(data_path)

    def explore_data(self):
        print(self.df.head())  # Display the first few rows of the dataset
        print(self.df.info())  # Display information about the dataset

    def visualize_columns(self, columns_to_analyze):
        for column in columns_to_analyze:
            plt.figure(figsize=(12, 6))  # Adjust the figure size

            if self.df[column].dtype == 'int64' or self.df[column].dtype == 'float64':
                # Create a histogram for numeric columns
                sns.histplot(data=self.df, x=column, kde=True)
                plt.title(f'Histogram of {column}')
                plt.xlabel('Value')
                plt.ylabel('Frequency')
            else:
                # Create a bar plot for categorical columns
                if self.df[column].nunique() > 10:
                    top_categories = self.df[column].value_counts().nlargest(10).index
                    self.df[column] = self.df[column].where(self.df[column].isin(top_categories), 'Other')

                sns.countplot(data=self.df, x=column, palette='viridis', saturation=0.75)
                plt.title(f'Count of {column}')
                plt.xlabel('Categories')
                plt.ylabel('Count')
                plt.xticks(rotation=45, ha='right')  # Adjust rotation and horizontal alignment

            plt.tight_layout()  # Adjust layout for better spacing
            plt.show()

# Example usage
data_visualizer = DataVisualizer('Netflix.csv')
data_visualizer.explore_data()
data_visualizer.visualize_columns(['show_id', 'type', 'title', 'director', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in'])