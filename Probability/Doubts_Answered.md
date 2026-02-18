# PHASE 1 - DAY 1: DOUBTS & ANSWERS
## Comprehensive Q&A on Probability & Distributions

---

## Q1: Situations to Use Basic Probability Rules

### **Addition Rule: P(A or B) = P(A) + P(B) - P(A and B)**

**When to use:** When you want probability of at least ONE event happening

#### Situation 1: Trading Signal Reliability
```
Your trading system has:
- P(RSI divergence signals correct trend) = 0.6
- P(Moving average crossover signals correct trend) = 0.7
- P(Both signals correct together) = 0.5

What's probability at least ONE signal is correct?
P(A or B) = 0.6 + 0.7 - 0.5 = 0.8 = 80%
```

**Approach:**
1. Identify events A and B
2. Find P(A), P(B), and P(A and B)
3. Apply formula

#### Situation 2: Stock Price Movement
```
Stock might go up because:
- P(Earnings beat) = 0.4
- P(Sector performs well) = 0.5
- P(Both happen) = 0.25

P(Stock goes up from either reason) = 0.4 + 0.5 - 0.25 = 0.65
```

---

### **Multiplication Rule: P(A and B) = P(A) × P(B|A)**

**When to use:** When you need probability of TWO events happening together

#### Situation 1: Risk Management - Drawdown Risk
```
You want duration to hold a losing trade:
- P(Trade goes negative on day 1) = 0.3
- P(Trade still negative on day 2 | it's negative on day 1) = 0.5

P(Trade loses 2 consecutive days) = 0.3 × 0.5 = 0.15 = 15%
```

**Approach:**
1. Find probability of first event P(A)
2. Find conditional probability P(B|A) - probability of B given A happened
3. Multiply them

#### Situation 2: Portfolio Risk
```
You have 2 independent trades:
- P(Trade 1 wins) = 0.6
- P(Trade 2 wins) = 0.6
- Assuming independent: P(Both win) = 0.6 × 0.6 = 0.36
```

---

### **Complement Rule: P(not A) = 1 - P(A)**

**When to use:** When it's easier to calculate probability something DOESN'T happen

#### Situation 1: Win Rate Calculation
```
If P(Losing trade) = 0.35
Then P(Winning trade) = 1 - 0.35 = 0.65
```

**Approach:**
1. Calculate probability of opposite event
2. Subtract from 1

#### Situation 2: Risk of Ruin
```
If P(Strategy survives 1 day) = 0.95
Then P(Strategy fails on that day) = 1 - 0.95 = 0.05
```

---

## Q2: What Each Curve Describes

### Different Curve Interpretations

#### **Uniform Distribution (Flat line)**
```
Probability
    |     ___
    |    |   |
    |___|___|___
```

**What it tells us:**
- All values are equally likely
- No value is more probable than another
- Data is completely random with no pattern

**Example:** Rolling a fair die - 1/6 chance for each number (1,2,3,4,5,6)

---

#### **Binomial Distribution (Steps/Mountains)**
```
Probability
    |    __
    |   |  |__
    |___|    |__
    0  1  2  3  4
```

**What it tells us:**
- We have fixed number of trials
- Each trial has only 2 outcomes (success/failure, yes/no)
- Most results cluster around the middle
- Results are discrete (1, 2, 3... not 2.5)

**Example:** In 10 coin flips, getting heads - most likely ~5 heads, unlikely to get 0 or 10

**What the height tells us:**
- Height = How probable that outcome is
- Higher peak = More likely outcome
- Wider spread = More uncertainty

---

#### **Normal Distribution (Bell Curve)**
```
Probability Density
      |      ___
      |    /     \
      |  /         \
      |/             \
      |________________
```

**What it tells us:**
- Most values cluster around the mean (center)
- Gradually fewer values toward the extremes
- Symmetric on both sides
- Continuous (can be any decimal value)

**What the shape means:**
- **Narrow/Tall Bell:** Data very consistent (low spread = low risk)
- **Wide/Flat Bell:** Data very varied (high spread = high risk)
- **Shifted left:** Average outcome is negative (bearish)
- **Shifted right:** Average outcome is positive (bullish)

**Trading Example:**
```
If stock returns follow normal distribution:
- Narrow bell = Stable stock, predictable returns, lower volatility
- Wide bell = Wild stock, unpredictable, higher volatility, more risk
```

---

## Q3: Coin Flips vs Dice - Why Different Classifications?

### **The Key Difference**

#### **Coin Flip (Binomial Distribution)**
```
Only 2 outcomes: Heads OR Tails
P(Heads) = 0.5
P(Tails) = 0.5
```

**Why Binomial?**
- Exactly 2 mutually exclusive outcomes
- Perfect definition of binomial distribution

