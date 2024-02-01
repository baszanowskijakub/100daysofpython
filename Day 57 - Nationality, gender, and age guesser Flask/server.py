from flask import Flask, render_template
import pycountry
import requests
import random
import datetime
import json

app = Flask(__name__)

def get_country_name(country_code):
    try:
        country = pycountry.countries.get(alpha_2=country_code)
        if country:
            return country.name
        else:
            return "Sorry, I don't know that country"
    except Exception as e:
        return f"Error: {e}"


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    date = datetime.date
    year = date.today().year
    name = "Jakub Baszanowski"
    return render_template("index.html", num=random_number, CURRENT_YEAR=year, YOUR_NAME=name)


@app.route('/guess/<name>')
def guess(name):
    name = name.title()
    age_url = requests.get(f"https://api.agify.io?name={name}")
    age_data = json.loads(age_url.text)
    age = age_data["age"]
    gender_url = requests.get(f"https://api.genderize.io/?name={name}")
    gender_data = json.loads(gender_url.text)
    gender = gender_data["gender"]
    nationality_url = requests.get(f"https://api.nationalize.io/?name={name}")
    nationality_data = json.loads(nationality_url.text)
    nationality1_code = nationality_data["country"][0]["country_id"]
    nationality2_code = nationality_data["country"][1]["country_id"]
    nationality1 = get_country_name(nationality1_code)
    nationality2 = get_country_name(nationality2_code)
    return render_template("guess.html", person_name=name, person_age=age,
                           person_gender=gender, person_nationality1=nationality1,
                           person_nationality2=nationality2)


if __name__ == "__main__":
    app.run(debug=True)