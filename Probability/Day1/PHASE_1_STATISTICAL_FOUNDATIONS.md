# PHASE 1: STATISTICAL & MATHEMATICAL FOUNDATIONS
## Weeks 1-3: Build Your Quant Trading Brain

---

## OVERVIEW
**Goal:** Understand the math and statistics behind successful trading
**Duration:** 3 weeks
**Time Commitment:** 2-3 hours daily
**Why this matters:** 80% of quant job interviews test these concepts

This phase is NOT optional. Professional traders think in probabilities, not certainties.

---

## SECTION 1.1: PROBABILITY & STATISTICS BOOTCAMP

### Week 1: Fundamental Concepts

#### Day 1-2: Distributions & Probability
**What to Learn:**
- Normal distribution (bell curve)
- Standard deviation (σ) - measure of spread
- Mean (μ) - average
- Variance (σ²) - spread squared
- Z-scores - how many σ away from mean

**Why it matters for trading:**
- If return distribution is normal, you can calculate risk
- 68% of returns fall within 1σ of mean
- 95% within 2σ
- This helps predict drawdowns

**Practice Exercise 1:**
```python
import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 trading returns (simulated)
returns = np.random.normal(mean=0.001, std=0.02, size=1000)  # 0.1% mean, 2% std

mean = np.mean(returns)
std = np.std(returns)

print(f"Mean return: {mean:.4f}")
print(f"Std dev: {std:.4f}")
print(f"Probability of return between {mean-std:.4f} and {mean+std:.4f}: 68%")

# Visualize
plt.hist(returns, bins=50, edgecolor='black')
plt.axvline(mean, color='r', linestyle='--', label='Mean')
plt.axvline(mean - std, color='g', linestyle='--', label='±1σ')
plt.axvline(mean + std, color='g', linestyle='--')
plt.legend()
plt.title('Distribution of Trading Returns')
plt.show()
```

**Apply to your trading:**
- Your strategy returns should be roughly normal
- If they're not, something is wrong (overfitting, survivorship bias)

---

#### Day 3-4: Hypothesis Testing
**What to Learn:**
- Null hypothesis (H0): "My strategy has NO edge"
- Alternative hypothesis (H1): "My strategy IS profitable"
- p-value: Probability that result is due to luck, not skill
- Significance level: α = 0.05 (5% threshold)

**The key question:** Is my +30% return due to skill or luck?

**Practice Exercise 2:**
```python
from scipy import stats

# Your strategy returns over 100 trades
strategy_returns = np.array([0.02, -0.01, 0.03, 0.01, -0.005, ...])  # Your real data

# Test 1: Is mean return significantly different from 0?
t_statistic, p_value = stats.ttest_1samp(strategy_returns, 0)

print(f"T-statistic: {t_statistic:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("✓ Your returns are statistically significant (not luck)")
else:
    print("✗ Your returns might be due to luck, need more data")
```

**Why it matters:**
- Quant firms ask: "How do you know this isn't luck?"
- Answer: "P-value tells me probability it's random"

---

#### Day 5-7: Correlation & Covariance
**What to Learn:**
- Correlation: How two things move together (-1 to +1)
- Covariance: Shared variance
- Correlation matrix: Multiple assets' relationships

**Practice Exercise 3:**
```python
import pandas as pd

# Get 2 stocks' returns
returns = pd.DataFrame({
    'TCS': [0.01, -0.02, 0.03, 0.01, -0.01, 0.02, 0.00],
    'INFY': [0.02, -0.01, 0.02, 0.01, 0.00, 0.01, 0.01],
    'NIFTY': [0.015, -0.015, 0.025, 0.01, -0.005, 0.015, 0.005]
})

# Calculate correlation matrix
correlation = returns.corr()
print(correlation)

# Interpretation:
# 1.0 = move together perfectly
# 0.0 = no relationship
# -1.0 = move opposite

# For portfolio: Choose assets with low correlation
# If both go down together → portfolio crashes
# If they move differently → portfolio is protected
```

