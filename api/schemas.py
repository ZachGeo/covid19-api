from api import ma

class CovidGreeceSchema(ma.Schema):
    class Meta:
        fields = ('date', 'cases', 'tests', 'deaths', 'vaccinations')

class SumCovidGreeceSchema(ma.Schema):
    class Meta:
        fields = ('sum_greece_cases', 'sum_greece_tests', 'sum_greece_deaths', 
            'sum_greece_recovered', 'sum_greece_vaccinations')

class SumCovidWorldSchema(ma.Schema):
    class Meta:
        fields = ('sum_world_cases', 'sum_world_deaths', 
            'sum_world_recovered', 'sum_world_vaccinations')

class SumCovidUnitedStatesSchema(ma.Schema):
    class Meta:
        fields = ('sum_usa_cases', 'sum_usa_deaths', 
            'sum_usa_recovered', 'sum_usa_vaccinations')

class SumCovidChinaSchema(ma.Schema):
    class Meta:
        fields = ('sum_china_cases', 'sum_china_deaths', 
            'sum_china_recovered', 'sum_china_vaccinations')

class SumCovidFranceSchema(ma.Schema):
    class Meta:
        fields = ('sum_france_cases', 'sum_france_deaths', 
            'sum_france_recovered', 'sum_france_vaccinations')

class SumCovidUnitedKingdomSchema(ma.Schema):
    class Meta:
        fields = ('sum_unitedkingdom_cases', 'sum_unitedkingdom_deaths', 
            'sum_unitedkingdom_recovered', 'sum_unitedkingdom_vaccinations')

class SumCovidGermanySchema(ma.Schema):
    class Meta:
        fields = ('sum_germany_cases', 'sum_germany_deaths', 
            'sum_germany_recovered', 'sum_germany_vaccinations')

class SumCovidItalySchema(ma.Schema):
    class Meta:
        fields = ('sum_italy_cases', 'sum_italy_deaths', 
            'sum_italy_recovered', 'sum_italy_vaccinations')

class SumCovidRussiaSchema(ma.Schema):
    class Meta:
        fields = ('sum_russia_cases', 'sum_russia_deaths', 
            'sum_russia_recovered', 'sum_russia_vaccinations')

class SumCovidJapanSchema(ma.Schema):
    class Meta:
        fields = ('sum_japan_cases', 'sum_japan_deaths', 
            'sum_japan_recovered', 'sum_japan_vaccinations')

class SumCovidCanadaSchema(ma.Schema):
    class Meta:
        fields = ('sum_canada_cases', 'sum_canada_deaths', 
            'sum_canada_recovered', 'sum_canada_vaccinations')

covid_greece_schema = CovidGreeceSchema()
all_covid_greece_schema = CovidGreeceSchema(many=True)
sum_covid_greece_schema = SumCovidGreeceSchema()
sum_covid_world_schema = SumCovidWorldSchema()
sum_covid_usa_schema = SumCovidUnitedStatesSchema()
sum_covid_china_schema = SumCovidChinaSchema()
sum_covid_france_schema = SumCovidFranceSchema()
sum_covid_uk_schema = SumCovidUnitedKingdomSchema()
sum_covid_germany_schema = SumCovidGermanySchema()
sum_covid_italy_schema = SumCovidItalySchema()
sum_covid_russia_schema = SumCovidRussiaSchema()
sum_covid_japan_schema = SumCovidJapanSchema()
sum_covid_canada_schema = SumCovidCanadaSchema()
