# PROBABILITY & STATISTICS PRACTICE WORKBOOK
## Phase 1 - Day 1: Hand Calculation Exercises

**Date Started:** February 17, 2026  
**Target:** Master probability calculations through practice  
**Time Estimate:** 2-3 hours  

---

## SECTION 1: BASIC PROBABILITY RULES
### Practice Level: BEGINNER ⭐

---

### **Problem 1.1: Addition Rule (Basic)**

**Question:** 
Your trading system generates signals from 2 independent indicators:
- RSI Signal accuracy: 55%
- MACD Signal accuracy: 65%
- Both signals correct together: 40%

What's the probability that AT LEAST ONE signal is correct?

**Formula to use:** P(A or B) = P(A) + P(B) - P(A and B)

**Your Calculation:**
```
P(A) = 
P(B) = 
P(A and B) = 

P(A or B) = _____ + _____ - _____ = _____
```

**Space for work:**
```



```

---

### **Problem 1.2: Complement Rule**

**Question:**
If the probability of your trade hitting stop loss is 0.35, what's the probability it doesn't hit stop loss?

**Formula to use:** P(not A) = 1 - P(A)

**Your Calculation:**
```
P(Stop loss) = 0.35
P(Not stop loss) = 1 - _____ = _____
```

---

### **Problem 1.3: Multiplication Rule (Sequential Events)**

**Question:**
Two independent trades. First trade wins with 60% probability, second trade wins with 60% probability.
- What's probability BOTH trades win?
- What's probability first wins AND second loses?

**Formula to use:** P(A and B) = P(A) × P(B)

**Your Calculation:**

Part A:
```
P(Trade 1 wins AND Trade 2 wins) = _____ × _____ = _____
```

Part B:
```
P(Trade 1 wins AND Trade 2 loses) = _____ × _____ = _____
```

---

### **Problem 1.4: Three Sequential Events**

**Question:**
What's probability of 3 consecutive winning trades if each has 60% win probability?

**Formula:** P(A and B and C) = P(A) × P(B) × P(C)

**Your Calculation:**
```
P(Win1 AND Win2 AND Win3) = _____ × _____ × _____ = _____
```

---

### **Problem 1.5: Win Rate Flip**

**Question:**
A strategy has a 48% losing rate. What's the win rate?

**Formula:** P(Win) = 1 - P(Loss)

**Your Calculation:**
```
P(Loss) = 0.48
P(Win) = 1 - _____ = _____
```

---

## SECTION 2: Z-SCORES & NORMAL DISTRIBUTION
### Practice Level: INTERMEDIATE ⭐⭐

---

### **Problem 2.1: Z-Score Calculation (Positive)**

**Question:**
Stock daily return = 2.5%  
Mean daily return (μ) = 0.1%  
Daily volatility (σ) = 1.2%

Calculate the Z-score.

**Formula:** $Z = \frac{X - \mu}{\sigma}$

**Your Calculation:**
```
X = 2.5%
μ = 0.1%
σ = 1.2%

Z = (_____ - _____) / _____ = _____ / _____ = _____
```

**Interpretation:** This Z-score of _____ tells us the move is _____ standard deviations above mean.

---

### **Problem 2.2: Z-Score Calculation (Negative)**

**Question:**
Stock daily return = -3.6%  
Mean = 0.05%  
Std Dev = 1.8%

Calculate Z-score and interpret.

**Your Calculation:**
```
Z = (_____ - _____) / _____ = _____ / _____ = _____
```

**Interpretation:** This is _____ standard deviations _____ the mean.

---

### **Problem 2.3: Finding X from Z-Score**

**Question:**
A Z-score of 2 tells us data is 2 standard deviations above mean.
Given: μ = 100, σ = 15

What's the actual value (X)?

**Formula (Rearranged):** $X = Z \times \sigma + \mu$

**Your Calculation:**
```
Z = 2
σ = 15
μ = 100

X = _____ × _____ + _____ = _____
```

---

### **Problem 2.4: Risk Threshold Planning**