**Why it matters:**
- Portfolio diversification depends on correlation
- If your strategies correlate, you don't reduce risk
- If they correlate negatively, you hedge

---

### Week 2: Statistical Inference

#### Day 1-2: Confidence Intervals
**What to Learn:**
- Confidence interval: Range where true value likely lies
- 95% CI: 95% chance true mean is in this range
- Margin of error

**Practice Exercise 4:**
```python
from scipy import stats

# Your strategy's returns
returns = np.array([0.01, -0.01, 0.02, 0.015, -0.005, 0.012, 0.008])

# Calculate 95% confidence interval
mean = np.mean(returns)
std_error = stats.sem(returns)  # Standard error of mean
ci = stats.t.interval(0.95, len(returns)-1, loc=mean, scale=std_error)

print(f"95% Confidence Interval: [{ci[0]:.4f}, {ci[1]:.4f}]")
print(f"This means: 95% chance true mean return is between {ci[0]:.4f} and {ci[1]:.4f}")
```

**Trading application:**
- Don't say "I'll make 50% annually"
- Say "With 95% confidence, I'll make between 15-35% annually"
- This is how professionals think

---

#### Day 3-4: Type I & II Errors
**What to Learn:**
- Type I Error: False positive (trade good strategy as if bad)
- Type II Error: False negative (ignore good strategy as if bad)
- Choose which error costs more

**For trading:**
- Type I: Reject good strategy (miss profits)
- Type II: Accept bad strategy (lose money)
- Which is worse? Usually Type II (losing money is worse than missing profits)

**Practice Exercise 5:**
```python
# Example: Is this strategy profitable?
returns = [0.01, -0.01, 0.02, 0.01, 0.005]  # 10 trades
mean_return = np.mean(returns)

# If we set strict threshold (95% confidence needed):
# Risk: Reject good strategy (Type I error)
# Benefit: Only trade proven winners

# If we set loose threshold (80% confidence ok):
# Risk: Trade bad strategy (Type II error)  
# Benefit: Trade more opportunities

# In trading: Be conservative, require high confidence
# Cost of Type II (bad strategy loss) > Type I (missed profit)
```

---

#### Day 5-7: Statistical Power
**What to Learn:**
- Power: Ability to detect real effect
- Sample size matters: More data = higher power
- Need enough data to prove edge exists

**Practice Exercise 6:**
```python
# How many trades needed to prove 55% win rate is real?
from scipy.stats import binom_test

# After 100 trades: 55 wins, 45 losses
p_value = binom_test(55, 100, 0.5, alternative='greater')
print(f"P-value with 100 trades, 55% win rate: {p_value:.4f}")

# After 30 trades: 17 wins, 13 losses  
p_value = binom_test(17, 30, 0.5, alternative='greater')
print(f"P-value with 30 trades, 56% win rate: {p_value:.4f}")

# Lesson: Need ~100+ trades to prove edge statistically
```

---

## SECTION 1.2: PORTFOLIO THEORY

### Week 2 (continued): Portfolio Concepts

#### Day 1-2: Expected Return & Risk
**What to Learn:**
- Expected return = weighted average of returns
- Risk (volatility) = standard deviation of returns
- Risk-free rate = 5-6% (Indian bonds)

**Practice Exercise 7:**
```python
# Portfolio with 2 stocks
weights = {'TCS': 0.6, 'INFY': 0.4}
returns = {'TCS': 0.12, 'INFY': 0.15}  # Expected annual returns

portfolio_return = weights['TCS'] * returns['TCS'] + weights['INFY'] * returns['INFY']
print(f"Expected portfolio return: {portfolio_return:.2%}")

# Volatility (risk)
volatility = {'TCS': 0.18, 'INFY': 0.20}  # Annual volatility
portfolio_volatility = np.sqrt(
    (weights['TCS']**2 * volatility['TCS']**2) +
    (weights['INFY']**2 * volatility['INFY']**2) +
    (2 * weights['TCS'] * weights['INFY'] * volatility['TCS'] * volatility['INFY'] * 0.3)  # correlation=0.3
)
print(f"Portfolio volatility: {portfolio_volatility:.2%}")
```

