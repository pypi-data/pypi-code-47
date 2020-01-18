import numpy as np
import pandas as pd

class ResponseCoding:
    '''
        Takes One Single column as Input and
        Returns Response Coded Single Column Vector.

        The categories of the feature do not need to be Label Encoded.
        All the values will be considered to be String.

        Performs Feature wise Response Coding.

        Example Code
        ------------
        Scenario: 
                 Binary classification. Positive class is labelled `1` and 
                 Negative class is labelled `0`. Transformer will output 
                 one column for each target class. The ouput will be ordered
                 Lexicographically. Thus the columns will correspond to the 
                 classes `0` and `1` respectively.

        Code:
                vectorizer = ResponseCoding()

                # For training data
                categories_response_coded = vectorizer.fit_transform(X_train.feature_column, y_train])
                
                # Get for class = 1 (Accepted)
                categories_train = categories_response_coded[1]

                                            OR

                vectorizer.fit(X_train.feature_column, y_train)
                categories_response_coded = vectorizer.transform(X_train.feature_column)
                categories_train = categories_response_coded[1]                                         
                
                
                # For testing data
                # Get for class = 1 (Accepted)
                categories_test = vectorizer.transform(X_test.feature_column)[1]
    '''
    def __init__(self):

        # list of Unique categories
        # Sorted Lexicographically
        # initialised in fit()
        self.categories = []#sorted(set(self.X))

        # list of unique target Labels
        # Sorted Lexicographically
        # initialised in fit()
        self.labels = []#sorted(set(self.y))
        
        # setup dictionary to hold probailities
        # initialised in fit()
        # {category_1: {target_1:value, ..., target_3:value},..., category_n: {...}}
        self.proba_ = dict()


    def only_one_col(self, data):
            '''
                Checks if only one Column provided as input.
                Response Coding is performed column wise.
            '''
            # Numpy array is Homogenous
            # Hence all the data will be 
            # converted to String.
            data = np.array(data)

            # In case of Multiple Columns
            # Numpy array will be Multi dimensional
            if len(data.shape) > 1:
                return False
            else:
                return True


    def is_iterable(self, X, column='Category'):
        #TODO
        '''
            Parameter
            ---------
            column = 'category' or 'target'
        '''
        try:
            iter(X)
            return True
        except TypeError:
            raise TypeError(f'''An iterable is needed for {column} column.
                                Non - iterable provided''')                                 


    def fit(self, X, y):
        '''
            Calculates Response Rate per category 
            for each Label.
        

            Return
            -------
            self
        '''

        #### Checks ####
        self.is_iterable(X), self.is_iterable(y, column='Target')

        # If more than one column
        # raise error
        if not self.only_one_col(X):
            raise ValueError('''Only One Feature Can be processed.
                             More than one Column provided.''')
        
        # If < 2 class label
        # raise error

        if len(set(y)) < 2:
            raise ValueError(f'''Atleast two Unique value expected for label,
                                 {len(set(self.y))} provided.''')
        ### END of Checks ####

        self.categories = sorted(set(X))
        self.labels = sorted(set(y))

        df = pd.DataFrame(data=np.column_stack([X, y]), columns=['X','y'])
        
        # dictionary to hold count per category
        denominator = dict()

        numerator = dict()

        # Populate the Numerator and Denominator dictionaries
        for category in self.categories:
            
            # get data for each category
            cat_data = df[df.X == category]
            
            # Count of All data for each category
            denominator[category] = cat_data.shape[0]
            
            # initialise the dictionary entry
            # needed to add 2nd dictinary nesting level
            numerator[category] = dict()

            for target in self.labels:
                # count of data points for each label of each category
                cat_target_count = cat_data[cat_data.y == target].shape[0]
                numerator[category][target] = cat_target_count


        ##### Calculate the Response Rate

        # key = category, value = #Points - all target
        for key, value in denominator.items():
             
            deno = value

            # initialise the dictionary entry
            # needed to add 2nd dictinary nesting level
            self.proba_[key] = dict()
            
            # k = target, v = count of each category per  target class
            for k,v in numerator.get(key).items():
                 self.proba_[key][k] = round(v/deno, 2)

        # Add the default value, incase of unseen Category
        self.proba_['default']=dict()
        for target in self.labels:
            # equal probability for each classes.
            self.proba_['default'][target] = round(1/len(self.labels), 2)

        return self  


    def transform(self, X, y=None):
        ''' 
            y: is not needed. Provided for Uniformity.
        '''
        #### Perform checks ####
        self.is_iterable(X)

        # If more than one column
        # raise error
        if not self.only_one_col(X):
            raise ValueError('''Only One Feature Can be processed.
                             More than one Column provided.''')
        
        #### End of Checks #### 

        # for each value of X create n lists
        # that contains reponse rate
        response_data = dict()
        response_data = {i:[] for i in self.labels}
        #print(self.labels, response_data)
        
        for index, category in enumerate(X):
                        
            for label in self.labels:
                #print(label)
                # check if category present in fit dictionary
                if not category in self.proba_.keys():
                    category = 'default'
                
                # Get response rate for each row
                # return data structure: {label_1: [],..., label_n: []}
                response_data[label].append(self.proba_[category][label])


        # (target_1_column, .., target_n_column)
        return tuple(response_data.values())


    def fit_transform(self, X, y):
           
        return self.fit(X, y).transform(X)
    