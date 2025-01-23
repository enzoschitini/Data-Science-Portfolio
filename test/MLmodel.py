from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

def Variabile_Migliore(dataframe: pd.DataFrame, variabile_impostata: str):
    dataframe = dataframe.drop_duplicates()

    dataframe = pd.get_dummies(dataframe)
    
    X = dataframe.drop(columns=[variabile_impostata])
    y = dataframe[variabile_impostata]
    
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.25, random_state=1729)
    
    clf = DecisionTreeClassifier(max_depth=4, random_state=1729)
    clf.fit(X_train, y_train)
    
    features_names = X_train.columns
    features_importance = pd.DataFrame(clf.feature_importances_, index=features_names, columns=['Importance']).sort_values(by='Importance', ascending=False)
    
    print('Top 25 Features:')
    print(features_importance.head(25))
    
    return features_importance.head(25)

"""ML = df.copy()
ML['default'] = [1 if valore == 'Vaginal' else 0 for valore in ML['PARTO']]
# ML['default'] = [1 if valore == 'Vaginal' else 2 if valore == 'ddd' else 0 for valore in ML['PARTO']]
ML = ML[['ESCMAE', 'GRAVIDEZ', 'GESTACAO', 'RACACOR', 'SEXO', 'default', 'QTDFILVIVO', 'faixa_mae']]

Variabile_Migliore(ML, 'default')#.to_csv('l.csv')"""