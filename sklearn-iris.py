import streamlit as st 
import numpy as np 
import pandas as pd

#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import classification_report
from PIL import Image
import pickle
model = pickle.load(open('IRIS-model.pkl', 'rb'))

st.title('Iris: Flower Class Prediction')
image = Image.open('iris-flower.png')
st.image(image)

readme = st.checkbox("README First")

if readme:

    st.write("""
        **Critical information for this web app demo are shown below:**
        \n * Scikit Learn Model: [Logistic Regression](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)
        \n * Host & Libraries: [Streamlit](https://streamlit.io/)
        \n * Code Repository: [Github](https://github.com/Tsuen86/iris-classification/)
        """)

st.sidebar.write("""
This is a web app to predict the class species of an Iris flower based on its sepal and petal dimensions (length, width)
""")

st.sidebar.write("Please adjust slider values, to get Class Prediction %")

SepalLengthCm = st.sidebar.slider('Sepal Length (cm):', 2.0, 8.0)
SepalWidthCm = st.sidebar.slider('Sepal Width (cm):', 0.0, 5.0)
PetalLengthCm = st.sidebar.slider('Petal Length (cm)',0.0, 7.0)
PetalWidthCm = st.sidebar.slider('Petal Width (cm):', 0.0, 2.5)
data = {'SepalLengthCm': SepalLengthCm,
        'SepalWidthCm': SepalWidthCm,
        'PetalLengthCm': PetalLengthCm,
        'PetalWidthCm': PetalWidthCm}

features = pd.DataFrame(data, index=[0])

pred_proba = model.predict_proba(features)

st.subheader('Class Prediction Percentages:') 
st.write('**Probablity of Iris Class being Iris-setosa is ( in % )**:',pred_proba[0][0]*100)
st.write('**Probablity of Isis Class being Iris-versicolor is ( in % )**:',pred_proba[0][1]*100)
st.write('**Probablity of Isis Class being Iris-virginica ( in % )**:',pred_proba[0][2]*100)

st.sidebar.write ("For more info, please contact:")

st.sidebar.write("<a href='https://www.linkedin.com/in/huei-tsuen-lim-89225536/'>Lim Huei Tsuen </a>", unsafe_allow_html=True)

# choice = st.sidebar.radio(
#     "Choose a dataset",   
#     ('Default', 'User-defined '),
#     index = 0
    
# )

# st.write(f"## You Have Selected <font color='Aquamarine'>{choice}</font> Dataset", unsafe_allow_html=True)

# def get_default_dataset(name):
#     data = None
#     if name == 'Iris':
#         data = datasets.load_iris()
#     elif name == 'Wine':
#         data = datasets.load_wine()
#     else:
#         data = datasets.load_breast_cancer()
#     X = data.data
#     y = data.target
#     return X, y

# def add_dataset_ui(choice_name):
#     X=[]
#     y=[]
#     X_names = []
#     X1 = []
#     if choice_name == 'Default':
#        dataset_name = st.sidebar.selectbox(
#             'Select Dataset',
#             ('Iris', 'Breast Cancer', 'Wine')
#         )
#        X, y = get_default_dataset (dataset_name)
#        X_names = X
#     else:
#         uploaded_file = st.sidebar.file_uploader(
#             "Upload a CSV",
#             type='csv'    )
        

#         if uploaded_file!=None:
           
#            st.write(uploaded_file)
#            data = pd.read_csv(uploaded_file)
  
        
#            y_name = st.sidebar.selectbox(
#                     'Select Label @ y variable',
#                     sorted(data)
#                     )

#            X_names = st.sidebar.multiselect(
#                      'Select Predictors @ X variables.',
#                      sorted(data),
#                      default = sorted(data)[1],
#                      help = "You may select more than one predictor"
#                      )

#            y = data.loc[:,y_name]
#            X = data.loc[:,X_names]
#            X1 = X.select_dtypes(include=['object'])
        
