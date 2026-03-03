from services.services import DatasetService


class EmissionsRepository:

    def __init__(self, source: str, use_url: bool = True):
        self.dataset_service = DatasetService(source, use_url)

    def get_all_emissions(self):
        return self.dataset_service.get_emissions_data()

    def get_emissions_by_keywords(self, keywords):
        return self.dataset_service.get_emissions_data(keywords)

    def get_country_emissions(self, country_column: str, country_name: str, keywords=None):
        data = self.dataset_service.get_emissions_data(keywords)

        if country_column in data.columns:
            return data[data[country_column] == country_name]

        return None
