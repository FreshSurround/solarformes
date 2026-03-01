import pandas as pd
import requests
from io import StringIO


class DatasetService:

    def __init__(self, source: str, use_url: bool):
        self.source = source      # URL o path local
        self.use_url = use_url
        self.data = None

    def load_data(self):
        if self.use_url:
            response = requests.get(self.source)
            response.raise_for_status()
            self.data = pd.read_csv(StringIO(response.text))
        else:
            self.data = pd.read_csv(self.source)

    def filter_emissions(self, keywords=None):
        if self.data is None:
            self.load_data()

        if keywords:
            cols = [col for col in self.data.columns
                    if any(k.lower() in col.lower() for k in keywords)]
            return self.data[cols]

        return self.data

    def get_emissions_data(self, keywords=None):
        self.load_data()
        return self.filter_emissions(keywords)