---

#### Day 3-4: Sharpe Ratio
**What to Learn:**
- Sharpe Ratio = (Return - Risk-Free Rate) / Volatility
- Measures return per unit of risk
- Higher Sharpe = better risk-adjusted returns

**Practice Exercise 8:**
```python
# Compare two strategies
strategy_a = {'return': 0.25, 'volatility': 0.20}  # 25% return, 20% risk
strategy_b = {'return': 0.15, 'volatility': 0.08}  # 15% return, 8% risk

risk_free_rate = 0.05

sharpe_a = (strategy_a['return'] - risk_free_rate) / strategy_a['volatility']
sharpe_b = (strategy_b['return'] - risk_free_rate) / strategy_b['volatility']

print(f"Strategy A Sharpe Ratio: {sharpe_a:.2f}")
print(f"Strategy B Sharpe Ratio: {sharpe_b:.2f}")

# Result: Strategy B has better risk-adjusted returns
# More return per unit of risk taken
```

**Why it matters:**
- 25% return sounds good, but if it requires 20% risk, it's bad
- 15% return with 8% risk is better risk-adjusted
- Quant firms prioritize Sharpe ratio over raw return

---

#### Day 5-7: Markowitz Portfolio Optimization
**What to Learn:**
- Efficient frontier: Best return for each risk level
- Optimal portfolio: Highest Sharpe ratio
- Correlation effects: Diversification reduces risk

**Practice Exercise 9:**
```python
from scipy.optimize import minimize

# 3 assets
assets = ['TCS', 'INFY', 'HDFC']
expected_returns = np.array([0.12, 0.15, 0.10])
volatility = np.array([0.18, 0.20, 0.15])
correlation_matrix = np.array([
    [1.0, 0.3, 0.2],
    [0.3, 1.0, 0.25],
    [0.2, 0.25, 1.0]
])

# Function to minimize (negative Sharpe ratio)
def negative_sharpe(weights, returns, cov_matrix, risk_free_rate=0.05):
    portfolio_return = np.dot(weights, returns)
    portfolio_volatility = np.sqrt(np.dot(weights, np.dot(cov_matrix, weights)))
    sharpe = (portfolio_return - risk_free_rate) / portfolio_volatility
    return -sharpe

# Constraints: weights sum to 1
constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
bounds = tuple((0, 1) for _ in range(len(assets)))

# Initial guess: equal weight
initial_weights = np.array([1/3, 1/3, 1/3])

# Calculate covariance matrix
cov_matrix = np.outer(volatility, volatility) * correlation_matrix

# Optimize
result = minimize(negative_sharpe, initial_weights, 
                 args=(expected_returns, cov_matrix),
                 method='SLSQP', bounds=bounds, constraints=constraints)

optimal_weights = result.x
print(f"Optimal weights: TCS={optimal_weights[0]:.1%}, INFY={optimal_weights[1]:.1%}, HDFC={optimal_weights[2]:.1%}")
```

---

## SECTION 1.3: TIME SERIES ANALYSIS

### Week 3: Time Series Fundamentals

#### Day 1-2: Stationarity
**What to Learn:**
- Stationary: Mean and variance don't change over time (good for modeling)
- Non-stationary: Mean or variance change (trending, bad for modeling)
- Unit root test: Check if time series is stationary

**Why it matters:**
- Stock prices are non-stationary (trending)
- Returns are stationary (mean-reverting)
- Most trading models require stationarity

**Practice Exercise 10:**
```python
from statsmodels.tsa.stattools import adfuller
import pandas as pd

# Get stock price (non-stationary)
prices = np.array([100, 102, 105, 103, 108, 110, 109, 112, 115])
returns = np.diff(prices) / prices[:-1]  # Convert to returns

# ADF test for prices
adf_price = adfuller(prices)
print(f"Price ADF p-value: {adf_price[1]:.4f}")
if adf_price[1] > 0.05:
    print("✗ Prices are NON-stationary (trending)")

# ADF test for returns
adf_returns = adfuller(returns)
print(f"Returns ADF p-value: {adf_returns[1]:.4f}")
if adf_returns[1] < 0.05:
    print("✓ Returns are STATIONARY (mean-reverting)")
```

