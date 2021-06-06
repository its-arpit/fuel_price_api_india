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
    return '''<h1 style="text-align: center;">&nbsp;Fuel API</h1>
<p style="text-align: center;">An API for the latest Diesel prices in India for all the major towns and cities. <br />It is a Flask-based lean app.</p>
<table style="border-collapse: collapse; width: 59.62078651685394%; height: 50px; margin-left: auto; margin-right: auto;" border="1">
<tbody>
<tr>
<td style="width: 9.778641701047292%;">1</td>
<td style="width: 21.354317100450842%;">List of States</td>
<td style="width: 68.86704119850188%;">/states</td>
</tr>
<tr>
<td style="width: 9.778641701047292%;">2</td>
<td style="width: 21.354317100450842%;">List of Districts</td>
<td style="width: 68.86704119850188%;">/state/district?state=Your%20State</td>
</tr>
<tr>
<td style="width: 9.778641701047292%;">3</td>
<td style="width: 21.354317100450842%;">Diesel Price for District</td>
<td style="width: 68.86704119850188%;">/price/state/district?state=Your%20State&amp;district=Your%20District</td>
</tr>
</tbody>
</table>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><a href="https://github.com/its-arpit/fuel_price_api_india/">Github</a>&nbsp;</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">Made With ❤️&nbsp;by <a href="https://www.linkedin.com/in/aarpitk/">Arpit</a></p>'''


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


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404