**Question:**
You want to set a stop-loss at ±2 standard deviations from the mean.
Current stock price = 100
Expected daily move (μ) = +0.2%
Daily volatility (σ) = 2.5%

Calculate upper and lower stop-loss levels.

**Formula:** 
- Upper Stop = 100 + (2 × σ)
- Lower Stop = 100 - (2 × σ)

**Your Calculation:**

Upper limit:
```
X_upper = _____ + (2 × _____) = _____ + _____ = _____
```

Lower limit:
```
X_lower = _____ - (2 × _____) = _____ - _____ = _____
```

**Interpretation:** Price can move between _____ and _____ before hitting 2σ stops.

---

### **Problem 2.5: Portfolio Return Range**

**Question:**
Portfolio expected return = 8% annually (μ)
Portfolio volatility = 12% annually (σ)

Using 68-95-99.7 rule, what return range covers:
- 68% probability?
- 95% probability?
- 99.7% probability?

**Your Calculation:**

68% (±1σ):
```
Lower = 8% - 1(12%) = _____ - _____ = _____
Upper = 8% + 1(12%) = _____ + _____ = _____
Range: _____ to _____
```

95% (±2σ):
```
Lower = 8% - 2(12%) = _____ - _____ = _____
Upper = 8% + 2(12%) = _____ + _____ = _____
Range: _____ to _____
```

99.7% (±3σ):
```
Lower = 8% - 3(12%) = _____ - _____ = _____
Upper = 8% + 3(12%) = _____ + _____ = _____
Range: _____ to _____
```

---

## SECTION 3: PROBABILITY FROM Z-SCORES
### Practice Level: INTERMEDIATE ⭐⭐

---

### **Problem 3.1: Reading Z-Table (Positive Z)**

**Question:**
You calculated Z = 1.5 for a stock move.

Using the Z-table provided:
| Z | P(Z < z) |
|---|----------|
| 1.5 | 0.9332 |

What's the probability of a move ≥ 1.5σ?

**Calculation:**
```
P(Z < 1.5) = 0.9332 (from table)
P(Z ≥ 1.5) = 1 - P(Z < 1.5) = 1 - _____ = _____

Percentage = _____ × 100% = _____% 

Interpretation: Only about _____% chance of this extreme move
```

---

### **Problem 3.2: Reading Z-Table (Negative Z)**

**Question:**
You calculated Z = -2.33 for a crash scenario.

Using Z-table:
| Z | P(Z < z) |
|---|----------|
| -2.33 | 0.0099 |

What's the probability of a move ≤ -2.33σ?

**Calculation:**
```
P(Z < -2.33) = _____ (from table)

This is already the tail probability!

Percentage = _____ × 100% = _____% 

Interpretation: About _____% chance of this crash
```

---

### **Problem 3.3: Two-Tailed Probability**

**Question:**
Stock moved 2.5 standard deviations in either direction (up or down).

Z-table shows P(Z < 2.5) = 0.9938

What's probability of moving ±2.5σ in EITHER direction?

**Calculation:**
```
One tail = 1 - 0.9938 = _____
Two tails = 2 × _____ = _____
Percentage = _____ × 100% = _____% 

Interpretation: About _____% chance of ±2.5σ move in any direction
```

---

### **Problem 3.4: Comparing Probabilities**

**Question:**
You have two unusual stock moves:
- Stock A: Z = 2.0, P(Z < 2.0) = 0.9772
- Stock B: Z = 3.0, P(Z < 3.0) = 0.9987

Which is more unusual? Calculate tail probabilities.

**Your Calculation:**

Stock A:
```
P(move ≥ 2.0σ) = 1 - _____ = _____ = _____% 
```

Stock B:
```
P(move ≥ 3.0σ) = 1 - _____ = _____ = _____% 
```

Which is more rare? _____ (Stock A / Stock B)

---

### **Problem 3.5: Extreme Event Detection**

**Question:**
Your portfolio had a loss of -8% in one day.
Expected return = +0.1%
Daily volatility = 1.5%

Calculate Z and find probability of this event.

**Step 1: Calculate Z**
```
Z = (_____ - _____) / _____ = _____
```