---

#### Day 3-4: Autocorrelation
**What to Learn:**
- Autocorrelation: How much today's value depends on yesterday's
- ACF (Auto-Correlation Function): Correlation at different lags
- PACF (Partial ACF): Direct correlation after removing intermediate effects

**Practice Exercise 11:**
```python
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

returns = np.random.normal(0.001, 0.02, 100)  # Daily returns

# Plot autocorrelation
fig, axes = plt.subplots(2, 1)
plot_acf(returns, lags=20, ax=axes[0])
plot_pacf(returns, lags=20, ax=axes[1])
plt.tight_layout()
plt.show()

# If returns have high autocorrelation:
# Yesterday's return influences today's → predictable
# If returns have low autocorrelation:
# Yesterday's return doesn't affect today → random walk (efficient market)
```

---

#### Day 5-7: Volatility Clustering
**What to Learn:**
- Volatility clustering: High volatility periods followed by high volatility
- GARCH models: Predict future volatility
- Implication: Risk varies over time, needs dynamic adjustment

**Practice Exercise 12:**
```python
# Simulate price with volatility clustering
np.random.seed(42)
returns = []
volatility = 0.01  # Starting volatility

for i in range(100):
    # GARCH: Next volatility depends on previous returns and volatility
    volatility = 0.00005 + 0.1 * (returns[-1]**2 if returns else 0) + 0.8 * volatility
    returns.append(np.random.normal(0, volatility))

# Plot
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(returns)
plt.title('Returns with Volatility Clustering')
plt.subplot(1, 2, 2)
plt.plot(np.abs(returns))
plt.title('Absolute Returns (Volatility)')
plt.tight_layout()
plt.show()

# Notice: High volatility periods cluster together
# This is used to predict risk periods
```

---

## SECTION 1.4: MARKET MICROSTRUCTURE

#### Day 1-2: Bid-Ask Spread & Slippage
**What to Learn:**
- Bid price: What buyers will pay
- Ask price: What sellers will sell at
- Spread: Ask - Bid = transaction cost
- Slippage: Actual fill price vs expected price

**Practice Exercise 13:**
```python
# Impact of bid-ask spread on 100 trades
bid_price = 100.00
ask_price = 100.05
spread = ask_price - bid_price  # ₹0.05

# Buy 100 shares
buy_cost = 100 * ask_price  # Pay ask price
# Sell 100 shares
sell_revenue = 100 * bid_price  # Get bid price

round_trip_cost = buy_cost - sell_revenue
round_trip_pct = round_trip_cost / buy_cost

print(f"Round trip cost: ₹{round_trip_cost:.2f}")
print(f"Round trip cost %: {round_trip_pct:.3%}")
print(f"On 100 trades with 2% target: Cost eats up {round_trip_pct * 100 / 2:.0f}% of profit")
```

---

#### Day 3-4: Liquidity
**What to Learn:**
- Liquidity: How easily you can buy/sell without moving price
- Highly liquid: Small spread, lot of volume
- Illiquid: Large spread, little volume

**Practice Exercise 14:**
```python
# Compare liquid vs illiquid stocks
stocks = {
    'TCS': {'daily_volume': 5000000, 'bid': 3599.95, 'ask': 3600.00},
    'NICHE': {'daily_volume': 50000, 'bid': 200.00, 'ask': 202.00},
}

for stock, data in stocks.items():
    spread_pct = (data['ask'] - data['bid']) / data['bid'] * 100
    print(f"{stock}: Spread = {spread_pct:.3f}%, Volume = {data['daily_volume']:,}")
    
# TCS: Liquid, tight spread (good for trading)
# NICHE: Illiquid, wide spread (bad for trading, cost eats profits)
```

---

## SECTION 1.5: MARKET STRUCTURE CONCEPTS

