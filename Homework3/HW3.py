#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import seaborn as sns


# In[2]:


data = pd.read_csv('cses4_cut.csv')


# In[3]:


data.head()


# In[4]:


data.shape


# In[5]:


data.describe


# In[6]:


# from this survey result, it seems like that D2005 to D2009 has similiar value and same order.


# In[7]:


for column in data:
    print(column)
    print(data[column].value_counts())
    print('-----------------')


# In[8]:


# Data Cleaning
# Before the machine Learning, I would like to clean the dataset first for getting rid of unmeaningful data


# In[9]:


data = data.drop(columns = ['Unnamed: 0'])


# In[10]:


# proved that D 2005 to D 2009 has very smiliar value and order, which is not meaningful for the research analysis. So I would drop out these except D2009 and Unnamed:0.
data = data.drop(columns = ['D2005','D2006', 'D2007','D2008'])


# In[11]:


data.head()


# In[12]:


# unique values in each columns
for x in data.columns:
    #prinfting unique values
    print(x ,':', len(data[x].unique()))


# In[13]:


# To check the missing value
data.info()


# In[14]:


# check the null values
print(data.isnull().sum())


# In[15]:


print(data['voted'].value_counts())


# In[16]:


# categorical to change to numeric label. LabelEncoder() can be used to achieve this:
from sklearn.preprocessing import LabelEncoder
label_voted = LabelEncoder()
data['voted'] = label_voted.fit_transform(data['voted'])


# In[17]:


data.head(5)


# In[18]:


ohe = ['D2002','D2003','D2004','D2009','D2010','D2011','D2012','D2013','D2014','D2015','D2016','D2017','D2018','D2019','D2020','D2021','D2016','D2017','D2018','D2019','D2020','D2021','D2022','D2023','D2024','D2025','D2026','D2027','D2016','D2017','D2018','D2019','D2020','D2021','D2016','D2017','D2018','D2019','D2020','D2021','D2022','D2023','D2024','D2025','D2026','D2027','D2028','D2029','D2030','D2031']


# In[19]:


new_data= pd.get_dummies(data, prefix=ohe, columns= ohe)


# In[20]:


new_data


# # Machine Learning

# In[21]:


#Import necessary libraries and metrics
from sklearn.metrics import classification_report,confusion_matrix, roc_auc_score, accuracy_score
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, RandomizedSearchCV, cross_val_score, StratifiedKFold


# In[22]:


# Variable Selection: Setting the dependent and independent variables
Y = new_data['voted']
X= new_data.drop(columns = ['voted'], axis=1)


# In[23]:


# train test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)


# In[24]:


# Scaling the data to take account of variations in mean and standard deviations
sc=StandardScaler()
X_train1 = sc.fit_transform(X_train)
X_test1 = sc.fit_transform(X_test)
X_train1[:]
X_test1[:]


# In[25]:


norm = StandardScaler().fit(X)

# transform training data
X_train_norm = norm.transform(X_train)
print("Scaled Train Data: \n\n")
print(X_train_norm)


# In[26]:


