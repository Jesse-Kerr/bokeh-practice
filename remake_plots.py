from bokeh.plotting import figure, output_file, show
import pandas as pd
import scipy.stats as scs
from sklearn import datasets

#Plot1: get data from probability_spearman_pair.ipynb
study = pd.read_csv('admissions_with_study_hrs_and_sports.csv')
x, y = study.hrs_studied, study.gpa

#Bokeh section #1
output_file('probability.html')
p = figure(title = 'GPA vs. Hours', x_axis_label = 'hours_studied', y_axis_label = 'GPA')
p.scatter(x, y, legend = 'Relationships')
#show(p)

#Plot2: linear algebra EDA
iris_data = datasets.load_iris()
iris = pd.DataFrame(iris_data.data, columns= iris_data.feature_names)
x2 = iris['sepal width (cm)']
y2 = iris['sepal length (cm)']

output_file('linear.html')
p2 = figure(title = 'Sepal Width v. Length', x_axis_label = 'width (cm)', y_axis_label = 'length (cm)')
p2.scatter(x2, y2, legend = 'False')
show(p2, browser='firefox')