#### Day 5-7: Why Structure Matters Statistically
**What to Learn:**
- Break of Structure is NOT random (has higher probability of trending)
- Liquidity zones have statistical edge (price clusters there)
- Your edge is probabilistic, not deterministic

**Practice Exercise 15:**
```python
# Simulate BOS edge
np.random.seed(42)
num_bos = 100

# Random trade (50% win rate)
random_trades = np.random.choice([1, -1], size=num_bos)
random_accuracy = (random_trades == 1).sum() / num_bos

# BOS-based trade (your edge: 55% win rate)
bos_trades = np.random.choice([1, -1], size=num_bos, p=[0.55, 0.45])
bos_accuracy = (bos_trades == 1).sum() / num_bos

print(f"Random trading win rate: {random_accuracy:.1%}")
print(f"BOS trading win rate: {bos_accuracy:.1%}")

# Calculate statistical significance
from scipy.stats import binom_test
p_value = binom_test(bos_trades.sum() + num_bos, num_bos * 2, 0.5, alternative='greater')
print(f"P-value: {p_value:.4f}")
print(f"Edge is significant: {p_value < 0.05}")
```

---

## LEARNING CHECKLIST

### Week 1 Checklist
- [ ] Understand normal distribution, std dev, z-scores
- [ ] Know what p-value means
- [ ] Calculate correlation between two stocks
- [ ] Identify Type I & II errors in your trading
- [ ] Complete Exercise 1-5

### Week 2 Checklist
- [ ] Calculate expected portfolio return
- [ ] Calculate Sharpe ratio for your strategy
- [ ] Understand Markowitz optimization concept
- [ ] Explain confidence intervals to someone
- [ ] Complete Exercise 6-9

### Week 3 Checklist
- [ ] Test time series for stationarity (ADF test)
- [ ] Plot autocorrelation of returns
- [ ] Understand volatility clustering
- [ ] Calculate bid-ask spread impact
- [ ] Prove BOS has statistical edge
- [ ] Complete Exercise 10-15

---

## RESOURCES

### Free Online Courses
1. **Khan Academy** - Statistics & Probability (https://www.khanacademy.org/)
2. **Coursera** - "Business Statistics and Analysis" (Andrew Ng)
3. **StatQuest with Josh Starmer** (YouTube) - Best explanations

### Books (Read these)
1. "The Signal and the Noise" by Nate Silver (Understanding probability)
2. "Fooled by Randomness" by Nassim Taleb (Why trading is hard)
3. "A Random Walk Down Wall Street" by Burton Malkiel (Market efficiency)

### Python Libraries
- numpy: Numerical computations
- scipy.stats: Statistical tests
- pandas: Data manipulation
- matplotlib: Visualization
- statsmodels: Time series analysis

---

## DAILY SCHEDULE (3 hours)

**Option A: Learning Focus**
- 1 hour: Watch tutorial/read concept
- 1 hour: Do practice exercise
- 1 hour: Apply to your trading data

**Option B: Coding Focus**
- 30 min: Review concept
- 2 hours: Code practice exercises
- 30 min: Debug and understand

**Mix and match based on your learning style**

---

## KEY TAKEAWAYS

1. **Trading is probabilistic, not certain**
   - You can't predict individual trades
   - You CAN predict outcomes over many trades

2. **Statistics prove your edge**
   - p-value < 0.05 = edge likely real
   - Sample size matters (need 100+ trades)

3. **Risk matters more than return**
   - Sharpe ratio > raw return
   - Volatility will humble you

4. **Market structure has edge**
   - BOS isn't random (statistical proof)
   - Liquidity zones cluster (exploitable)
   - Your manual intuition works → now prove it mathematically

---

## END OF PHASE 1

After completing this, you'll be able to:
✓ Validate strategies statistically
✓ Design optimal portfolios
✓ Understand risk properly
✓ Explain your edge to quant firms
✓ Know when you DON'T have an edge

**Ready for Phase 2?** You'll apply all this theory to market structure detection.

---
