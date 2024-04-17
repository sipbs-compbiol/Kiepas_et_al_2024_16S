# Removing ambiguity
Scripts in this folder were used to identify and exclude sequences with ambiguity count that significantly differs from others. 

## Model choice and parametrising
Distribution of ambiguity symbols present in each sequence showed over-dispersion with 498.3 variance and 5.5 mean (`get_ambiguity_stats_info.py`), thus negative binomial statistical model was used to identify a threshold at which outlier sequences should be discarded. 

A threshold value was calculated for Negative Binomial Distribution in R using qnbinom(), where $\mu$ was the mean count of ambiguity per sequences, and n was the run of positive outcomes treated as dipersion parameter, calulated with the following formulae:


$$ \mu = {total\ count\ of\ ambiguity\ symbols \over total\ number\ of\ sequences} $$



$$ n = {\mu p\over 1 - p} $$

where $p$ is the probablity calculayed as follow:

$$ p = {total\ count\ of\ ambiguity\ symbols \over total\ count\ of\ all\ babes\ in\ all\ sequences} $$

Parameters were calculated using `get_parameters_for_qnbinom.py`

# Choosing appropriate thereshol for *Streptomyces*
Sequences with more than 14, 153 and 536 ambiguity symbols were found to be outliers at the p values of 0.05, 0.01 and 0.001, respectively (`qnbinom.R`). The shortest sequence length in this study was 1200bp. Thus, retaining sequences with as many as 536 ambiguity symbols is equivalent to missing half of the biological information. This could negatively affect phylogenetic analysis, leading to inac- curate tree topology estimation. Therefore, excluding sequences at P < 0.001 was not considered. Retaining sequences with as many as 153 ambiguity sym- bols is comparable to losing one conserved region. Taking into consideration that this study is based on whole 16S rRNA sequences, there is still enough bi- ological information to distinguish between different species. Additionally, only 100 sequences had more than 14 and less than 153 ambiguity symbols, therefore that does not substantially reduce the number of sequences in the database. Hence, sequences with ambiguity symbols were discarded at P < 0.01 (`remove_ambiguity.py`).
