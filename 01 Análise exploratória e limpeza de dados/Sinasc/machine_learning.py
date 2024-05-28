
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.tree import plot_tree
from sklearn.tree import DecisionTreeClassifier
from imblearn.under_sampling import RandomUnderSampler

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score
from sklearn.metrics import classification_report

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import pickle

class MLM(object):
    def __init__(self) -> None:
        pass

    def Machine_Learning(self, dataframe):

        def desempenho(arvore, teste_x, teste_y):
            from sklearn.metrics import precision_score
            predictions = arvore.predict(teste_x)
            accuracy = accuracy_score(teste_y, predictions)
            precision_score_value = precision_score(teste_y, predictions)
            recall_score_value = recall_score(teste_y,predictions)
            
            print("Accuracy:", (accuracy * 100).round(), "%")
            print('\nConfusion Matrix:')
            print(confusion_matrix(teste_y,predictions))
            print("\nRecall Score:", (recall_score_value * 100).round(), "%")
            print('\nPrecision Score Value', (precision_score_value * 100).round(), "%")

        PAIS = dataframe[dataframe['IDADEPAI'] != 0]
        PAIS = PAIS.drop_duplicates()

        def default(row):
            if (row['IDADEMAE'] <= 18) & (row['IDADEPAI'] > 18):
                return 1
            else:
                return 0

        PAIS['default'] = PAIS.apply(default, axis=1)
        PAIS = PAIS[['IDADEMAE', 'PESO', 'default']]

        df = PAIS
        df = pd.get_dummies(df)

        y = df['default']
        X = df.drop('default', axis=1)

        clf_df = DecisionTreeClassifier(random_state=100)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)

        clf_df.fit(X_train, y_train)

        #y.value_counts().plot.pie(autopct='%.2f');

        rus = RandomUnderSampler(random_state=42)
        X_train, y_train = rus.fit_resample(X_train, y_train)
        X_train, y_train = rus.fit_resample(X_train, y_train)

        y_train.value_counts().plot.pie(autopct='%.2f');

        clf = DecisionTreeClassifier(random_state=100)
        path = clf.cost_complexity_pruning_path(X_train, y_train)
        ccp_alphas, impurities = path.ccp_alphas, path.impurities

        clf_df4 = DecisionTreeClassifier(ccp_alpha=0.001359, random_state=100) # 0.001359
        clf_df4.fit(X_train, y_train)

        plt.figure(figsize=(25, 10))
        plot_tree(clf_df4,
                filled=True,
                feature_names=X_train.columns);

        predictions = clf_df4.predict(X_test)

        count_0 = np.count_nonzero(predictions == 0)
        count_1 = np.count_nonzero(predictions == 1)

        proportion_0 = count_0 / len(predictions)
        proportion_1 = count_1 / len(predictions)

        print("Proporção de 0:", proportion_0)
        print("Proporção de 1:", proportion_1)

        desempenho(clf_df4, X_test, y_test)
        print(classification_report(y_test, predictions, target_names=['0', '1']))

        feature_names = X.columns

        feature_importance = pd.DataFrame(clf_df4.feature_importances_, index = feature_names).sort_values(0, ascending=False)
        features = list(feature_importance[feature_importance[0]>0].index)

        with open('clf_model.pkl', 'wb') as model_file:
            pickle.dump(clf_df4, model_file)

        print("Modello salvato correttamente in 'clf_model.pkl'")

        with open('clf_model.pkl', 'rb') as model_file:
            loaded_model = pickle.load(model_file)

        Sinasc = dataframe
        Sinasc_Ml = Sinasc[['IDADEMAE', 'PESO']]
        Sinasc_Ml.head()

        new_predictions = loaded_model.predict(Sinasc_Ml)
        Sinasc_Ml['Target'] = new_predictions
        pd.DataFrame(Sinasc_Ml)

        predictions = Sinasc_Ml['Target']
        predictions.to_csv('predictions.csv')
