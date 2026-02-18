# PHASE 1 - DAY 1: Distributions & Probability
## Probability & Statistics Bootcamp

**Date:** February 15, 2026  
**Duration:** ~2-3 hours  
**Topics:** Distributions, Probability, Normal Distribution

---

## 1. PROBABILITY FOUNDATIONS

### What is Probability?
Probability measures the likelihood of an event occurring, ranging from 0 to 1:
- **P(Event) = 0:** Event will never happen
- **P(Event) = 0.5:** Event has 50% chance
- **P(Event) = 1:** Event will definitely happen

### Basic Rules
1. **Addition Rule:** P(A or B) = P(A) + P(B) - P(A and B)
2. **Multiplication Rule:** P(A and B) = P(A) × P(B|A)
3. **Complement Rule:** P(not A) = 1 - P(A)

### Trading Context
When you enter a trade, you're betting on:
- **P(Stock goes up) > P(Stock goes down)** with acceptable profit margins
- **Risk Management:** Define P(loss limit) before entering

---

## 2. DISTRIBUTIONS

### What is a Distribution?
A distribution describes how values are spread across a range. It shows:
- Which values are most likely
- Which values are rare
- The shape/pattern of the data

### Common Types

#### **Uniform Distribution**
All values equally likely
```
Probability
    |     ___
    |    |   |
    |____|___|____
    a         b
```
- **Example:** Rolling a fair die (1/6 chance for each number)
- **Trading:** If events are random, they follow uniform distribution

#### **Binomial Distribution**
Number of successes in N trials
```
Probability
    |    __
    |   |  |__
    |___|    |__
    0  1  2  3
```
- **Example:** Coin flips (heads/tails)
- **Trading:** Did your strategy get + or - signals today?

#### **Normal Distribution (Gaussian)**
Bell curve - most data clusters around the mean
```
Probability Density
      |      ___
      |    /     \
      |  /         \
      |/             \
      |________________
      -3σ  μ  +3σ   (mean)
```
- **Most Important for Trading!**
- Many real-world phenomena follow normal distribution
- Stock returns often approximately normal

---

## 3. NORMAL DISTRIBUTION (THE BELL CURVE)

### Key Characteristics
1. **Symmetric** around the mean (μ)
2. **Mean = Median = Mode** at the center
3. Defined by two parameters:
   - **Mean (μ):** Center of the distribution
   - **Standard Deviation (σ):** Spread/width

### The 68-95-99.7 Rule
```
68% of data within ±1σ
95% of data within ±2σ
99.7% of data within ±3σ
```

### Example: Stock Returns
If a stock has:
- Mean daily return = 0.1% (μ)
- Standard deviation = 2% (σ)

Then:
- 68% of days: return between -1.9% to +2.1%
- 95% of days: return between -3.9% to +4.1%
- Only 0.3% of days: return beyond ±6%

### Why This Matters for Trading
1. **Risk Assessment:** Know possible price ranges
2. **Stop Loss:** Set stops at 2-3σ to cover 95-99.7% of scenarios
3. **Volatility:** Higher σ = higher uncertainty
4. **Probability Calculation:** Calculate chance of specific returns

---

## 4. Z-SCORE (Standardization)

### What is a Z-Score?
Converts any value to standard units showing how many standard deviations from mean:

$$Z = \frac{X - \mu}{\sigma}$$

Where:
- X = individual value
- μ = mean
- σ = standard deviation

### Example
Stock: μ = 100, σ = 10
- Value 110 → Z = (110-100)/10 = **+1** (1 SD above mean)
- Value 85 → Z = (85-100)/10 = **-1.5** (1.5 SD below mean)

### Z-Score Interpretation
- Z = 0: Exactly at mean
- Z = +2: In top 2.3% of values
- Z = -2: In bottom 2.3% of values

### Trading Use
Identifies unusual price movements (outliers):
- Z > 2: Unusual high movement (opportunity? manipulation?)
- Z < -2: Unusual low movement
- Z > 3: Extreme rare event

---

## 5. CODE EXERCISE 1: Generate & Plot Normal Distribution

### Part 1: Basic Setup
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Set random seed for reproducibility
np.random.seed(42)

# Generate normal distribution data
mean = 0
std_dev = 1
num_samples = 10000

# Create random data from normal distribution
data = np.random.normal(mean, std_dev, num_samples)

print(f"Mean: {np.mean(data):.4f}")
print(f"Std Dev: {np.std(data):.4f}")
print(f"Min: {np.min(data):.4f}")
print(f"Max: {np.max(data):.4f}")
```

### Part 2: Create Visualizations
```python
# Create figure with multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Histogram
axes[0, 0].hist(data, bins=50, density=True, alpha=0.7, color='blue', edgecolor='black')
axes[0, 0].set_title('Histogram of Normal Distribution')
axes[0, 0].set_xlabel('Value')
axes[0, 0].set_ylabel('Frequency (Density)')