**Step 2: Interpret rarity**
```
Is this > 3σ? _____ (Yes/No)
Expected frequency: ~1 per _____ years
(Use: 252 trading days/year × 3 = 756 days ≈ 3 years)
```

---

## SECTION 4: BINOMIAL DISTRIBUTION
### Practice Level: INTERMEDIATE ⭐⭐

---

### **Problem 4.1: Simple Binomial - Coin Flips**

**Question:**
Flip a fair coin 5 times. What's probability of getting exactly 3 heads?

**Given:**
- n = 5 (trials)
- k = 3 (successes we want)
- p = 0.5 (probability of heads)

**Formula:** $P(X = k) = \binom{n}{k} \times p^k \times (1-p)^{n-k}$

**Step 1: Calculate C(5,3)**
```
C(5,3) = 5! / (3! × 2!)

5! = 5 × 4 × 3 × 2 × 1 = _____
3! = 3 × 2 × 1 = _____
2! = 2 × 1 = _____

C(5,3) = _____ / (_____ × _____) = _____ / _____ = _____
```

**Step 2: Calculate p^k**
```
(0.5)^3 = 0.5 × 0.5 × 0.5 = _____
```

**Step 3: Calculate (1-p)^(n-k)**
```
(0.5)^2 = 0.5 × 0.5 = _____
```

**Step 4: Multiply all together**
```
P(X = 3) = _____ × _____ × _____ = _____

Percentage = _____% 
```

**Interpretation:** ____% chance of exactly 3 heads in 5 flips.

---

### **Problem 4.2: Trading Win/Loss Scenario**

**Question:**
Your strategy wins 60% of the time. Out of 5 trades, what's probability of exactly 3 wins?

**Given:**
- n = 5 trades
- k = 3 wins
- p = 0.6

**Your Calculation:**

Step 1: C(5,3)
```
C(5,3) = _____ (from Problem 4.1)
```

Step 2: (0.6)^3
```
(0.6)^3 = 0.6 × 0.6 × 0.6 = _____
```

Step 3: (0.4)^2
```
(0.4)^2 = 0.4 × 0.4 = _____
```

Step 4: Multiply
```
P(X = 3) = _____ × _____ × _____ = _____

Percentage = _____% 
```

---

### **Problem 4.3: All 5 Wins**

**Question:**
Same strategy (60% win rate). What's probability of 5 wins in 5 trades?

**Given:**
- n = 5
- k = 5  
- p = 0.6

**Your Calculation:**
```
C(5,5) = _____ (only 1 way to get 5/5)

(0.6)^5 = 0.6 × 0.6 × 0.6 × 0.6 × 0.6 = _____

(0.4)^0 = _____ (any number to power 0 = 1)

P(X = 5) = 1 × _____ × _____ = _____

Percentage = _____% 
```

**Interpretation:** Only ____% chance of 5 wins in a row!

---

### **Problem 4.4: At Least 3 Wins**

**Question:**
Out of 5 trades with 60% win rate, what's probability of getting AT LEAST 3 wins?

This means: P(X = 3) + P(X = 4) + P(X = 5)

**Your Calculation:**

From previous problems:
- P(X = 3) = _____ (from 4.2)
- P(X = 5) = _____ (from 4.3)

Calculate P(X = 4):
```
C(5,4) = 5! / (4! × 1!) = _____ / (_____ × _____) = _____

(0.6)^4 = _____
(0.4)^1 = 0.4

P(X = 4) = _____ × _____ × 0.4 = _____
```

Add them:
```
P(X ≥ 3) = _____ + _____ + _____ = _____

Percentage = _____% 
```

---

### **Problem 4.5: Probability Distribution Table**

**Question:**
Create a complete probability distribution table for 3 coin flips (p = 0.5)

| k (Heads) | C(3,k) | (0.5)^k | (0.5)^(3-k) | P(X=k) | % |
|-----------|--------|---------|------------|--------|-----|
| 0 | ? | ? | ? | ? | ? |
| 1 | ? | ? | ? | ? | ? |
| 2 | ? | ? | ? | ? | ? |
| 3 | ? | ? | ? | ? | ? |

