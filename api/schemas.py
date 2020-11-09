from api import ma

class CovidSchema(ma.Schema):
    class Meta:
        fields = ('date', 'cases', 'deaths')

class SumCovidSchema(ma.Schema):
    class Meta:
        fields = ('sum_cases', 'sum_deaths', 'sum_recovered')

class WorldSumCovidSchema(ma.Schema):
    class Meta:
        fields = ('sum_world_cases', 'sum_world_deaths', 'sum_world_recovered')

covid_schema = CovidSchema()
covids_schema = CovidSchema(many=True)
sum_covid_schema = SumCovidSchema()
sum_world_schema = WorldSumCovidSchema()
