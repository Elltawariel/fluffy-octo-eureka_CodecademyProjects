import scipy.stats as stats
import numpy as np

### Task Group 1 ###
## Task 1: 
lam = 7
## Task 2:
print(stats.poisson.pmf(7, 7))

## Task 3:
print(stats.poisson.pmf(4, 7))

## Task 4:
print(1 - stats.poisson.pmf(9, 7))


### Task Group 2 ###
## Task 5:
year_defects = stats.poisson.rvs(lam, size = 365)
## Task 6:
print(year_defects[:20])
## Task 7:
print(lam*365)

## Task 8:
print(sum(year_defects))
## Task 9:
print(sum(year_defects)/365)

## Task 10:
print(max(year_defects))
## Task 11:
print(1 - stats.poisson.pmf(max(year_defects) - 1, 7))

### Extra Bonus ###
# Task 12
print(stats.poisson.ppf(0.9, 7))
# Task 13
print(sum(year_defects >= 10)/len(year_defects))
