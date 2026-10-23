from city_country_function import city_country

def test_city_country_format():
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'

def test_city_country_with_population():
    result = city_country('jakarta', 'INDOnesia', 100000000)
    assert result == 'Jakarta, Indonesia - population 100000000'
