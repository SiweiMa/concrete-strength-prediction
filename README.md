# Prediction of concrete strength by machine learning
*The repository is the final project in course MSDS 699. [Colab link](https://colab.research.google.com/drive/1KFYW6li0pEBU6IIQ9T00QcdbQjZy8Rjk?usp=sharing)* 

#### by Siwei Ma


# Summary

Concrete is the single most widely used man-made material in the world. Construction workers reply on the experiments to determine the strength of concrete. It would be ideal if we can predict the strength based on the information of raw materials. 

The classical statistical methods like linear or non-linear regression prove to be unsuitable to cope with the complexity of modern higher performance concrete [1]. Therefore, several machine learning algorithms, LASSO, random forest regressor, extra tree regressor, were used to predict the concrete strength. 

By using randomized search cross validation, random forest regressor performs the best regarding the evaluation metrics of coefficient of variance. It gives coefficient of variance of 8.67%, which is within the acceptable range of coefficient of variation for 2 cylinder strengths, 9.0%, according to American Society for Testing and Materials (ASTM). The prediction by machine learning can serve as a good indicator for the strength of concrete.


# Data

The data of this project came from [this research paper](https://www.sciencedirect.com/science/article/pii/S0950061820339581) [2] generously shared by the authors.

# References
[1] Henri Van Damme, Concrete material science: Past, present, and future innovations, Cement and Concrete Research, Volume 112, 2018, Pages 5-24, ISSN 0008-8846

[2] Tianyu Xie, M.S. Mohamad Ali, Mohamed Elchalakani, Phillip Visintin, Modelling fresh and hardened properties of self-compacting concrete containing supplementary cementitious materials using reactive moduli, Construction and Building Materials, Volume 272, 2021, 121954, ISSN 0950-0618
