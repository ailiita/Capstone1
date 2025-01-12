import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold
import pickle

# ------------------- Model Parameters -------------------------------------

output_file = 'model_lr.bin' 

n_splits = 5
random_state = 42
# Data preparation ------------------------------------------------------------
df = pd.read_csv('flood_cleaned.csv', delimiter=',')


# Splitting data --------------------------------------------------------------
df_full_train, df_test = train_test_split(df, test_size=0.2, shuffle = True)
df_train = df_full_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y = df_full_train.flood_probability
y_train = df_train.flood_probability
y_test = df_test.flood_probability

del df_full_train['flood_probability']
del df_train['flood_probability']
del df_test['flood_probability']

dico = df_full_train.to_dict(orient='records')
train_dicts = df_train.to_dict(orient='records')
train_test = df_test.to_dict(orient='records')

dv = DictVectorizer(sparse=False)
X = dv.fit_transform(dico)
X_train = dv.fit_transform(train_dicts)
X_test = dv.transform(train_test)

features = dv.get_feature_names_out()

# Training ------- ------------------------------------------------------------

# Validation   ------------------------------------------------------------
print('Doing cross-validation --------------------------------------------- ')

model = LinearRegression()

kf = KFold(n_splits=n_splits, shuffle=True, random_state=random_state)

rmse_scores = []
i=1
for train_index, test_index in kf.split(X_train):
    X_train_fold, X_test_fold = X_train[train_index], X_train[test_index]
    y_train_fold, y_test_fold = y_train[train_index], y_train[test_index]
    
    model.fit(X_train_fold, y_train_fold)
    
    y_pred = model.predict(X_test_fold)
    
    rmse = np.sqrt(mean_squared_error(y_test_fold, y_pred))
    rmse_scores.append(rmse)
    
    print(f"RMSE for fold {i}: {rmse}")
    i+=1

print('Cross-validation results : ')
print(' %.3f +- %.3f' % ( np.mean(rmse_scores), np.std(rmse_scores)))

# Train Final model --------------------------------------------------------
print('Training final model')

model = LinearRegression()

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f' Validation RMSE : {rmse}')


# Save the model -----------------------------------------------------------

with open(output_file, 'wb') as f_out :
    pickle.dump((dv,model), f_out)
    
print(f'Model is saved to {output_file}')

