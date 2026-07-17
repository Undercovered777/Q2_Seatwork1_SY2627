# 2nd Quarter Seatwork 1
from pyscript import display, document


def get_nickname(e):
    document.getElementById('output1').innerHTML = " "
    country_nicknames = {
        "philippines": "The Pearl of the Orient Seas",
        "indonesia": "The Emerald of the Equator",
        "thailand": "The Land of Smiles",
        "vietnam": "The Land of the Ascending Dragon",
        "malaysia": "The Land of Truly Asia",
        "singapore": "The Lion City",
        "myanmar": "The Golden Land",
        "cambodia": "The Kingdom of Wonder",
        "laos": "The Land of a Million Elephants",
        "brunei": "The Abode of Peace",
        "timor-leste": "The Land of the Rising Sun in South East Asia"
    }

    country = document.getElementById('country_input').value.lower()

    # Look up the nickname using .get(), with a default message if not found
    nickname = country_nicknames.get(country, "Sorry, I don't have a nickname for that country.")

    display(f"Nickname: {nickname}", target='output1')