#Create a function within many Machine Learning Models
def LinReg(X,Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
    #Using Logistic Regression Algorithm to the Training Set
    log = LogisticRegression(random_state = 0, solver='lbfgs', max_iter=2000)
    log.fit(X_train, Y_train)
    predictions = log.predict(X_test)
    

    #print model accuracy on the training data.
    print('[0]Logistic Regression Training Accuracy:', "%.4g" % accuracy_score(Y_test, predictions))
    print ("[0]Logistic Regression AUC Score : %f" % roc_auc_score(Y_test, predictions))
    
    return log


# In[27]:


def KNeig(X,Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
    #Using KNeighborsClassifier Method of neighbors class to use Nearest Neighbor algorithm
    knn = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
    knn.fit(X_train, Y_train)
    predictions = knn.predict(X_test)
    
    print('[1]K Nearest Neighbor Training Accuracy:', "%.4g" % accuracy_score(Y_test, predictions))
    print ("[1]K Nearest Neighbor AUC Score : %f" % roc_auc_score(Y_test, predictions))

      
    return knn


# In[28]:


def svcm(X,Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
    #Using SVC method of svm class to use Support Vector Machine Algorithm
    svc_lin = SVC(gamma='auto', kernel = 'linear', random_state = 0)
    svc_lin.fit(X_train, Y_train)
    predictions = svc_lin.predict(X_test)
    
    print('[2]Support Vector Machine (Linear Classifier) Training Accuracy:', "%.4g" % accuracy_score(Y_test, predictions))
    print ("[2]Support Vector Machine (Linear Classifier) AUC Score : %f" % roc_auc_score(Y_test, predictions))
    
    return svc_lin


# In[29]:


def DecTree(X,Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
    #Using DecisionTreeClassifier of tree class to use Decision Tree Algorithm
    tree = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
    tree.fit(X_train, Y_train)
    predictions = tree.predict(X_test)
    print('[3]Decision Tree Classifier Training Accuracy:', "%.4g" % accuracy_score(Y_test, predictions))
    print ("[3]Decision Tree Classifier AUC Score : %f" % roc_auc_score(Y_test, predictions))

    return tree


# In[ ]:


#Create a function within many Machine Learning Models
def RanForest(X,Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
  #Using RandomForestClassifier method of ensemble class to use Random Forest Classification algorithm
    forest = RandomForestClassifier(n_estimators = 5000, criterion = 'entropy', random_state = 0)
    forest.fit(X_train, Y_train)
    predictions = forest.predict(X_test)
      
  #print model accuracy on the training data.
    print('[4]Random Forest Classifier Training Accuracy:', "%.4g" % accuracy_score(Y_test, predictions))
    print ("[4]Random Forest Classifier AUC Score : %f" % roc_auc_score(Y_test, predictions))


    return forest


# # Evaluating Performance on Traning Sets

# In[31]:


LinReg(X,Y)


# In[32]:


KNeig(X,Y)


# In[33]:


svcm(X,Y)


# In[34]:


DecTree(X,Y)


# In[35]:


RanForest(X,Y)


# In[ ]:


#RanForest(X['age','D2002_1','D2002_2','D2003_1','D2003_2','D2003_3','D2003_4','D2003_5','D2003_6','D2003_7','D2003_8','D2003_9','D2003_96','D2003_97','D2003_98','D2003_99','D2004_1','D2004_2','D2004_3','D2004_4'],Y)


# # Optimization

# In[38]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

data_scaled = X.copy()
col_names = X.columns
features = X[col_names]

data_scaled[col_names] = scaler.fit_transform(features.values)


# In[40]:


KNeig(data_scaled,Y)


# # Finding a best features

# In[43]:


#apply SelectKBest class to extract top 10 best features
bestfeatures = SelectKBest(score_func=chi2, k=15)
fit = bestfeatures.fit(X_train,Y_train)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(X.columns)

#concat two dataframes for better visualization 
featureScores = pd.concat([dfcolumns,dfscores],axis=1)
featureScores.columns = ['Specs','Score']  
print(featureScores.nlargest(15,'Score'))


# # Random Search

# In[41]:


from pprint import pprint

# Number of trees in random forest, I choose low because otherwise takes lot of time.
n_estimators = [200]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf}
pprint(random_grid)


# In[ ]:


#With these features, it performed best. That's why we will implement grid search on this data.
new_X = X[['age','D2002_1','D2002_2','D2003_1','D2003_2','D2003_3','D2003_4','D2003_5','D2003_6','D2003_7','D2003_8','D2003_9','D2003_96','D2003_97','D2003_98','D2003_99','D2004_1','D2004_2','D2004_3','D2004_4']]
X_train, X_test, y_train, y_test = train_test_split(new_X, Y, test_size = 0.2, random_state = 0)
# Use the random grid to search for best hyperparameters
# First create the base model to tune
rf = RandomForestClassifier()
# Random search of parameters, using 3 fold cross validation, 
# search across 100 different combinations, and use all available cores
rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1, scoring = 'roc_auc')
# Fit the random search model

rf_random.fit(X_train, Y_train)


# In[ ]:


rf_random.best_params_


# In[ ]:


random_search.best_score_


# In[ ]:


rfc = RandomForestClassifier(n_estimators= 1000,
 min_samples_split= 10,
 min_samples_leaf= 2,
 max_depth= 10)

rfc.fit(X_train,y_train)
predictions = rfc.predict(X_test)
        
#Print model report:
print('[4]Random Forest Classifier Training Accuracy:', "%.4g" % accuracy_score(Y_test, predictions))
print ("[4]Random Forest Classifier AUC Score : %f" % roc_auc_score(Y_test, predictions))


# random_search = RandomizedSearchCV(RandomForestRegressor(random_state=0),
#                            {
#                               'n_estimators':np.arange(5,100,5),
#                               'max_features':np.arange(0.1,1.0,0.05),
#                             },cv=5, scoring="r2",verbose=1,n_jobs=-1, 
#                              n_iter=50, random_state = 0
#                            )
# random_search.fit(X_train,Y_train)

# random_search.best_params_

# random_search.best_score_

# In[ ]:





# #Normalizing the dataset to see how the accuracy improves
# # scaling values into 0-1 range
# #from sklearn.preprocessing import MinMaxScaler
# #scaler = MinMaxScaler(feature_range=(0, 1))
# #features = new_data.drop(columns = ['voted'], axis=1)
# #new_data[features] = scaler.fit_transform(new_data[features])

#     #Print Feature Importance:
#     def importance_check(importance,names,model_type, top_x_features):
#         #Create arrays from feature importance and feature names
#         feature_importance = np.array(importance)
#         feature_names = np.array(names)
#         
#         feature_names = feature_names[:top_x_features]
#         print(feature_names)
#         feature_importance = feature_importance[:top_x_features]
#         #Create a DataFrame using a Dictionary
#         data={'feature_names':feature_names,'feature_importance':feature_importance}
#         fi_df = pd.DataFrame(data)
# 
#         #Sort the DataFrame in order decreasing feature importance
#         fi_df.sort_values(by=['feature_importance'], ascending=False,inplace=True)
# 
#         #Define size of bar plot
#         plt.figure(figsize=(10,8))
#         #Plot Searborn bar chart
#         sns.barplot(x=fi_df['feature_importance'], y=fi_df['feature_names'])
#         #Add chart labels
#         plt.title('FEATURE IMPORTANCE')
#         plt.xlabel('FEATURE IMPORTANCE')
#         plt.ylabel('FEATURE NAMES')
#         
#     importance_check(forest.feature_importances_, X.columns, 'Random Forest ', 20)
#       

# In[ ]:





# In[ ]:





# 

# In[ ]:





# In[ ]:




