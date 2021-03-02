import pickle

class WineQuality (object):
    def __init__(self):
        self.free_sulfur_dioxide = pickle.load(open('/Users/rauferibeiro/DataScience/Projetos/Estudos/sejaumdatascientist/deploy/free_sulfur_scale.pkl','rb'))
        self.total_sulfur_dioxide = pickle.load(open('/Users/rauferibeiro/DataScience/Projetos/Estudos/sejaumdatascientist/deploy/total_sulfur_scale.pkl','rb'))
        
    def data_preparation(self, df):
        # rescale free sulfur
        df['free sulfur dioxide'] = self.free_sulfur_dioxide.transform(df[['free sulfur dioxide']].values)
        
        # rescale total sulfur
        df['total sulfur dioxide'] = self.total_sulfur_dioxide.transform(df[['total sulfur dioxide']].values)

        return df