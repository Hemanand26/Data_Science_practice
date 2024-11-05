from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

my_data = pd.read_csv("train.csv")

y = my_data["Survived"]

numerical_columns = ["Age","Fare","SibSp"]
categorical_columns = ["Embarked","Sex","Pclass"]

x = my_data[numerical_columns + categorical_columns]

number_transformer = SimpleImputer(strategy = "mean")
categorical_data_transformer = Pipeline(steps=[('imputer',SimpleImputer(strategy='most_frequent')),('onehot',OneHotEncoder(handle_unknown='ignore'))])

data_pre_processing = ColumnTransformer(transformers = [("num",number_transformer,numerical_columns),("cat",categorical_data_transformer,categorical_columns)])

post_transformation = data_pre_processing.fit_transform(x)

cat_columns = data_pre_processing.named_transformers_["cat"].named_steps["onehot"].get_feature_names_out(categorical_columns)

final_column_names = numerical_columns + cat_columns.tolist()

final_df = pd.DataFrame(post_transformation, columns= final_column_names)

print(final_df)