**Your Calculation:**

k = 0:
```
C(3,0) = _____
(0.5)^0 = _____
(0.5)^3 = _____
P(X=0) = _____ × _____ × _____ = _____
```

k = 1:
```
C(3,1) = _____
(0.5)^1 = _____
(0.5)^2 = _____
P(X=1) = _____ × _____ × _____ = _____
```

k = 2:
```
C(3,2) = _____
P(X=2) = _____
```

k = 3:
```
C(3,3) = _____
P(X=3) = _____
```

**Verification:** Sum all probabilities = _____ (should equal 1.0)

---

## SECTION 5: ADVANCED COMBINATIONS
### Practice Level: ADVANCED ⭐⭐⭐

---

### **Problem 5.1: Complete Trading Scenario**

**Question:**
You manage a $100,000 portfolio with:
- Expected daily return: 0.15%
- Daily volatility: 1.8%
- Win rate: 62%
- Average winning trade: +$500
- Average losing trade: -$300

In one day:
1. What's your stop loss at 2σ?
2. What's probability of hitting that stop?
3. Out of 10 trades with 62% win rate, what's most likely outcome?

**Part 1: Stop Loss Calculation**
```
Stop Loss = Current Price - (2 × σ)
          = $100,000 - (2 × 1.8%)
          = $100,000 - _____
          = $_____
```

**Part 2: Probability of Trigger**
```
Z = (-_____ - 0.15%) / 1.8% = _____ (calculate the loss needed to hit stop)
From Z-table: P = _____
Percentage = _____% 
```

**Part 3: Binomial Distribution (n=10, p=0.62, most likely k=?)**
```
Expected wins = n × p = 10 × 0.62 = _____
This is most likely outcome: _____ wins

Calculate P(X = 6):
C(10,6) = _____
(0.62)^6 = _____
(0.38)^4 = _____
P(X=6) = _____ × _____ × _____ = _____
```

---

### **Problem 5.2: Risk vs Reward**

**Question:**
Compare two strategies:

**Strategy A:**
- Win rate: 70%
- Avg win: +2%
- Avg loss: -1%

**Strategy B:**
- Win rate: 55%
- Avg win: +3%
- Avg loss: -1%

Calculate expected value per trade for both. Which is better?

**Strategy A:**
```
EV_A = P(win) × Avg_win + P(lose) × Avg_loss
     = _____ × _____ + _____ × _____
     = _____ + _____
     = _____%
```

**Strategy B:**
```
EV_B = _____ × _____ + _____ × _____
     = _____ + _____
     = _____%
```

**Better strategy:** _____ (A or B)

---

### **Problem 5.3: Streaks and Probability**

**Question:**
If your strategy wins 65% of trades, what's:
- Probability of 3 wins in a row?
- Probability of 5 wins in a row?
- Probability of 10 wins in a row?

**Your Calculation:**

3 wins:
```
P(3 wins) = 0.65 × 0.65 × 0.65 = (0.65)^3 = _____
Percentage = _____% 
```

5 wins:
```
P(5 wins) = (0.65)^5 = _____
Percentage = _____% 
```

10 wins:
```
P(10 wins) = (0.65)^10 = _____
Percentage = _____% 
```

**Interpretation:** Getting 10 wins in a row is only ____% likely!

---

### **Problem 5.4: Real Data Application**

**Question:**
Use actual stock data (or simulated):
- Pick any stock/index
- Record last 20 daily returns
- Calculate mean and std dev
- Identify any Z > 2 or Z < -2 outliers

**Your Work:**

Daily Returns (last 20 days):
```
1. _____ %
2. _____ %
3. _____ %
... (continue)
20. _____ %
```

Calculate Mean:
```
Sum = _____
Mean (μ) = _____ / 20 = _____% 
```

Calculate Std Dev:
```
(Note: This is tedious by hand, use calculator or estimate)
Std Dev (σ) = _____% 
```

