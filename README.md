📈 Intraday Alpha Signal Generator
---

## 🧠 Background & Overview

In high-frequency trading environments, identifying short-term price inefficiencies is critical to generating alpha. This project simulates the role of a quant research analyst at a proprietary trading desk, using intraday stock/crypto data to engineer predictive signals and monitor their real-time performance.

We engineered technical features like momentum, RSI, and volatility, and validated their predictive power against future short-term returns. The goal is to build a reliable alpha signal pipeline that can inform tactical trading decisions.

---

## 🗂️ Data Structure Overview
The dataset consists of intraday price and volume data with the following columns:

- `timestamp`
- `open`, `high`, `low`, `close`
- `volume`

  Feature columns:
- `rsi_14`, `ma_5`, `ma_15`, `momentum_5`, `volatility_15`

Label:
- `future_return_5min` (calculated)
- `signal_label` (1 = buy, -1 = sell, 0 = hold)

📌 **Entity Relationship Diagram (ERD):**

![ERD](visuals/erd_diagram.png)

---

## 📊 Executive Summary

- Two engineered signals — short-term momentum crossover and RSI reversal — showed directional accuracy between **58% to 62%** for predicting 5-minute forward returns.
- Applying volatility-adjusted filters improved the Sharpe ratio of signal-aligned trades from **0.8 to 1.9**.
- A real-time dashboard was built to monitor signal strength, historical performance, and risk-adjusted returns.

📸 **Dashboard Snapshot:**

![Alpha Dashboard](visuals/charts/snapshot_dashboard.png)

---

## 🔍 Insights Deep Dive

### 1. 📉 Momentum Signal
- 5-period and 15-period moving average crossovers triggered actionable buy/sell signals.
- Cumulative return of signal-driven strategy: **+4.2% over 30 days** (vs baseline: +1.7%).

### 2. 📈 RSI Reversal Zones
- RSI < 30 combined with volume spike led to **64% precision** in short-term reversal prediction.
- Most effective during range-bound market conditions.

### 3. ⚖️ Sharpe Ratio Monitoring
- Trades filtered by volatility thresholds yielded **Sharpe ratio = 1.9**, compared to 0.8 for unfiltered signals.

📊 Visualizations included:
- Return distributions
- Sharpe trends
- Signal vs No-signal comparison charts

---

## 🧩 Recommendations

- ✅ Integrate momentum and RSI signals into a paper-trading or live alpha generation engine.
- ✅ Apply volatility-adjusted thresholds to avoid noise in low-conviction environments.
- ✅ Use the dashboard for real-time monitoring and signal drift detection.
- 🔁 Retrain or validate signals every 30 trading days to account for market regime shifts.

---

intraday-alpha-signal-generator/
│
├── README.md
├── data/
│   ├── raw/               # Raw intraday datasets (e.g., Binance, Polygon)
│   └── processed/         # Feature-engineered datasets
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│   └── signal_generation.ipynb
│   └── signal_evaluation.ipynb
│
├── src/
│   ├── etl.py             # Data loading and cleaning scripts
│   ├── features.py        # Momentum, RSI, volatility feature engineering
│   ├── labeling.py        # Logic to label future return signals
│   └── evaluation.py      # Accuracy, Sharpe ratio, performance evaluation
│
├── dashboard/
│   └── dashboard.ipynb    # Plotly or Streamlit dashboard code
│
├── visuals/
│   └── erd_diagram.png    # ERD or system overview diagram
│   └── charts/            # Exported plots/images
│
├── requirements.txt

## ⚙️ Tech Stack

- Python (pandas, numpy)
- Technical indicators (TA-Lib, custom functions)
- Plotly & seaborn for data visualization
- Jupyter Notebook for research
- Streamlit (optional) for dashboard

---

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/intraday-alpha-signal-generator.git

# 2. Navigate and create virtual environment
cd intraday-alpha-signal-generator
python -m venv venv && source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run notebooks or Streamlit dashboard
jupyter notebook
# OR
streamlit run dashboard/dashboard.ipynb

---

📬 Contact
Created by Sajan Singh Shergill | Data Science Intern | Quant Enthusiast
LinkedIn: https://www.linkedin.com/in/sajanshergill/
Email: sajansshergill@gmail.com / ss54534n@pace.edu
