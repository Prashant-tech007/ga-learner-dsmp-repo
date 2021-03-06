# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
df=pd.read_csv(path)
bank=pd.DataFrame(df)
categorical_var = bank.select_dtypes(include='object')
print(categorical_var)
numerical_var = bank.select_dtypes(include='number')
print(numerical_var)

# code ends here


# --------------
# code starts here
import pandas as pandas
import numpy as np
bank.head()
banks = bank.drop(['Loan_ID'],axis=1)
banks.head()
print(banks.isnull().sum())
bank_mode = banks.mode().iloc[0]
print(bank_mode)
banks = banks.fillna(bank_mode)
print(banks)

#code ends here-


# --------------
# Code starts here
import pandas as pd
import numpy as np

avg_loan_amount = pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values=['LoanAmount'],aggfunc='mean')

print(avg_loan_amount)
# code ends here


# --------------
# code starts here
import pandas as pd
import numpy as np
banks.head()
loan_approved_se = banks.loc[(banks["Self_Employed"]=="Yes")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_se)
loan_approved_nse = banks.loc[(banks["Self_Employed"]=="No")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_nse)

percentage_se = (loan_approved_se * 100 / 614)
percentage_se=percentage_se[0]

print(percentage_se)

percentage_nse = (loan_approved_nse * 100 / 614)
percentage_nse=percentage_nse[0]

print (percentage_nse)

# code ends here


# --------------
# code starts here
import numpy as numpy
import pandas as pd
loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12) 

big_loan_term = len([i for i in loan_term if i>=25])
#big_loan_term = banks.loc[(banks['Loan_Amount_Term']>=25)].count()
print(big_loan_term)
# code ends here



# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')
print(loan_groupby)
loan_groupby = loan_groupby[['ApplicantIncome','Credit_History']]
print(loan_groupby)
mean_values = loan_groupby.mean()
print(mean_values)
# code ends here


