import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor,plot_tree

#Sample data for regression
data = {
    'size': [1500, 1700, 1800, 1900, 2100],
    'Prize': [30000, 35000,40000,43000,49000]
}
#Convert dataframe
df = pd.DataFrame(data)

#Define features and target
X= df[['size']]
Y= df[['Prize']]

#Create and train the model with default MSE criterion
regressor = DecisionTreeRegressor()
regressor.fit(X,Y)

#plot the tree
plt.figure(figsize= (10,8))
plot_tree(regressor, feature_names=['size'], filled=True)
plt.title("Decision Tree Regression")
plt.show()

