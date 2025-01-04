
class NaiveBayes:
    def __init__(self):
        pass
    
    def get_classes_probability(self, X):
        # Convert DataFrame row to dictionary if needed
        if not isinstance(X, dict):
            X = X.iloc[0].to_dict()
        
        classes_probabilities = {}
        for class_val in self.probability_target.keys():
            prob = self.probability_target[class_val]
            
            for feature, value in X.items():
                if feature in self.probability_features and \
                   value in self.probability_features[feature] and \
                   class_val in self.probability_features[feature][value]:
                    prob *= self.probability_features[feature][value][class_val]
            
            classes_probabilities[class_val] = prob
        
        return classes_probabilities
    
    def fit(self, X_train, y_train):
        self.probability_features = {}
        self.probability_target = {}
        target_variable = "target"
        df = X_train.copy()
        df[target_variable] = y_train
        
        # Calculate target probabilities
        yes_samples = len(df[df[target_variable] == "yes"])
        total_samples = len(df)
        
        self.probability_target = {
            "yes": yes_samples / total_samples,
            "no": (total_samples - yes_samples) / total_samples
        }
        
        # Calculate feature probabilities
        for feature in X_train.columns:
            self.probability_features[feature] = {}
            
            # Get unique values for this feature
            feature_values = df[feature].unique()
            
            for value in feature_values:
                self.probability_features[feature][value] = {}
                
                for class_val in ["yes", "no"]:
                    # Get data for current class
                    class_data = df[df[target_variable] == class_val]
                    feature_class_data = class_data[class_data[feature] == value]
                    
                    # Calculate conditional probability P(feature|class)
                    class_count = len(class_data)
                    feature_count = len(feature_class_data)
                    
                    if class_count > 0:
                        prob = feature_count / class_count
                    else:
                        prob = 0
                        
                    self.probability_features[feature][value][class_val] = prob
    
    def predict(self, X_test):
        pass
