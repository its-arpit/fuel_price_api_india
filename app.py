import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask import request, jsonify

app = Flask(__name__)
states = {'Chandigarh': 'https://www.goodreturns.in/diesel-price-in-chandigarh-s6.html',
          'Andaman & Nicobar': 'https://www.goodreturns.in/diesel-price-in-andaman-nicobar-s1.html',
          'Andhra Pradesh': 'https://www.goodreturns.in/diesel-price-in-andhra-pradesh-s2.html',
          'Arunachal Pradesh': 'https://www.goodreturns.in/diesel-price-in-arunachal-pradesh-s3.html',
          'Assam': 'https://www.goodreturns.in/diesel-price-in-assam-s4.html',
          'Bihar': 'https://www.goodreturns.in/diesel-price-in-bihar-s5.html',
          'Chhatisgarh': 'https://www.goodreturns.in/diesel-price-in-chhatisgarh-s7.html',
          'Dadra Nagarhaveli': 'https://www.goodreturns.in/diesel-price-in-dadra-nagarhaveli-s8.html',
          'Daman & Diu': 'https://www.goodreturns.in/diesel-price-in-daman-diu-s9.html',
          'Delhi': 'https://www.goodreturns.in/diesel-price-in-delhi-s10.html',
          'Goa': 'https://www.goodreturns.in/diesel-price-in-goa-s11.html',
          'Gujarat': 'https://www.goodreturns.in/diesel-price-in-gujarat-s12.html',
          'Haryana': 'https://www.goodreturns.in/diesel-price-in-haryana-s13.html',
          'Himachal Pradesh': 'https://www.goodreturns.in/diesel-price-in-himachal-pradesh-s14.html',
          'Jammu & Kashmir': 'https://www.goodreturns.in/diesel-price-in-jammu-kashmir-s15.html',
          'Jharkhand': 'https://www.goodreturns.in/diesel-price-in-jharkhand-s16.html',
          'Karnataka': 'https://www.goodreturns.in/diesel-price-in-karnataka-s17.html',
          'Kerala': 'https://www.goodreturns.in/diesel-price-in-kerala-s18.html',
          'Madhya Pradesh': 'https://www.goodreturns.in/diesel-price-in-madhya-pradesh-s19.html',
          'Maharashtra': 'https://www.goodreturns.in/diesel-price-in-maharashtra-s20.html',
          'Manipur': 'https://www.goodreturns.in/diesel-price-in-manipur-s21.html',
          'Meghalaya': 'https://www.goodreturns.in/diesel-price-in-meghalaya-s22.html',
          'Mizoram': 'https://www.goodreturns.in/diesel-price-in-mizoram-s23.html',
          'Nagaland': 'https://www.goodreturns.in/diesel-price-in-nagaland-s24.html',
          'Odisha': 'https://www.goodreturns.in/diesel-price-in-odisha-s25.html',
          'Pondicherry': 'https://www.goodreturns.in/diesel-price-in-pondicherry-s26.html',
          'Punjab': 'https://www.goodreturns.in/diesel-price-in-punjab-s27.html',
          'Rajasthan': 'https://www.goodreturns.in/diesel-price-in-rajasthan-s28.html',
          'Sikkim': 'https://www.goodreturns.in/diesel-price-in-sikkim-s29.html',
          'Tamil Nadu': 'https://www.goodreturns.in/diesel-price-in-tamil-nadu-s30.html',
          'Telangana': 'https://www.goodreturns.in/diesel-price-in-telangana-s31.html',
          'Tripura': 'https://www.goodreturns.in/diesel-price-in-tripura-s32.html',
          'Uttar Pradesh': 'https://www.goodreturns.in/diesel-price-in-uttar-pradesh-s33.html',
          'Uttarakhand': 'https://www.goodreturns.in/diesel-price-in-uttarakhand-s34.html',
          'West Bengal': 'https://www.goodreturns.in/diesel-price-in-west-bengal-s35.html'}


def getHtmlData(url):
    try:
        page = requests.get(url)
        pagetext = page.text
        return pagetext
    except:
        return "Try after some time"


def get_district_url(state):
    try:
        url = states[state]
        return url
    except:
        return "Please enter correct spelling"


@app.route('/', methods=['GET'])
def hello_world():
    return '''<h1>Welcome In Fuel API</h1>
                <h3>For State List: "/states"</h3>
                <h3>For District List: "/state/district?state=Kerala"</h3>
                <h3>For Price: "/price/state/district/?state=Kerala&district=Thrissur"</h3>
                <p> Example: "/price/state/district/?state=Delhi&district=South%20Delhi"</p>'''


@app.route('/states', methods=['GET'])
def api_states():
    state = {}
    for key in states:
        state[key] = key
    return jsonify(state)


@app.route('/state/district', methods=['GET'])
def get_district_list():
    #pdb.set_trace()
    if 'state' in request.args:
        state = str(request.args['state'])
    else:
        return "Error: No state field provided. Please specify a state."
    district = {}
    url = get_district_url(state)
    print(url)
    pagetext = getHtmlData(url)
    soup = BeautifulSoup(pagetext, 'html.parser')
    for row in soup.find_all('tr'):
        for col in row.find_all('td'):
            if col.a in col:
                district[col.text] = col.text
    return jsonify(district)

@app.route('/price/state/district/', methods=['GET'])
def get_fuel_price():
    #pdb.set_trace()
    if 'state' in request.args:
        state = str(request.args['state'])
    else:
        return "Error: No state field provided. Please specify a state."
    if 'district' in request.args:
        district = str(request.args['district'])
    else:
        return "Error: No district field provided. Please specify a district."
    fuel_price_list = []
    url = get_district_url(state)
    print(url)
    pagetext = getHtmlData(url)
    soup = BeautifulSoup(pagetext, 'html.parser')
    for row in soup.find_all('tr'):
        if district in row.text:
            for col in row.find_all('td'):
                try:
                    fuel_price = (float(col.text.split(' ')[1]))
                    print(fuel_price)
                    fuel_price_list.append(fuel_price)
                except:
                      pass
    return str(fuel_price_list[0])


if __name__ == '__main__':
    app.run()
