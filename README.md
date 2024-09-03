## Mixed-effects model demo

* This repository shows how to use mixed effects models with example data of "firing rates" recorded in NLGF and WT mice.

* One fake dataset `data_obvious_effect` has an obvious effect where the firing rates are elevated in all NLGF cells.  

* The other fake dataset  `data_one_animal_skews_result` has only one NLGF “mouse” with high firing rates (which positively skews the mean across all cells). 

* The example computes a p value, testing for significance between the firing rates in "WT" and "NLGF" mice, using a mixed effects model and a simple ttest approach. 

* Both approaches show a signficant difference in the `data_obvious_effect` dataset. However the mixed-effects model is not significant for the `data_one_animal_skews_result` whereas the ttest is. 

* All relevant code and the resulting p values are in `mixed_effects.py`