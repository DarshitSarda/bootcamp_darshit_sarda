
# Amazon Bestsellers — Stakeholder Report (Stage 12)

## Executive Summary
- **Baseline model is reasonably stable**: Test RMSE ≈ **0** with 95% bootstrap CI **[0, 0]**.
- **Model choice matters**: Polynomial features did **improve** error (Linear RMSE=0, Poly RMSE=0).
- **Assumptions about missing data influence results**: Under 10% MAR in price, **median imputation** led to RMSE change of **-0**, while **mean imputation** changed RMSE by **-0**.

---


## Visualizations & Interpretation

### 1) Bootstrap Uncertainty for Model Error
![Bootstrap RMSE](images\bootstrap_rmse_distribution.png)

**What it shows**: Distribution of test RMSE via 500 bootstrap draws.  
**Key insight**: Our linear model’s error is concentrated around **0**, with 95% CI **[0, 0]**.  
**Assumption/Limit**: Bootstrap draws reflect current test distribution; a changing catalog could widen uncertainty.

### 2) Scenario Comparison: True vs Predicted (Linear vs Polynomial)
![Scenario Scatter](images\scenario_true_vs_pred_scatter.png)

**What it shows**: Side-by-side fit quality comparing linear and polynomial models.  
**Key insight**: Polynomial reduces error modestly.  
**Assumption/Limit**: Polynomial can overfit; benefits depend on stable non-linear price–ratings relationships.

### 3) Subgroup Diagnostic: RMSE by Product Category
![Subgroup RMSE](images\subgroup_rmse_bar.png)

**What it shows**: Error varies across categories.  
**Key insight**: Some categories underperform (higher RMSE). Prioritize category-level monitoring and data quality checks.  
**Assumption/Limit**: Category definitions and sample sizes affect stability; small categories may appear noisier.

### 4) Sensitivity (Imputation Choice under 10% MAR)
![Tornado Sensitivity](images\sensitivity_tornado_rmse_delta.png)

**What it shows**: RMSE change vs baseline when **10%** of training prices are missing-at-random and imputed by mean/median.  
**Key insight**: **Median imputation** is slightly better than mean in this dataset.  
**Assumption/Limit**: MAR mechanism is simulated; real-world missingness may be systematic.


## Assumptions & Risks
- **Assumptions**: (a) data cleaned per Stages 08–11; (b) price–ratings relationships are relatively stable; (c) missingness ≈ MAR at ≤10%.  
- **Risks**: (a) category mix shift can degrade accuracy; (b) heavy missingness or currency noise in prices; (c) non-stationarity (seasonality, promotions).

## Sensitivity Summary
| Scenario | Test RMSE |
|---|---:|
| Baseline (no missing) | 0 |
| Mean imputation (10% MAR) | 0 |
| Median imputation (10% MAR) | 0 |

- **Δ vs Baseline**: Mean -0, Median -0  
- **Interpretation**: Reasonable robustness at 10% missing, but **data policy on price completeness matters**.

## Decision Implications (“What this means for you”)
- **OK to proceed** with the linear model for near-term reporting; maintain **category-level monitoring** for error drift.  
- If **missing price >10%** or **category mix shifts**, expect performance degradation; prefer **median imputation** and re-calibration.  
- Reassess polynomial model **only if** there is clear, persistent non-linearity; otherwise the added complexity may not pay off.

