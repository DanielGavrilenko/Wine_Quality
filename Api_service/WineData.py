class WineData:
    """ process data for wine prediction model
{
"fixed_acidity":"8.3",
"volatile_acidity":"0.18",
"citric_acid":"0.3",
"residual_sugar":"1.1",
"chlorides":"0.033",
"free_sulfur_dioxide":"20",
"total_sulfur_dioxide":"57",
"density":"0.99109",
"pH":"3.02",
"sulphates":"0.51",
"alcohol":"11"
}
"""

    ATTRIBUTE_MAPPING = {
        'fixed_acidity': 'fixed_acidity',
        'volatile_acidity': 'volatile_acidity',
        'citric_acid': 'citric_acid',
        'residual_sugar': 'residual_sugar',
        'chlorides': 'chlorides',
        'free_sulfur_dioxide': 'free_sulfur_dioxide',
        'total_sulfur_dioxide': 'total_sulfur_dioxide',
        'density': 'density',
        'pH': 'pH',
        'sulphates': 'sulphates',
        'alcohol': 'alcohol'
    }

    def __init__(self, data: dict) -> None:
        # Initializes an instance of the WineData class.
        self._initialize_attributes(data)

    def _initialize_attributes(self, data: dict) -> None:
        # Private method to initialize attributes based on input data.
        for key, attribute in self.ATTRIBUTE_MAPPING.items():
            if key in data:
                setattr(self, attribute, float(data.get(key, 0.0)))
            else:
                raise Exception("error 400: attribute is not found")

    def get_2d_array(self) -> list:
        # Returns a 2D array representation of the wine data.
        n_features = len(self.ATTRIBUTE_MAPPING)
        array = [[0.0] * n_features for _ in range(2)]
        # Iterate through attributes and get their values using getattr
        for i, attr in enumerate(self.ATTRIBUTE_MAPPING):
            array[0][i] = getattr(self, attr)
        return array

    def get_attribute(self, attribute_name: str) -> float:
        # Returns the value of a specified attribute.
        return getattr(self, attribute_name, 0.0)