**Example with multiple flips:**
```
10 coin flips → 0 to 10 heads
Results: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
Pattern: Discrete steps (not continuous)
```

---

#### **Dice Roll (Uniform Distribution NOT Binomial)**
```
6 possible outcomes: 1, 2, 3, 4, 5, 6
P(each) = 1/6
```

**Why Uniform, not Binomial?**
- NOT a success/failure outcome
- 6 equally likely outcomes (not 2)
- Each outcome is distinct value
- Binomial requires only 2 outcomes

**Key Point:**
- **Binomial = 2 outcomes** (success/fail, yes/no, up/down)
- **Uniform = Multiple equally likely outcomes**
- **Dice = Uniform, not Binomial**

---

### **Trading Context**

#### **Binomial Example:**
```
Does trade hit stop loss? 
- YES (binomial outcome 1)
- NO (binomial outcome 2)
→ Use Binomial Distribution
```

#### **Uniform Example:**
```
Which NSE stock will outperform today?
- INFY, TCS, HDFC, WIPRO, LT... (many outcomes)
→ Use Uniform Distribution (if no preference)
```

---

## Q4: More Examples of Each Distribution

### **Uniform Distribution Examples**

1. **Lottery Numbers:** Each number 1-50 has equal 2% chance
2. **Random Password Generation:** Each character equally likely
3. **Fair Roulette Wheel:** Each number 1-37 has 1/37 probability
4. **Trading:** Random entry on any day of week (no pattern)

---

### **Binomial Distribution Examples**

1. **Trading Win/Loss:**
   - Success = Trade wins (+2%)
   - Failure = Trade loses (-1%)
   - Question: How many wins in 20 trades?
   
2. **Quality Control:**
   - Defective part = success/failure
   - Testing 100 items, how many defective?

3. **Election:**
   - Vote for Candidate A = yes/no
   - Poll 1000 people, how many vote for A?

4. **Stock Direction:**
   - Stock up = success
   - Stock down = failure
   - In 252 trading days, how many up days?

---

### **Normal Distribution Examples**

1. **Stock Returns:**
   - Daily stock returns approximately normal
   - Most days: 0% to 2% return
   - Rare: 5%+ or -5% extreme moves

2. **Height of Population:**
   - Average height = 170cm
   - Most people 160-180cm
   - Few < 150cm or > 190cm

3. **Test Scores:**
   - Average score = 70
   - Most students 60-80
   - Few scoring 40 or 95+

4. **Trading Slippage:**
   - Average slippage = 0.02%
   - Most trades: 0% to 0.05%
   - Rare: > 0.1% slippage

---

## Q5: Layman Explanation of Mean & Standard Deviation

### **Mean (μ) - The Average**

**Simple analogy:**
```
Imagine you have 5 traders in your group:
Profits: $100, $150, $200, $250, $300

Mean (Average) = (100+150+200+250+300) / 5 = $200

What it means: On average, each trader made $200
```

**For stock trading:**
```
If daily return's mean = 0.1%

What it tells us: On average, you make 0.1% per day
After 252 trading days: 0.1% × 252 ≈ 25% annual return (if compounded)
```

---

### **Standard Deviation (σ) - The Variability/Risk**

**Simple analogy:**
```
Two traders with same average profit = $1000/month

Trader A: Makes $900, $950, $1000, $1050, $1100 (consistent)
Trader B: Makes $100, $500, $1000, $1500, $2900 (wild swings)

Both have mean = $1000
But Trader A has LOW std dev (low variability)
Trader B has HIGH std dev (high variability/risk)

Which would you trust? Trader A! (More predictable)
```

**For stock volatility:**
```
Stock A: Mean return = 0.1%, Std Dev = 1%
→ Stable stock, predictable, safer

Stock B: Mean return = 0.1%, Std Dev = 5%
→ Volatile stock, unpredictable, riskier

Same average return, but very different risk!
```

---

### **The Perfect Layman Explanation**

**Tell your grandmother:**
```
Mean = On average, what happens
Std Dev = How much things vary from average

Example: Room temperature
Mean = 25°C (on average, it's 25°C)
Std Dev = 3°C (temps range between 22°C to 28°C usually)

If Std Dev = 10°C
Then temps swing between 15°C to 35°C (much more variation!)
```

**For investing:**
```
Return Mean = 10% (on average you make 10%)
Return Std Dev = 2% (mostly between 8% to 12%)

VS

Return Mean = 10% (on average you make 10%)
Return Std Dev = 20% (might be -10% to +30%!)

Same average return, but second one is scarier!
```

---

## Q6: Calculating the 0.3% Beyond ±6%

### **The Breakdown**

Given:
```
Mean (μ) = 0.1%
Standard Deviation (σ) = 2%
Range beyond ±6%
```

