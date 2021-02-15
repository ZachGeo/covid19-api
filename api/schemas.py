from api import ma

class CovidGreeceSchema(ma.Schema):
    class Meta:
        fields = (
            'country', 'date', 'cases', 'tests', 'deaths', 'vaccinations')

class SumCovidGreeceSchema(ma.Schema):
    class Meta:
        fields = ('country', 'sum_greece_cases', 'sum_greece_deaths', 
            'sum_greece_recovered', 'sum_greece_vaccinations', 
            'last_modified_date')

class SumCovidWorldSchema(ma.Schema):
    class Meta:
        fields = ('label', 'sum_world_cases', 'sum_world_deaths', 
            'sum_world_recovered', 'sum_world_vaccinations', 
            'last_date_modified')

class SumCovidCountrySchema(ma.Schema):
    class Meta:
        fields = ('country', 'sum_country_cases', 'sum_contry_deaths', 
            'sum_contry_recovered', 'sum_contry_vaccinations',
            'last_date_modified')


covid_greece_schema = CovidGreeceSchema()
all_covid_greece_schema = CovidGreeceSchema(many=True)
sum_covid_greece_schema = SumCovidGreeceSchema()
sum_covid_world_schema = SumCovidWorldSchema()
sum_covid_country_schema = SumCovidCountrySchema()
sum_covid_all_countries_schema = SumCovidCountrySchema(many=True)