#            X2 = X.select_dtypes(exclude=['object'])

#            if sorted(X1) != []:
#               X1 = X1.apply(LabelEncoder().fit_transform)
#               X = pd.concat([X2,X1],axis=1)

#            y = LabelEncoder().fit_transform(y)
#         else:
#            st.write(f"## <font color='Aquamarine'>Note: Please upload a CSV file to analyze the data.</font>", unsafe_allow_html=True)

#     return X,y, X_names, X1

# X, y , X_names, cat_var= add_dataset_ui (choice)




# classifier_name = st.sidebar.selectbox(
#     'Select classifier',
#     ('KNN', 'SVM', 'Random Forest')
# )

# test_data_ratio = st.sidebar.slider('Select testing size or ratio', 
#                                     min_value= 0.10, 
#                                     max_value = 0.50,
#                                     value=0.2)
# random_state = st.sidebar.slider('Select random state', 1, 9999,value=1234)

# st.write("## 1: Summary (X variables)")


# if len(X)==0:
#    st.write("<font color='Aquamarine'>Note: Predictors @ X variables have not been selected.</font>", unsafe_allow_html=True)
# else:
#    st.write('Shape of predictors @ X variables :', X.shape)
#    st.write('Summary of predictors @ X variables:', pd.DataFrame(X).describe())

# st.write("## 2: Summary (y variable)")

# if len(y)==0:
#    st.write("<font color='Aquamarine'>Note: Label @ y variable has not been selected.</font>", unsafe_allow_html=True)
# elif len(np.unique(y)) <5:
#      st.write('Number of classes:', len(np.unique(y)))

# else: 
#    st.write("<font color='red'>Warning: System detects an unusual number of unique classes. Please make sure that the label @ y is a categorical variable. Ignore this warning message if you are sure that the y is a categorical variable.</font>", unsafe_allow_html=True)
#    st.write('Number of classes:', len(np.unique(y)))


# def add_parameter_ui(clf_name):
#     params = dict()
#     if clf_name == 'SVM':
#         C = st.sidebar.slider('C', 0.01, 10.0,value=1.0)
#         params['C'] = C
#     elif clf_name == 'KNN':
#         K = st.sidebar.slider('K', 1, 15,value=5)
#         params['K'] = K
#     else:
#         max_depth = st.sidebar.slider('max_depth', 2, 15,value=5)
#         params['max_depth'] = max_depth
#         n_estimators = st.sidebar.slider('n_estimators', 1, 100,value=10)
#         params['n_estimators'] = n_estimators
#     return params

# params = add_parameter_ui(classifier_name)

# def get_classifier(clf_name, params):
#     clf = None
#     if clf_name == 'SVM':
#         clf = SVC(C=params['C'])
#     elif clf_name == 'KNN':
#         clf = KNeighborsClassifier(n_neighbors=params['K'])
#     else:
#         clf = clf = RandomForestClassifier(n_estimators=params['n_estimators'], 
#             max_depth=params['max_depth'], random_state=random_state)
#     return clf

# clf = get_classifier(classifier_name, params)


# st.write("## 3: Classification Report")

# if len(X)!=0 and len(y)!=0: 


#   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_data_ratio, random_state=random_state)

#   scaler = StandardScaler()
#   X_train_scaled = scaler.fit_transform(X_train)
#   X_test_scaled = scaler.transform(X_test)    

#   clf.fit(X_train_scaled, y_train)
#   y_pred = clf.predict(X_test_scaled)


#   st.write('Classifier:',classifier_name)
#   st.write('Classification report:')
#   report = classification_report(y_test, y_pred,output_dict=True)
#   df = pd.DataFrame(report).transpose()
#   st.write(df)

# else: 
#    st.write("<font color='Aquamarine'>Note: No classification report generated.</font>", unsafe_allow_html=True)
          
            
# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