**Step 1: Convert to Z-scores**
```
Upper limit: 6% 
Z = (6% - 0.1%) / 2% = 5.9% / 2% = 2.95 ≈ 3

Lower limit: -6%
Z = (-6% - 0.1%) / 2% = -6.1% / 2% = -3.05 ≈ -3
```

**Step 2: Use the 68-95-99.7 Rule**
```
68% within ±1σ (-1.9% to 2.1%)
95% within ±2σ (-3.9% to 4.1%)
99.7% within ±3σ (-5.9% to 6.1%)
```

**Step 3: Calculate tail probability**
```
If 99.7% falls within ±3σ
Then 0.3% falls outside ±3σ

Since our range is approximately ±3σ:
Probability of returns beyond ±6% ≈ 0.3%
```

**More precise calculation using Z-table:**
```
Z = 3.0 corresponds to P(Z < 3) = 0.99865
So P(Z > 3) = 1 - 0.99865 = 0.00135 = 0.135%
Both tails = 0.135% × 2 = 0.27% ≈ 0.3%
```

---

## Q7: Usual Z-Score Values

### **Common Z-Score Reference Table**

| Z-Score | Percentage | What it means |
|---------|-----------|--------------|
| 0 | 50% | At the mean |
| ±0.5 | 38.3% (within) | Common variation |
| ±1 | 68% (within) | Normal range |
| ±1.5 | 86.6% (within) | Slightly unusual |
| ±2 | 95% (within) | Unusual/Alert |
| ±2.5 | 98.8% (within) | Very unusual |
| ±3 | 99.7% (within) | Extreme/Rare |
| ±4 | 99.99% (within) | Extremely rare |

---

### **Practical Trading Ranges**

**Low Z-Scores (±0 to ±1):**
- Normal market behavior
- No action needed
- Stock moving as expected

**Medium Z-Scores (±1 to ±2):**
- Elevated but normal
- Monitor position
- Possible opportunity

**High Z-Scores (±2 to ±3):**
- Unusual move
- Possible breakout OR manipulation
- Consider taking profit/setting stops

**Extreme Z-Scores (> ±3):**
- Very rare event
- Market anomaly
- Could be error or major news

---

## Q8: Z-Score Values & Interpretation

### **Detailed Z-Score Interpretation Table**

| Z-Score Range | Probability | Trading Signal | Action |
|---|---|---|---|
| Z = 0 | 50% | Neutral | Hold position |
| 0 < Z < 1 | 34% | Slightly bullish | Monitor |
| Z = 1 | 84% | Moderately bullish | Consider entry |
| 1 < Z < 2 | 95% | Strong signal | Possible entry |
| Z = 2 | 97.5% | Very strong | Enter/Add position |
| 2 < Z < 3 | 99.7% | Extreme **BUY** | Consider booking partial |
| Z > 3 | 99.99% | Black swan event | ALERT - Verify if data error |
| Z = -1 | 16% | Moderately bearish | Monitor |
| Z = -2 | 2.5% | Strong bearish signal | Consider SHORT |
| Z < -3 | < 0.3% | Black swan **SELL** | Emergency stop-loss check |

---

### **Real Trading Scenarios with Z-Scores**

#### **Scenario 1: Stock Unusual Uptick**
```
Stock average daily return = 0.1% (μ)
Stock volatility = 1.5% (σ)

Today's return = 4.1%

Z-score = (4.1% - 0.1%) / 1.5% = 4.0 / 1.5% = 2.67

Interpretation:
- Z = 2.67 (between 2 and 3)
- This is > 2σ (unusual)
- Only ~0.4% chance of this happening
- Possible reasons:
  * Earnings beat
  * Sector momentum
  * Acquisition news
  * Market manipulation
```

#### **Scenario 2: Stock Crash**
```
Stock average daily return = 0.05%
Stock volatility = 2%

Today's return = -7%

Z-score = (-7% - 0.05%) / 2% = -7.05% / 2% = -3.53

Interpretation:
- Z < -3 (Extreme rare event)
- Only 0.02% chance of this happening
- Likely causes:
  * Regulatory action
  * Major loss announcement
  * Wrong data?
- Action: Verify if data is correct, else CHECK FOR NEWS
```

---

## BONUS: QUANT INTERVIEW QUESTIONS & SCENARIOS

### **Question 1: Portfolio Risk Calculation**

**Interview Q:** *"You have a portfolio with 3 stocks. Daily returns are normally distributed with means [0.1%, 0.05%, -0.02%] and volatilities [1.5%, 2%, 1%]. Correlations are [0.3, 0.5, 0.2]. Calculate 1-day VaR (Value at Risk) at 95% confidence."*

**Approach:**
1. Calculate portfolio mean return
2. Calculate portfolio volatility (use correlation matrix)
3. Find Z-score for 95% confidence = 1.645
4. VaR = Portfolio Mean - (Z × Portfolio Volatility)