Find Outliers (|Z| > 2):
```
For each return X:
Z = (X - μ) / σ

Day ___ : Z = (_____ - _____) / _____ = _____ (|Z| > 2? Yes/No)
Day ___ : Z = _____  (|Z| > 2? Yes/No)

Total unusual days found: _____
```

---

## SECTION 6: CHALLENGE PROBLEMS
### Practice Level: HARD ⭐⭐⭐⭐

---

### **Problem 6.1: Portfolio Correlation Effect**

**Question:**
Two stocks with same return (μ = 10%) but different correlations:

**Portfolio of Stock A + Stock B:**
- Correlation = 0.2 (low)
- Combined portfolio volatility = 8%

**Portfolio of Stock A + Stock C:**
- Correlation = 0.9 (high)
- Combined portfolio volatility = 12%

Using Z-score approach:
- At 95% confidence level (Z = 1.645), what's maximum loss in each portfolio?
- Assume portfolio value = $50,000

**Your Calculation:**

Portfolio AB:
```
Max Loss = Portfolio Value × 1.645 × σ
         = $50,000 × 1.645 × 8%
         = $50,000 × _____
         = $_____
```

Portfolio AC:
```
Max Loss = $50,000 × 1.645 × 12%
         = $50,000 × _____
         = $_____
```

**Interpretation:** Low correlation portfolio is _____ safer than high correlation portfolio.

---

### **Problem 6.2: Multiple Signal Combination**

**Question:**
You have 3 independent trading signals:
- Signal A: 60% accuracy
- Signal B: 65% accuracy
- Signal C: 55% accuracy

What's probability that:
1. At least 1 is correct?
2. Exactly 2 are correct?
3. All 3 are correct?

**Part 1: At least 1 correct**
```
Easier to calculate using complement:
P(at least 1) = 1 - P(none correct)

P(all wrong) = (1-0.6) × (1-0.65) × (1-0.55)
             = _____ × _____ × _____
             = _____

P(at least 1 correct) = 1 - _____ = _____
Percentage = _____% 
```

**Part 2: Exactly 2 correct** (Most complex!)
```
This means: (A correct AND B correct AND C wrong) OR 
            (A correct AND B wrong AND C correct) OR
            (A wrong AND B correct AND C correct)

= (0.6 × 0.65 × 0.45) + (0.6 × 0.35 × 0.55) + (0.4 × 0.65 × 0.55)
= _____ + _____ + _____
= _____
```

**Part 3: All 3 correct**
```
P(all 3) = 0.6 × 0.65 × 0.55
         = _____
```

---

### **Problem 6.3: Break-Even Analysis**

**Question:**
Your trading system stats:
- Win rate: 55%
- Average win: $100
- Average loss: $90
- Transaction cost per trade: $5

What's your expected return per trade?

**Your Calculation:**
```
EV = (Win% × Avg_Win) + (Loss% × Avg_Loss) - Transaction_Cost

EV = (0.55 × $100) + (_____ × $_____) - $_____
   = _____ + _____ - _____
   = $_____

Is this profitable? _____ (Yes/No)
```

---

### **Problem 6.4: Risk of Ruin**

**Question:**
You have $10,000 account.
Risk per trade: 1% = $100
You need 10 consecutive losses to blow up account.

Assuming 60% win rate:
- What's probability of 10 consecutive losses?
- How long until you're likely to experience this?

**Your Calculation:**

P(loss) = 1 - 0.6 = 0.4

```
P(10 losses in a row) = (0.4)^10
                      = _____
                      = _____% 

Expected occurrences per 1000 trades:
= 1000 × _____ = _____ times

This means roughly 1 blow-up per _____ trades
```

---

### **Problem 6.5: Sharpe Ratio Calculation**

**Question:**
Strategy A:
- Annual return: 18%
- Annual volatility: 12%

Risk-free rate: 4%

Calculate Sharpe Ratio and interpret.

**Formula:** $Sharpe = \frac{Return - Risk\_Free\_Rate}{Volatility}$

**Your Calculation:**
```
Sharpe = (18% - 4%) / 12%
       = _____ / _____
       = _____

Interpretation: For every unit of risk, you get _____ units of return
Is this good? _____ (use benchmark: Sharpe > 1.0 is good)
```

