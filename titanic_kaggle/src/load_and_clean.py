from dagster import In, Out, op
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
from sklearn.model_selection import cross_val_score, StratifiedKFold, train_test_split, GridSearchCV


@op(out={"train_df": Out(), "test_df": Out(), "gender_df": Out()})
def load_data():
    train_df = pd.read_csv('../data/train.csv')
    test_df = pd.read_csv('../data/test.csv')
    gender_df = pd.read_csv('../data/gender_submission.csv')

    return train_df, test_df, gender_df

@op(ins={"train_df": In(pd.DataFrame)})
def group_by_class(train_df) -> pd.DataFrame:

    return train_df.groupby(['Pclass'], as_index=False)['Survived'].mean()

@op(ins={"train_df": In(pd.DataFrame)})
def group_by_sex(train_df) -> pd.DataFrame:
    return train_df.groupby(['Sex'], as_index=False)['Survived'].mean()

@op(ins={"train_df": In(pd.DataFrame)})
def group_by_sibsp(train_df) -> pd.DataFrame:
    return train_df.groupby(['SibSp'], as_index=False)['Survived'].mean()