---

### **Question 2: Probability of Win Streak**

**Interview Q:** *"Your trading strategy wins 60% of trades. What's the probability of getting 5 wins in a row? And 10 in a row?"*

**Solution:**
```
P(5 wins in a row) = 0.6^5 = 0.078 = 7.8% (rare but possible)
P(10 wins in a row) = 0.6^10 = 0.006 = 0.6% (very rare)

If you see 10 wins in a row, either:
- You're extremely lucky (0.6% chance)
- Strategy is better than 60% win rate
- You got lucky today (regression to mean coming)
```

---

### **Question 3: Options Pricing Scenario**

**Interview Q:** *"A stock is at 100 with σ=20% annually, r=5% risk-free rate. What's the probability the stock is above 110 after 1 day?"*

**Step-by-step:**
```
1-day volatility = 20% / √252 ≈ 1.26%
1-day expected return = 5% / 252 ≈ 0.02%

Z = (110 - 100 - 0.02%) / 1.26% = 9.98 / 1.26 ≈ 7.9

P(Z > 7.9) ≈ 0% (extremely unlikely)
Correct, 1-day moves are small usually!
```

---

### **Question 4: Drawdown Risk**

**Interview Q:** *"Your strategy has daily volatility of 1.5%. You have $100,000. What's maximum expected drawdown at 95% confidence in one day? In one week?"*

**Solution:**
```
One-day drawdown (95%):
Z = 1.645 for 95% confidence
Max loss = $100,000 × 1.645 × 1.5% = $2,467.50

One-week drawdown (95%):
Daily return correlation matters
Assume independent days:
Weekly σ = 1.5% × √5 = 3.35%
Max loss = $100,000 × 1.645 × 3.35% = $5,510.75
```

---

### **Question 5: Correlation Interpretation**

**Interview Q:** *"Two stocks have correlation 0.8. Does this mean one moves 80% as much as the other?"*

**Answer: NO!**
```
Correlation 0.8 means:
- Strong positive relationship
- When one goes up, other likely goes up
- You can't predict exact move, just direction

Example:
Stock A: +5%
Stock B might be: +3% or +7% (not exactly 4%)

Correlation is about direction, not magnitude!
```

---

### **Question 6: Option Greeks & Probability**

**Interview Q:** *"An option's delta is 0.6. What's the probability it expires in-the-money?"*

**Answer:**
```
Delta ≈ Probability of expiry ITM (under certain conditions)

Delta 0.6 ≈ 60% chance expires ITM
Delta 0.3 ≈ 30% chance expires ITM

BUT: This assumes risk-neutral probability, not real-world probability
Real-world probability depends on your edge/analysis
```

---

### **Question 7: Sharpe Ratio Comparison**

**Interview Q:** *"Strategy A: Return 15%, Volatility 10%. Strategy B: Return 12%, Volatility 5%. Risk-free rate 3%. Which is better?"*

**Solution:**
```
Sharpe A = (15% - 3%) / 10% = 1.2
Sharpe B = (12% - 3%) / 5% = 1.8

Strategy B is better!
Less risk, better risk-adjusted returns

This is why Sharpe ratio matters more than raw returns
```

---

### **Question 8: Backtesting Fallacy**

**Interview Q:** *"I backtested 100 strategies on historical data. 1 showed 50% annual return with 5% Sharpe. Should I trade it?"*

**Red Flags:**
```
Possible issues:
1. Overfitting: Strategy fit to historical noise
2. Look-ahead bias: Used future data accidentally
3. Survivorship bias: Only tested surviving stocks
4. Multiple comparison problem: 100 strategies, 1 is lucky
5. Data snooping: Tried many parameters

Safe approach: Out-of-sample testing must be 40%+ of data
```

---

## SUMMARY: WHEN TO USE WHAT

| Situation | Distribution | Rule |
|-----------|--------------|------|
| Win/Loss in trades | Binomial | P(A and B) |
| Multiple signal reliability | Uniform or Normal | Addition rule |
| Price movements | Normal | Z-score |
| Risk calculation | Normal | 68-95-99.7 |
| Portfolio return | Normal | All three rules |
| Sequential trades | Binomial | Multiplication |

---

## KEY TAKEAWAYS

✅ **Probability Rules** help you understand WHEN events happen together  
✅ **Distributions** show us WHAT usually happens  
✅ **Z-Scores** tell us HOW unusual an event is  
✅ **Mean + Std Dev** define normal behavior  
✅ **Normal Distribution** is everywhere in trading  
✅ **Risk Management** uses all these concepts  

---

## NEXT: Practice with Your Own Trading Data
```python
# Calculate mean, std dev, z-scores for your broker data
# Identify unusual days (|Z| > 2)
# Predict stop-loss levels using 2-3σ
```

