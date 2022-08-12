# local imports
from src.pages.home import home_radios

# CURRENTLY FAILS BECAUSE OF dash.register_page
def test_home_radio_callback():
    value = 5
    output = home_radios(value)
    assert output == f'You have selected {value}'