# Plot 2: Normal distribution curve overlay
x = np.linspace(-4, 4, 100)
y = stats.norm.pdf(x, mean, std_dev)
axes[0, 1].plot(x, y, 'r-', linewidth=2, label='Normal Distribution Curve')
axes[0, 1].hist(data, bins=50, density=True, alpha=0.5, color='blue', edgecolor='black')
axes[0, 1].set_title('Histogram with Normal Curve')
axes[0, 1].set_xlabel('Value')
axes[0, 1].set_ylabel('Probability Density')
axes[0, 1].legend()

# Plot 3: Q-Q Plot (compares data to normal distribution)
stats.probplot(data, dist="norm", plot=axes[1, 0])
axes[1, 0].set_title('Q-Q Plot (Normal Distribution Check)')

# Plot 4: Cumulative Distribution Function
sorted_data = np.sort(data)
y_cumsum = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
axes[1, 1].plot(sorted_data, y_cumsum, 'b-', linewidth=2, label='Empirical CDF')
theoretical_cdf = stats.norm.cdf(sorted_data, mean, std_dev)
axes[1, 1].plot(sorted_data, theoretical_cdf, 'r--', linewidth=2, label='Theoretical CDF')
axes[1, 1].set_title('Cumulative Distribution Function')
axes[1, 1].set_xlabel('Value')
axes[1, 1].set_ylabel('Cumulative Probability')
axes[1, 1].legend()

plt.tight_layout()
plt.show()
```

### Part 3: Stock Returns Application
```python
# Simulate stock daily returns (more realistic)
daily_returns = np.random.normal(0.001, 0.02, 252)  # 1 year of trading days
# mean = 0.1% daily return, std = 2%, 252 trading days

# Calculate probability of extreme moves
extreme_moves = np.sum(np.abs(daily_returns) > 0.05)  # moves > 5%
prob_extreme = extreme_moves / len(daily_returns)

print(f"\nStock Return Analysis:")
print(f"Average daily return: {np.mean(daily_returns)*100:.3f}%")
print(f"Daily volatility: {np.std(daily_returns)*100:.3f}%")
print(f"Probability of move > 5%: {prob_extreme*100:.2f}%")

# Z-scores for returns
z_scores = (daily_returns - np.mean(daily_returns)) / np.std(daily_returns)
extreme_z = np.sum(np.abs(z_scores) > 2)
print(f"Days with |Z| > 2: {extreme_z} out of {len(z_scores)}")

# Plot stock returns
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.hist(daily_returns * 100, bins=40, density=True, alpha=0.7, color='green', edgecolor='black')
plt.xlabel('Daily Return %')
plt.ylabel('Frequency')
plt.title('Distribution of Daily Stock Returns')
plt.grid(alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(np.cumsum(daily_returns) * 100, linewidth=2, color='blue')
plt.xlabel('Trading Day')
plt.ylabel('Cumulative Return %')
plt.title('Cumulative Returns Over Time')
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()
```

---

## 6. KEY INSIGHTS FOR TRADING

| Concept | Trading Application |
|---------|-------------------|
| **Mean** | Expected daily return of your strategy |
| **Std Dev** | Volatility - measure of risk |
| **Normal Distribution** | Assume returns follow this pattern |
| **Z-Score > 2** | Unusual profitable opportunity OR execution error |
| **68-95-99.7 Rule** | Set risk limits (stops) at 2-3σ |
| **Probability** | Calculate odds before entering trade |

---

## 7. QUICK REFERENCES

### Probability Formula
$$P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total number of possible outcomes}}$$

### Normal Distribution
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

### Standard Error
$$SE = \frac{\sigma}{\sqrt{n}}$$

---

## 8. PRACTICE QUESTIONS

1. **What % of data falls within ±2 standard deviations?** 
   - Answer: 95%

2. **If stock returns are normally distributed with μ=0.1%, σ=2%, what's the probability of a day with return > 4%?**
   - Z = (4% - 0.1%) / 2% = 1.95
   - P(Z > 1.95) ≈ 2.6%

3. **Why does the normal distribution matter for trading?**
   - Answer: Stock prices often follow approximately normal distributions, allowing risk calculation and stop-loss placement

---

## 9. NEXT STEPS

- [ ] Code Exercise 1: Run the Python code above
- [ ] Save output plots
- [ ] Note any unusual patterns in the plots
- [ ] Prepare for Day 2: Standard Deviation, Variance, Z-Scores (deep dive)

---

## 📚 RESOURCES

- **Khan Academy:** Normal Distribution (20 min) - Search "intro to normal distribution"
- **StatQuest YouTube:** "Normal Distribution Explained" - Josh Starmer
- **Book:** "Statistics" by David Freedman (beginner-friendly)

---

**Notes Section (Fill as you Learn):**
- Learned: 
- Questions:
- Code status: ✓ Running / ⚠ Issue / ✗ Not started
