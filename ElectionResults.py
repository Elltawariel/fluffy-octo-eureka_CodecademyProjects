import codecademylib
import numpy as np
from matplotlib import pyplot as plt


survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']



total_ceballos = sum([1 for n in survey_responses if n == "Ceballos"])
print(total_ceballos)
print(len(survey_responses))
leng = float(len(survey_responses))
percentage_ceballos = 100 * total_ceballos/len(survey_responses)
print(percentage_ceballos)
print(leng)
prediction = np.random.binomial(70, 0.54, size=10000)
possible_surveys = np.random.binomial(leng, 0.54, size=10000) / leng
plt.hist(possible_surveys, range=(0, 1), bins=20)
plt.show()
poss_len = float(len(possible_surveys))

print(poss_len)
large_survey = np.random.binomial(7000.0, 0.54, size=10000) / 7000.0
plt.hist(large_survey, range=(0, 1), bins=20)
plt.show()
ceballos_loss_surveys = np.mean(possible_surveys < 0.5)
print(ceballos_loss_surveys)
ceballos_loss_new = np.mean(possible_surveys > 0.5)
print(ceballos_loss_new)


ceballos_loss_surveys = np.mean(possible_surveys < 0.5)
print('loss percentage '+str (ceballos_loss_surveys))

large_survey = np.random.binomial(7000,0.5,size=10000)/7000.0
print('large_survey'+str(large_survey))
plt.hist(possible_surveys,bins=20,range=(0,1))
plt.hist(large_survey,alpha=.4,bins=20,range=(0,1))

plt.show()

ceballos_loss_new = np.mean(large_survey < 0.5)
print(ceballos_loss_new)
