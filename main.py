import pandas as pd
fear_greed_df = pd.read_csv('/content/fear_greed_index.csv')
historical_df = pd.read_csv('/content/historical_data.csv')


fear_greed_df.head()
historical_df.head()


fear_greed_df['Date'] = pd.to_datetime(fear_greed_df['Date'])
historical_df['Date'] = pd.to_datetime(
historical_df['Timestamp IST'], format="%d-%m-%Y %H:%M").dt.date
historical_df['Date'] = pd.to_datetime(historical_df['Date'])
print(fear_greed_df[['Date', 'classification']].head())
print(historical_df[['Timestamp IST', 'Date']].head())


merged_df = pd.merge(
      historical_df, fear_greed_df[['Date', 'classification', 'value']],
          on='Date',
          how='left'
)
missing_sentiment = merged_df['classification'].isnull().sum()
print(f"Missing sentiment rows: {missing_sentiment}")


merged_df.dropna(subset=['classification'], inplace=True)
print(merged_df[['Date', 'Account', 'Coin', 'Closed PnL', 'classification']].head())


merged_df['Date_str'] = merged_df['Date'].astype(str)
daily_pnl = merged_df.groupby(['Account', 'Date_str'])['Closed PnL'].sum().reset_index()
daily_pnl.rename(columns={'Closed PnL': 'Daily_Cumulative_PnL'}, inplace=True)
merged_df = pd.merge(
      merged_df, daily_pnl, on=['Account', 'Date_str'], how='left'
)
sentiment_trade_count = merged_df.groupby(['classification'])['Closed PnL'].count().reset_index()
sentiment_trade_count.rename(columns={'Closed PnL': 'Trade_Count'}, inplace=True)


avg_pnl_by_sentiment = merged_df.groupby('classification')['Closed PnL'].mean().reset_index()
avg_pnl_by_sentiment.rename(columns={'Closed PnL': 'Average_PnL'}, inplace=True)


sentiment_summary = pd.merge(sentiment_trade_count, avg_pnl_by_sentiment, on='classification')


print(sentiment_summary)


import matplotlib.pyplot as plt
import seaborn as sns


sns.set(style="dark")
plt.figure(figsize=(12, 5))


plt.subplot(1, 2, 1)
sns.barplot(data=sentiment_summary, x='classification', y='Average_PnL', palette='coolwarm')
plt.title("Average PnL per Sentiment")
plt.xticks(rotation=45)
plt.ylabel("Average PnL")


plt.subplot(1, 2, 2)
sns.barplot(data=sentiment_summary, x='classification', y='Trade_Count', palette='viridis')
plt.title("Trade Volume per Sentiment")
plt.xticks(rotation=45)
plt.ylabel("Number of Trades")

plt.tight_layout()
plt.show()













