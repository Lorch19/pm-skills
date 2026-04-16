---
name: cohort-analysis
description: "Perform cohort analysis on user engagement data — retention curves, feature adoption trends, and segment-level insights. Use when analyzing user retention by cohort, studying feature adoption over time, investigating churn patterns, or identifying engagement trends."
type: tool
best_for:
  - "Retention curve analysis by signup cohort"
  - "Feature adoption tracking across cohorts"
  - "Churn pattern identification"
---

# Cohort Analysis & Retention Explorer

## Purpose
Analyze user engagement and retention patterns by cohort to identify trends in user behavior, feature adoption, and long-term engagement. Combine quantitative insights with qualitative research recommendations.

## How It Works

### Step 1: Read and Validate Your Data
- Accept CSV, Excel, or JSON data files with user cohort information
- Verify data structure: cohort identifier, time periods, engagement metrics
- Check for missing values and data quality issues
- Summarize key statistics (cohort sizes, date ranges, metrics available)

### Step 2: Generate Quantitative Analysis
- Calculate cohort retention rates and engagement trends
- Identify retention curves, drop-off patterns, and anomalies
- Compute feature adoption rates across cohorts
- Calculate month-over-month or period-over-period changes
- Generate Python analysis scripts using pandas and numpy if requested

### Step 3: Create Visualizations
- Generate retention heatmaps (cohorts vs. time periods)
- Create line charts showing cohort progression
- Build comparison charts for feature adoption
- Visualize drop-off points and engagement trends
- Output as interactive charts or static images

### Step 4: Identify Insights & Patterns
- Spot one or more significant patterns:
  - Early churn in specific cohorts
  - Late-stage engagement changes
  - Feature adoption clusters
  - Seasonal or temporal trends
- Highlight surprising findings and deviations
- Compare cohort performance to establish baselines

### Step 5: Suggest Follow-Up Research
- Recommend qualitative research methods:
  - Targeted user interviews with churning users
  - Feature usage surveys with engaged cohorts
  - Session replays of key interaction patterns
  - Win/loss analysis for high vs. low retention cohorts
- Design follow-up quantitative studies
- Suggest A/B tests or feature experiments

## Usage Examples

**Example 1: Upload CSV Data**
```
Upload cohort_engagement.csv with columns: cohort_month, weeks_active,
user_id, feature_x_usage, engagement_score

Request: "Analyze retention patterns and identify why Q4 2025 cohorts
underperform compared to Q3"
```

**Example 2: Describe Data Format**
```
"I have monthly user cohorts from Jan-Dec 2025. Each row shows:
cohort date, user ID, purchase frequency, and support tickets.
Analyze which cohorts show best long-term retention."
```

**Example 3: Feature Adoption Analysis**
```
Upload feature_usage.xlsx with cohort adoption data.

Request: "Compare adoption curves for our new feature across cohorts.
Which cohorts adopted fastest? Any patterns?"
```

## Key Capabilities

- **Data Reading**: Import CSV, Excel, JSON, SQL query results
- **Retention Analysis**: Calculate and visualize retention rates over time
- **Cohort Comparison**: Compare metrics across cohort groups
- **Anomaly Detection**: Flag unusual patterns or drop-offs
- **Python Scripts**: Generate reusable analysis code for ongoing analysis
- **Visualizations**: Create heatmaps, charts, and interactive dashboards
- **Research Design**: Suggest targeted follow-up studies and interview approaches
- **Statistical Summary**: Provide quantitative metrics and correlation analysis

## Tips for Best Results

1. **Include time dimension**: Provide data across multiple time periods
2. **Define cohort clearly**: Make cohort grouping explicit (signup month, feature launch date, etc.)
3. **Provide context**: Explain product changes, launches, or events during the period
4. **Multiple metrics**: Include retention, engagement, feature usage, revenue, etc.
5. **Sufficient data**: At least 3-4 cohorts for meaningful pattern identification
6. **Request specific output**: Ask for visualizations, Python scripts, or research recommendations

## Output Format

You'll receive:
- **Data Summary**: Cohort overview and data quality assessment
- **Quantitative Findings**: Key metrics, retention rates, and trend analysis
- **Visualizations**: Charts showing retention curves, adoption patterns
- **Pattern Identification**: 2-3 significant insights from the data
- **Research Recommendations**: Specific qualitative and quantitative follow-ups
- **Analysis Scripts** (if requested): Python code for reproducible analysis
- **Next Steps**: Prioritized actions based on findings

---

## B2B SaaS Cohort Dimensions

In B2B, cohorts aren't just "signup month." Choose dimensions that reveal *why* retention differs:

| Dimension | How to define cohorts | What it reveals |
|-----------|---------------------|-----------------|
| **Signup date** | Month/quarter of first contract | Seasonal patterns, onboarding quality over time |
| **Company size** | Employee count bands (1-50, 51-200, 201-1000, 1000+) | Which segments retain best; where to focus GTM |
| **Industry vertical** | NAICS code or manual tag | Vertical-specific retention patterns and product-market fit signals |
| **Acquisition channel** | How they found you (inbound, outbound, partner, event) | Channel quality beyond cost-per-lead |
| **Onboarding path** | Self-serve vs. assisted vs. white-glove | ROI of onboarding investment |
| **First feature adopted** | Which core feature they used first | Activation patterns that predict retention |
| **Contract value** | ACV bands ($0-10K, $10-50K, $50K+) | Price sensitivity and value realization by segment |
| **Champion persona** | Role of the internal champion (admin, IC, exec) | Which buyer personas drive long-term engagement |
| **Time to value** | Days from signup to first meaningful outcome | Whether faster TTV predicts retention (it usually does) |

