from typing import Any, Dict, List
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
from scipy.stats import ttest_ind

from data import data_obvious_effect, data_one_animal_skews_result


def fit_mixed_effects(data: List[Dict]) -> float:
    df = pd.DataFrame(data)
    df = df.explode("firing_rate_cell", ignore_index=True)
    df["firing_rate_cell"] = pd.to_numeric(df["firing_rate_cell"])
    df["Animal_ID"] = pd.Categorical(df["Animal_ID"])
    df["genotype"] = pd.Categorical(
        df["genotype"], categories=["WT", "NLGF"], ordered=True
    )

    mixed_lm = smf.mixedlm("firing_rate_cell ~ genotype", df, groups=df["Animal_ID"])
    mixed_lm_fit = mixed_lm.fit()

    return float(mixed_lm_fit.pvalues["genotype[T.NLGF]"])


def fit_basic_ttest(data: List[Dict[str, Any]]) -> float:
    wt: np.ndarray = np.hstack(
        [d["firing_rate_cell"] for d in data if d["genotype"] == "WT"]
    )
    nlgf: np.ndarray = np.hstack(
        [d["firing_rate_cell"] for d in data if d["genotype"] == "NLGF"]
    )

    return float(ttest_ind(wt, nlgf).pvalue)


"""
One animal skews result mixed effects p-value: 0.33
One animal skews result ttest p-value: 0.039

Obvious effect mixed-effects p-value: 1.2e-08
Obvious effect ttest p-value: 2.9e-06

"""

print(
    f"One animal skews result mixed effects p-value: {fit_mixed_effects(data_one_animal_skews_result):.1e}"
)
print(
    f"One animal skews result ttest p-value: {fit_basic_ttest(data_one_animal_skews_result):.1e}"
)
print(
    f"Obvious effect mixed-effects p-value: {fit_mixed_effects(data_obvious_effect):.1e}"
)
print(f"Obvious effect ttest p-value: {fit_basic_ttest(data_obvious_effect):.1e}")
