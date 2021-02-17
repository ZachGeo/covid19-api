from api import ma

class CovidGreeceSchema(ma.Schema):
    class Meta:
        fields = ('country', 'date', 'new_cases', 'new_tests', 
            'new_deaths', 'new_vaccinations')

class SumCovidGreeceSchema(ma.Schema):
    class Meta:
        fields = ('country', 'last_updated_date', 'total_cases', 
            'total_deaths', 'people_fully_vaccinated', 'population')

class SumCovidWorldSchema(ma.Schema):
    class Meta:
        fields = ('country', 'last_updated_date', 'total_cases', 
            'total_deaths', 'people_fully_vaccinated', 'population')

class SumCovidCountrySchema(ma.Schema):
    class Meta:
        fields = ('country', 'last_updated_date', 'total_cases', 
            'total_deaths', 'people_fully_vaccinated', 'population')


covid_greece_schema = CovidGreeceSchema()
all_covid_greece_schema = CovidGreeceSchema(many=True)
sum_covid_greece_schema = SumCovidGreeceSchema()
sum_covid_world_schema = SumCovidWorldSchema()
sum_covid_country_schema = SumCovidCountrySchema()
sum_covid_all_countries_schema = SumCovidCountrySchema(many=True)