**Tip:** Start with signup date cohorts to establish a baseline, then layer in one business dimension at a time to isolate what drives retention differences.

---

## Output Format Templates

### Retention Heatmap Specification

```
Rows: Cohorts (one per row, ordered by signup date)
Columns: Periods since signup (Month 0, Month 1, ... Month 12)
Cells: Retention rate as percentage
Color scale: Green (>90%) → Yellow (60-90%) → Red (<60%)
Include: Cohort size (N) in the leftmost column
```

### Cohort Comparison Table

```markdown
| Cohort | N | M1 | M3 | M6 | M12 | LTV (est.) | Notes |
|--------|---|----|----|----|----|------------|-------|
| [Cohort A] | [N] | [%] | [%] | [%] | [%] | [$] | [Key observation] |
| [Cohort B] | [N] | [%] | [%] | [%] | [%] | [$] | [Key observation] |
```

### Python Analysis Skeleton

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def build_cohort_retention(df, user_col, date_col, cohort_col=None, period='M'):
    """
    Build a retention matrix from event-level data.
    
    Args:
        df: DataFrame with at least user_col and date_col
        user_col: Column identifying the user/account
        date_col: Column with event timestamps
        cohort_col: Optional pre-defined cohort column. If None, uses first event date.
        period: 'M' for monthly, 'W' for weekly, 'Q' for quarterly
    """
    df[date_col] = pd.to_datetime(df[date_col])
    
    # Assign cohort based on first activity
    if cohort_col is None:
        cohorts = df.groupby(user_col)[date_col].min().dt.to_period(period)
        cohorts.name = 'cohort'
        df = df.merge(cohorts, on=user_col)
    
    # Calculate period offset from cohort
    df['period'] = df[date_col].dt.to_period(period)
    df['period_offset'] = (df['period'] - df['cohort']).apply(lambda x: x.n)
    
    # Build retention matrix
    cohort_data = df.groupby(['cohort', 'period_offset'])[user_col].nunique().reset_index()
    cohort_sizes = cohort_data[cohort_data['period_offset'] == 0].set_index('cohort')[user_col]
    
    retention = cohort_data.pivot(index='cohort', columns='period_offset', values=user_col)
    retention = retention.divide(cohort_sizes, axis=0) * 100
    
    return retention, cohort_sizes

def plot_retention_heatmap(retention, title='Cohort Retention Heatmap'):
    """Plot a styled retention heatmap."""
    plt.figure(figsize=(14, 8))
    sns.heatmap(
        retention.round(1), annot=True, fmt='.1f', 
        cmap='RdYlGn', vmin=0, vmax=100,
        linewidths=0.5, cbar_kws={'label': 'Retention %'}
    )
    plt.title(title)
    plt.xlabel('Periods Since Signup')
    plt.ylabel('Cohort')
    plt.tight_layout()
    return plt

# Usage:
# retention, sizes = build_cohort_retention(df, 'account_id', 'event_date')
# plot_retention_heatmap(retention)
```

---

## Common Pitfalls

1. **Cohort size neglect** — A cohort of 5 accounts showing 100% retention is noise, not signal. Always display N alongside percentages. Minimum viable cohort size for B2B: ~20-30 accounts.
2. **Survivorship bias** — If you only analyze active accounts, you miss the ones that churned before generating enough data. Include accounts that churned in Period 0 or 1.
3. **Calendar vs. tenure confusion** — "March retention" (calendar) and "Month 3 retention" (tenure since signup) are different questions. Be explicit about which you're measuring.
4. **Ignoring expansion/contraction** — Logo retention (did they stay?) ≠ net revenue retention (did they grow?). Track both. A 95% logo retention with 80% NRR means accounts are shrinking.
5. **Single-metric fixation** — Retention rate alone doesn't explain *why*. Layer in feature adoption, support ticket volume, or NPS by cohort to explain retention differences.
6. **Seasonal artifacts** — Q4 cohorts may look worse because they onboarded during holiday staffing gaps, not because of product issues. Control for seasonal effects before drawing product conclusions.
7. **Too many cohorts** — Slicing by 4 dimensions creates dozens of tiny cohorts with no statistical power. Start with one dimension, validate, then add a second.
8. **Incomplete periods** — The most recent cohort always looks like it has worse retention because the period isn't over. Exclude or label incomplete periods clearly.

---

### Further Reading

- [Cohort Analysis 101: How to Reduce Churn and Make Better Product Decisions](https://www.productcompass.pm/p/cohort-analysis)
- [The Product Analytics Playbook: AARRR, HEART, Cohorts & Funnels for PMs](https://www.productcompass.pm/p/the-product-analytics-playbook-aarrr)
- [Are You Tracking the Right Metrics?](https://www.productcompass.pm/p/are-you-tracking-the-right-metrics)
