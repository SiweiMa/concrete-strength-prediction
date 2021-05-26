import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image


st.sidebar.header("SCC Concrete Features")

def user_input_features():
    wb = st.sidebar.number_input('Effective water-to-binder ratio', 0.00, 1.00, value=0.320, format="%.3f")
    bf = st.sidebar.number_input('Binder-to-fly ash ratio', 0.3, 5.0, value=0.768, format="%.3f")

    coarse_aggregate = st.sidebar.number_input('Coarse aggregate content (kg/m3)', 400.0, 1000.0, value=920.0, format="%.1f")
    fine_aggregate = st.sidebar.number_input('Fine aggregate (kg/m3)', 210.0, 1100.0, value=716.0, format="%.1f")

    surface_area = st.sidebar.number_input('Overall specific surface area (m2/kg) * corresponding mix proportion (kg/m3)', 72500, 3000000, value=842792)
    superplasticizer = st.sidebar.number_input('Superplasticizer (kg/m3)', 0.0, 30.0, value=10.8, format="%.3f")
    water = st.sidebar.number_input('Water (kg/m3)', 90.0, 800.0, value=176.0, format="%.1f") # 168.0

    SO3 = st.sidebar.number_input('SO3 content (kg/m3)', 0.0, 2700.0, value=923.5, format="%.1f")
    CaO = st.sidebar.number_input('CaO content (kg/m3)', 700.0, 50000.0, value=26306.0, format="%.1f")

    data = {
            'Fine aggregate': fine_aggregate,
            'Superplasticizer': superplasticizer,
            'CaO': CaO,
            'Water': water,
            'Specific surface area (m2/kg)': surface_area,
            'b/FA': bf,
            'SO3': SO3,
            'Coarse aggregate': coarse_aggregate,
            'w/b (eff)': wb
            }

    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

#Load in model
filename = 'final_model_sel.sav'
with open(filename, 'rb') as f:
    model = pickle.load(f)

# Apply model to make predictions
prediction = model.predict(input_df)
# st.markdown("# Predicting Concrete Strength")
# st.markdown("#### by [Siwei Ma](https://www.linkedin.com/in/siwei-ma-28345856/)")
st.markdown(f"## Predicted 28-d compressive strength: **{prediction[0]:.2f}** MPa")
st.markdown("### Executive Summary")
st.markdown("""
Concrete is the single most widely used man-made material in the world. Construction workers reply on 
the experiments to determine the strength of concrete. The app presents an attempt to predict the strength based on the 
information of raw materials by machine learning methods. 
""" )

st.markdown("### Analysis Process")
st.markdown("#### Data Cleaning")
st.markdown("""
The data of this project was collected from [academic research papers](
https://www.journals.elsevier.com/construction-and-building-materials) and re-arranged to tidy format.
""")
st.markdown("#### Feature Engineering")
st.markdown("""
Create features related to chemical composition and specific surface area. Impute the missing values with mean.
Standardize the data for Lasso and Ridge regression. 
""")
st.markdown("#### Modeling")
st.markdown("""
The classical statistical methods like linear or non-linear regression prove to be unsuitable to cope with the 
complexity of modern higher performance concrete [1]. Therefore, several machine learning algorithms were used to 
predict the concrete strength. 

By using randomized search cross validation, extra tree regressor outperformed the other algorithms including 
linear (Lasso, Ridge), bagging (random forest, extra tree), boosting (xgboost, lightgbm) regressors 
in terms of the RMSE score.
""")
st.image(Image.open('images/model_comparison.png'), width=500)
st.markdown(">Figure 1. Comparison between models.")

st.markdown("#### Feature importance")
st.markdown("""
Select features based on permutation importance. If two or more features are codependent, 
the permutation importance would give unexpected results. 
For example, permuting a duplicated column would still allow prediction to be half supported by the other identical column. 
As shown in the heatmap of Spearman rank-order correlations (Fig 2. zoom-in maybe needed to see details), 
some features are correlated and could be clustered as a group. 
Thus, we performed hierarchical clustering on the Spearman rank-order correlations and 
only kept a single feature from each cluster to solve collinearity.
""")
st.image(Image.open('images/spearmanr.png'), width=500)
st.markdown(">Figure 2. Heatmap of Spearman rank-order correlations.")

st.markdown("""
It is also useful to test the significance of the feature's importance. As shown below, the bar chart in blue shows 
a null hypothesis distribution for comparison with the permutation importance in red. It is likely that a significant 
feature would be different from the null hypothesis distribution, thus we will drop the non-significant features.
""")
st.image(Image.open('images/ptest.png'), width=500)
st.markdown(">Figure 3 The empirical p-test on feature importance.")

st.markdown("""
Furthermore, we also keep decreasing the number of features to 9 based on domain knowledge. 
The ranking of permutation importance of the selected features is shown below.
""")
st.image(Image.open('images/feature_importance.png'), width=500)
st.markdown(">Figure 4. Feature importance.")


st.markdown("#### Prediction")
st.markdown("""
After filtering out the correlated features, we apply the model to the hold-out test data to examine the performance. 
The model gives reasonable prediction ranging from 20-90 MPa. **It gives RMSE of 7.81 MPa**. 
""")
st.image(Image.open('images/prediction.png'), width=450)
st.markdown(">Figure 4. The strength prediction by extra tree regressor.")

st.markdown("#### Limitation")
st.markdown("""
To improve the ease of use for the web app, we dramatically decreased the number of features from 153 to 9, which 
moderately sacrifice the accuracy of the model. The RMSE increased from 6.49 to 7.81 MPa. 

The data used in this project is from academic publications, which could be quite possible that 
the research work cannot represent the construction work in reality. We cannot ignore the risk of violating the 
fundamental assumption in standard supervised learning setting which assumes both the training data and the test data
 are drawn independently from identical distribution. 
 Collecting larger data, especially the data from site construction, to mitigate this concern would be my future work.
""")


st.markdown("#### References")
st.markdown("""[1] Henri Van Damme, Concrete material science: Past, present, and future innovations, Cement and 
Concrete Research, Volume 112, 2018, Pages 5-24, ISSN 0008-8846 

[2] Tianyu Xie, M.S. Mohamad Ali, 
Mohamed Elchalakani, Phillip Visintin, Modelling fresh and hardened properties of self-compacting concrete containing 
supplementary cementitious materials using reactive moduli, Construction and Building Materials, Volume 272, 2021, 
121954, ISSN 0950-0618 
""")

