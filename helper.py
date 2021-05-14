# credit: https://www.kaggle.com/jankoch/scikit-learn-pipelines-and-pandas
from sklearn.base               import TransformerMixin, BaseEstimator, clone

class DropAllZeroTrainColumnsTransformer(BaseEstimator, TransformerMixin):
    """ A DataFrame transformer that provides dropping all-zero columns
    """

    def transform(self, X, **transformparams):
        """ Drops certain all-zero columns of X

        Parameters
        ----------
        X : DataFrame

        Returns
        ----------
        trans : DataFrame
        """

        trans = X.drop(self.cols_, axis=1).copy()
        return trans

    def fit(self, X, y=None, **fitparams):
        """ Determines the all-zero columns of X

        Parameters
        ----------
        X : DataFrame
        y : not used

        Returns
        ----------
        self : object
        """

        self.cols_ = X.columns[(X == 0).all()]
        return self