import requests

states_p = {'Chandigarh': 'https://www.goodreturns.in/petrol-price-in-chandigarh-s6.html',
            'Andaman & Nicobar': 'https://www.goodreturns.in/petrol-price-in-andaman-nicobar-s1.html',
            'Andhra Pradesh': 'https://www.goodreturns.in/petrol-price-in-andhra-pradesh-s2.html',
            'Arunachal Pradesh': 'https://www.goodreturns.in/petrol-price-in-arunachal-pradesh-s3.html',
            'Assam': 'https://www.goodreturns.in/petrol-price-in-assam-s4.html',
            'Bihar': 'https://www.goodreturns.in/petrol-price-in-bihar-s5.html',
            'Chhatisgarh': 'https://www.goodreturns.in/petrol-price-in-chhatisgarh-s7.html',
            'Dadra Nagarhaveli': 'https://www.goodreturns.in/petrol-price-in-dadra-nagarhaveli-s8.html',
            'Daman & Diu': 'https://www.goodreturns.in/petrol-price-in-daman-diu-s9.html',
            'Delhi': 'https://www.goodreturns.in/petrol-price-in-delhi-s10.html',
            'Goa': 'https://www.goodreturns.in/petrol-price-in-goa-s11.html',
            'Gujarat': 'https://www.goodreturns.in/petrol-price-in-gujarat-s12.html',
            'Haryana': 'https://www.goodreturns.in/petrol-price-in-haryana-s13.html',
            'Himachal Pradesh': 'https://www.goodreturns.in/petrol-price-in-himachal-pradesh-s14.html',
            'Jammu & Kashmir': 'https://www.goodreturns.in/petrol-price-in-jammu-kashmir-s15.html',
            'Jharkhand': 'https://www.goodreturns.in/petrol-price-in-jharkhand-s16.html',
            'Karnataka': 'https://www.goodreturns.in/petrol-price-in-karnataka-s17.html',
            'Kerala': 'https://www.goodreturns.in/petrol-price-in-kerala-s18.html',
            'Madhya Pradesh': 'https://www.goodreturns.in/petrol-price-in-madhya-pradesh-s19.html',
            'Maharashtra': 'https://www.goodreturns.in/petrol-price-in-maharashtra-s20.html',
            'Manipur': 'https://www.goodreturns.in/petrol-price-in-manipur-s21.html',
            'Meghalaya': 'https://www.goodreturns.in/petrol-price-in-meghalaya-s22.html',
            'Mizoram': 'https://www.goodreturns.in/petrol-price-in-mizoram-s23.html',
            'Nagaland': 'https://www.goodreturns.in/petrol-price-in-nagaland-s24.html',
            'Odisha': 'https://www.goodreturns.in/petrol-price-in-odisha-s25.html',
            'Pondicherry': 'https://www.goodreturns.in/petrol-price-in-pondicherry-s26.html',
            'Punjab': 'https://www.goodreturns.in/petrol-price-in-punjab-s27.html',
            'Rajasthan': 'https://www.goodreturns.in/petrol-price-in-rajasthan-s28.html',
            'Sikkim': 'https://www.goodreturns.in/petrol-price-in-sikkim-s29.html',
            'Tamil Nadu': 'https://www.goodreturns.in/petrol-price-in-tamil-nadu-s30.html',
            'Telangana': 'https://www.goodreturns.in/petrol-price-in-telangana-s31.html',
            'Tripura': 'https://www.goodreturns.in/petrol-price-in-tripura-s32.html',
            'Uttar Pradesh': 'https://www.goodreturns.in/petrol-price-in-uttar-pradesh-s33.html',
            'Uttarakhand': 'https://www.goodreturns.in/petrol-price-in-uttarakhand-s34.html',
            'West Bengal': 'https://www.goodreturns.in/petrol-price-in-west-bengal-s35.html'}

states_d = {'Chandigarh': 'https://www.goodreturns.in/diesel-price-in-chandigarh-s6.html',
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
        pagecontent = page.text
        return pagecontent
    except:
        return "Try after some time"


def get_district_url(state):
    try:
        url = states_p[state]
    except:
        return "Enter correct state"
    return url


def get_district_url_with_fuel(state, fuel):
    if fuel == "petrol":
        url = states_p[state]
    elif fuel == 'diesel':
        url = states_d[state]
    else:
        return "Please put correct fuel spelling"
    return url
