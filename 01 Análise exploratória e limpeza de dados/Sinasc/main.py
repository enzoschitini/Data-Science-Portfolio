import pandas as pd

class GuidaDataframe:
    def __init__(self, data_frame):
        self.data_frame = data_frame

    def esplorazione(self):
        righe, qnt_colonne = self.data_frame.shape
        quantita_righe = format(righe, ",").replace(',', '.')
        sequenza = list(range(qnt_colonne + 1))
        sequenza = sequenza[1:]

        colonne = self.data_frame.columns.to_list()
        types_list = [str(type(self.data_frame[col][0])).split("'")[1] for col in self.data_frame.columns]
        lista_categorias = [self.data_frame[col].nunique() for col in self.data_frame.columns]

        elementos_nulos = self.data_frame.isnull().sum()
        elementos_nulos = elementos_nulos.to_list()

        memoria = (self.data_frame.memory_usage(deep=True) / (1024 ** 2)).round() # Mb
        lista_memoria = memoria.to_list()
        lista_memoria = lista_memoria[1:]

        memoria = self.data_frame.memory_usage(deep=True) # Total Mb
        memoria_total = round(memoria.sum() / (1024 ** 2), 2)

        percentagem_dados_nulos = round((self.data_frame.isnull().sum() / righe) * 100)
        percentagem_dados_nulos = percentagem_dados_nulos.to_list()

        dados = pd.DataFrame({'Nome': colonne, 
                             'Tipo': types_list, 
                             'qnt_categorias': lista_categorias,
                             'Dados nulos' : elementos_nulos,
                             'Dados nulos %' : percentagem_dados_nulos,
                             'Memória (Mb)': lista_memoria}, index=sequenza)
        
        # Títulos
        print('Tabela Exploratória')
        print(f'Nesses dados temos {quantita_righe} linhas e {qnt_colonne} colunas.')
        print(f'Consumo de memória: {memoria_total}Mb.')
        
        return dados
    
    def Machine_Learning(dataframe):
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.model_selection import train_test_split
        from imblearn.under_sampling import RandomUnderSampler
        import numpy as np
        from sklearn.metrics import precision_score
        from sklearn.metrics import classification_report

        dataframe = pd.get_dummies(dataframe)
        y = dataframe['default']
        X = dataframe.drop('default', axis=1)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)
       
        rus = RandomUnderSampler(random_state=42)
        X_train, y_train = rus.fit_resample(X_train, y_train)

        X_train, y_train = rus.fit_resample(X_train, y_train)

        clf = DecisionTreeClassifier(random_state=100)
        path = clf.cost_complexity_pruning_path(X_train, y_train)
        ccp_alphas, impurities = path.ccp_alphas, path.impurities

        clfs = []
        for ccp_alpha in ccp_alphas:
            clf = DecisionTreeClassifier(random_state=0, ccp_alpha=ccp_alpha)
            clf.fit(X_train, y_train)
            clfs.append(clf)

        train_scores = [clf.score(X_train, y_train) for clf in clfs]
        test_score = [clf.score(X_test, y_test) for clf in clfs]

        clf_df4 = DecisionTreeClassifier(ccp_alpha=0.001359, random_state=100) # 0.001359
        clf_df4.fit(X_train, y_train)

        predictions = clf_df4.predict(X_test)
    
        count_0 = np.count_nonzero(predictions == 0)
        count_1 = np.count_nonzero(predictions == 1)

        proportion_0 = count_0 / len(predictions)
        proportion_1 = count_1 / len(predictions)

        print("Proporzione di 0:", proportion_0)
        print("Proporzione di 1:", proportion_1)

        def grafico():
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots()
            ax.set_xlabel('Alpha')
            ax.set_ylabel("Accuratezza vs alpha dell'addesttramento e teste")
            ax.plot(ccp_alphas, train_scores, marker='o', label='Addestramento',
                    drawstyle='steps-post')
            ax.plot(ccp_alphas, test_score, marker='o', label='Teste',
                    drawstyle='steps-post')
            ax.legend()
            plt.show()
        
        def prestazioni(albero, teste_x, teste_y):
            from sklearn.metrics import precision_score
            from sklearn.metrics import accuracy_score
            from sklearn.metrics import confusion_matrix
            from sklearn.metrics import recall_score

            predictions = albero.predict(teste_x)
            accuracy = accuracy_score(teste_y, predictions)
            precision_score_value = precision_score(teste_y, predictions)
            recall_score_value = recall_score(teste_y,predictions)
            
            print("Accuracy:", (accuracy * 100).round(), "%")
            print('\nConfusion Matrix:')
            print(confusion_matrix(teste_y,predictions))
            print("\nRecall Score:", (recall_score_value * 100).round(), "%")
            print('\nPrecision Score Value', (precision_score_value * 100).round(), "%")
        
        prestazioni(clf_df4, X_test, y_test)
        precision_score(y_test, predictions)
        print(classification_report(y_test, predictions, target_names=['0', '1']))

        feature_names = X.columns

        feature_importance = pd.DataFrame(clf_df4.feature_importances_, index = feature_names).sort_values(0, ascending=False)
        feature_importance.head(5)

        features = list(feature_importance[feature_importance[0]>0].index)
        feature_importance.head(10).plot(kind='bar')

        def arvore():
            import matplotlib.pyplot as plt
            from sklearn import tree

            fig = plt.figure(figsize=(25,15))
            _ = tree.plot_tree(clf_df4, 
                            feature_names=feature_names,  
                            class_names={0:'Paga', 1:'Não paga'},
                            filled=True,
                            fontsize=12)