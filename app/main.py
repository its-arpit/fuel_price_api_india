import pdb

import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask import request, jsonify
from urls import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return '''<h1 style="text-align: center;">&nbsp;Fuel API</h1>
<p style="text-align: center;">An API for the latest Petrol and Diesel prices in India for all the major towns and cities. <br />It is a Flask-based lean app.</p>
<table style="border-collapse: collapse; width: 59.62078651685393%; height: 126px; margin-left: auto; margin-right: auto;" border="1">
<tbody>
<tr style="height: 36px;">
<td style="width: 9.778641701047292%; height: 36px;">1</td>
<td style="width: 21.354317100450842%; height: 36px;">List of States</td>
<td style="width: 68.86704119850188%; height: 36px;">/states</td>
</tr>
<tr style="height: 36px;">
<td style="width: 9.778641701047292%; height: 36px;">2</td>
<td style="width: 21.354317100450842%; height: 36px;">List of Districts</td>
<td style="width: 68.86704119850188%; height: 36px;">/state/district?state=Your%20State</td>
</tr>
<tr style="height: 36px;">
<td style="width: 9.778641701047292%; height: 36px;">3</td>
<td style="width: 21.354317100450842%; height: 36px;">Diesel Price for District</td>
<td style="width: 68.86704119850188%; height: 36px;">/price/state/district?state=Your%20State&amp;district=Your%20District&amp;fuel='diesel'</td>
</tr>
<tr style="height: 18px;">
<td style="width: 9.778641701047292%; height: 18px;">4</td>
<td style="width: 21.354317100450842%; height: 18px;">ChangeFuel</td>
<td style="width: 68.86704119850188%; height: 18px;">/price/state/district?state=Your%20State&amp;district=Your%20District&amp;fuel='petrol'</td>
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
    for key in states_p:
        state[key] = key
    return jsonify(state)


@app.route('/state/district', methods=['GET'])
def get_district_list():
    pdb.set_trace()
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
    pdb.set_trace()
    if 'state' in request.args:
        state = str(request.args['state'])
    else:
        return "Error: No state field provided. Please specify a state."
    if 'district' in request.args:
        district = str(request.args['district'])
    else:
        return "Error: No district field provided. Please specify a district."
    if "fuel" in request.args:
        fuel = str(request.args['fuel'])
    else:
        return "You did'nt enterd correct fuel parameter. It could be 'petrol' or 'diesel'."
    fuel_price_list = []
    url = get_district_url_with_fuel(state, fuel)
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
