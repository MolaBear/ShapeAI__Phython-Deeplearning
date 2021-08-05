from sklearn.datasets import load_breast_cancer
Data = load_breast_cancer()

data_features = Data.data
target_data = Data.target

from sklearn.model_selection import train_test_split

train_1, test_x, train_2, test_y = train_test_split(data_features, target_data, test_size = 0.2)

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(32, input_dim = 30, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam',metrics=['accuracy'])

model.fit(train_1, train_2, epochs=15)

scores = model.evaluate(test_x, test_y)

predictions = model.predict(test_x)
label=[]
for pred in predictions:
  if pred>=0.5:
   print("Melignent")
  else:
   print("Benign")