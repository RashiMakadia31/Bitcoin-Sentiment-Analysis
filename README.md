# Bitcoin-Sentiment-Analysis

This project investigates the relationship between Bitcoin market sentiment (as captured by the Fear & Greed Index) and trader performance on the Hyperliquid platform. By analyzing historical trading data alongside market sentiment classifications, we aim to uncover behavioral patterns that can inform smarter trading strategies.

## Objective

To analyze how shifts in market sentiment (Fear, Greed, etc.) influence trading activity and profitability. The project also identifies how individual traders perform under different emotional market states.

## Datasets Used

1. **Bitcoin Market Sentiment Dataset**
   - Columns: `date`, `classification` (e.g., Fear, Greed, Extreme Fear), `value`
   - Source: Fear and Greed Index data

2. **Hyperliquid Historical Trader Data**
   - Columns include: `account`, `symbol`, `execution price`, `size`, `side`, `time`, `closedPnL`, `leverage`, and more
   - Contains trade-level logs for each account

## Methodology

### 1. Data Preprocessing
- Parsed and formatted date/time fields
- Normalized timestamp precision
- Handled missing or mismatched sentiment records

### 2. Dataset Merging
- Merged trade data with sentiment data on the date column
- Aligned trades with corresponding market sentiment classification

### 3. Feature Engineering
- Computed trade-level and daily cumulative PnL
- Calculated:
  - Average PnL by sentiment classification
  - Trade count per sentiment
  - Trader-level performance per sentiment

## Visual Insights

### Trade Volume per Sentiment

![Trade Volume](./download.png)

- Highest trading volume observed on "Fear" days
- Lowest volume on "Extreme Fear" days

### Average PnL per Sentiment

![Average PnL](./download%20(1).png)

- Traders were most profitable on "Extreme Greed" days
- Lowest average profitability observed on "Extreme Fear" and "Neutral" days

## Trader-Specific Insights

- Identified top-performing traders under different sentiment states
- Found that some traders consistently outperformed under specific sentiment conditions (e.g., high PnL under Fear or Greed)

## Conclusion

Market sentiment has a measurable effect on both trade volume and trader profitability. This analysis reveals that traders tend to perform better in "Extreme Greed" conditions and are less profitable in "Extreme Fear" and "Neutral" markets. The findings could help traders optimize strategies based on prevailing sentiment.

## Tools Used

- Python (Pandas, Seaborn, Matplotlib)
- Google Colab
- CSV datasets from Hyperliquid and Fear/Greed Index



