from sklearn.feature_extraction.text import CountVectorizer

data = []
data_labels = []
with open("pos.txt", encoding='utf8') as f:
    for i in f: 
        data.append(i) 
        data_labels.append('pos')

with open("neg.txt", encoding='utf8') as f:
    for i in f: 
        data.append(i)
        data_labels.append('neg')

with open("mix.txt", encoding='utf8') as f:
    for i in f: 
        data.append(i)
        data_labels.append('mix')


with open("nuet.txt", encoding='utf8') as f:
    for i in f: 
        data.append(i)
        data_labels.append('nuet')

vectorizer = CountVectorizer(
    analyzer = 'word',
    lowercase = False,
)
features = vectorizer.fit_transform(
    data
)
features_nd = features.toarray() # for easy usage
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test  = train_test_split(
        features_nd, 
        data_labels,
        train_size=0.80, 
        random_state=1234)      

from sklearn.linear_model import LogisticRegression
log_model = LogisticRegression()

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
log_model = log_model.fit(X=X_train, y=y_train0)

y_pred = log_model.predict(X_test)

import random
j = random.randint(0,len(X_test)-7)
for i in range(j,j+15):
    print(y_pred[0])
    ind = features_nd.tolist().index(X_test[i].tolist())
    print(data[ind].strip())

from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score


print(recall_score(y_test, y_pred,average='micro'))
print(precision_score(y_test, y_pred, average='micro'))
print(f1_score(y_test, y_pred, average='micro'))