---

## ANSWER KEY
### Check Your Work Below

---

### SECTION 1 ANSWERS

**1.1:** P(A or B) = 0.55 + 0.65 - 0.40 = **0.80 or 80%**

**1.2:** P(Not Stop) = 1 - 0.35 = **0.65 or 65%**

**1.3A:** 0.6 × 0.6 = **0.36 or 36%**  
**1.3B:** 0.6 × 0.4 = **0.24 or 24%**

**1.4:** 0.6 × 0.6 × 0.6 = **0.216 or 21.6%**

**1.5:** 1 - 0.48 = **0.52 or 52%**

---

### SECTION 2 ANSWERS

**2.1:** Z = (2.5 - 0.1) / 1.2 = 2.4 / 1.2 = **2.0**

**2.2:** Z = (-3.6 - 0.05) / 1.8 = -3.65 / 1.8 = **-2.03**

**2.3:** X = 2 × 15 + 100 = 30 + 100 = **130**

**2.4:** Upper = 100 + 5 = 105; Lower = 100 - 5 = 95

**2.5:** 
- 68%: -4% to 20%
- 95%: -16% to 32%
- 99.7%: -28% to 44%

---

### SECTION 3 ANSWERS

**3.1:** P(Z ≥ 1.5) = 1 - 0.9332 = 0.0668 = **6.68%**

**3.2:** P(Z < -2.33) = **0.99% or ~1%**

**3.3:** Two tails = 2 × (1 - 0.9938) = 2 × 0.0062 = **0.0124 or 1.24%**

**3.4:** Stock A: 2.28%; Stock B: 0.13%; **Stock B is more rare**

**3.5:** Z = (-8 - 0.1) / 1.5 = -5.4; Extremely rare, ~1 per 20+ years

---

### SECTION 4 ANSWERS

**4.1:** C(5,3) = 10; P = 10 × 0.125 × 0.25 = **0.3125 or 31.25%**

**4.2:** C(5,3) = 10; P = 10 × 0.216 × 0.16 = **0.3456 or 34.56%**

**4.3:** P(5 wins) = (0.6)^5 = **0.07776 or 7.78%**

**4.4:** P(≥3) = 0.3456 + 0.2592 + 0.0776 = **0.6824 or 68.24%**

**4.5:**
| k | P(X=k) | % |
|---|--------|-----|
| 0 | 0.125 | 12.5% |
| 1 | 0.375 | 37.5% |
| 2 | 0.375 | 37.5% |
| 3 | 0.125 | 12.5% |

---

### SECTION 5 ANSWERS

**5.1:**
1. Stop Loss = $100,000 - $3,600 = $96,400
2. Probability depends on specific loss ≈ 2-3%
3. Expected wins ≈ 6; P(6) ≈ 25-30%

**5.2:**
- EV_A = 0.70 × 2% + 0.30 × (-1%) = 1.40% - 0.30% = **1.1%**
- EV_B = 0.55 × 3% + 0.45 × (-1%) = 1.65% - 0.45% = **1.2%**
- **Strategy B is better**

**5.3:**
- 3 wins: 27.5%
- 5 wins: 11.6%
- 10 wins: 1.35%

**5.4:** (Will vary based on your data)

---

### SECTION 6 ANSWERS

**6.1:** Max loss AB = $6,584; Max loss AC = $9,876

**6.2:** 
- At least 1: 94.3%
- Exactly 2: 30.7%
- All 3: 21.5%

**6.3:** EV = $55 - $4.50 - $5 = **$45.50 per trade (Profitable!)**

**6.4:** P(10 losses) = (0.4)^10 = 0.00001 ≈ **0.001%** (Very rare!)

**6.5:** Sharpe = 14% / 12% = **1.17** (Good!)

---

## NEXT STEPS

Once you complete this workbook:

1. ✓ Check answers against key
2. ✓ Identify weak areas
3. ✓ Rework problem types you struggled with
4. ✓ Try with real trading data
5. ✓ Move to Day 2 content

**Time Estimate:** 3-4 hours hands-on practice

