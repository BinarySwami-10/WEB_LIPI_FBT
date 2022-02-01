import requests
import re
import urllib
from mxproxy import mx


class TBODATA:
	flightsearch = ""


def auto_encoder(d):
	string = "&".join([f"{k}={urllib.parse.quote_plus(str(v))}" for k, v in d.items()])
	return string


def get_tbo_routes():
	url = "https://m.travelboutiqueonline.com/FlightSearchResult.aspx"
	parsed_data = auto_encoder(TBODATA.flightsearch)
	print(parsed_data)
	# parsed_data="ReturnType=0&LoginType=Agent&origin=Delhi+%28DEL%29%2C+India&destination=Hyderabad+%28HYD%29%2C+India&departDate=31-Dec-2021&OutBoundTime=00%3A00%3A00&returnDate=31-Dec-2021&InBoundTime=00%3A00%3A00&hResultFareType=RegularFare&hIsSpecialFare=False&NoOfAdutls=1&NoOfChilds=0&NoOfInfants=0&CabinClass=0&GDSPrefferedAirlines=&PreferredCarrier=GDS&PreferredCarrier=FZ&PreferredCarrier=G9&PreferredCarrier=AK&PreferredCarrier=IX&PreferredCarrier=LB&PreferredCarrier=TR&PreferredCarrier=SG&PreferredCarrier=G8&PreferredCarrier=6E&PreferredCarrier=B3&PreferredCarrier=OP&PreferredCarrier=2T&PreferredCarrier=W5&PreferredCarrier=LV&PreferredCarrier=TZ&PreferredCarrier=ZO&PreferredCarrier=PY&PreferredCarrier=TBA&PreferredCarrier=XW&PreferredCarrier=OV&PreferredCarrier=J9&PreferredCarrier=OG&PreferredCarrier=S9&LCCPreferredCarrier=G8&LCCPreferredCarrier=6E&LCCPreferredCarrier=SG&GDSPreferredCarrier=AI&GDSPreferredCarrier=UK&GDSPreferredCarrier=9W&GDSPreferredCarrier=S2&searchType=0&OriginIsDomestic=true&DestinationIsDomestic=true&hTravelInfo=&hDeptdate=&hReturndate=&hAdult=&hChild=&hInfant=&hsearchToReturn=true&hSwitchToAirportWiseSearch=True"
	resp = requests.post(url, data=parsed_data,
	                     headers=mx.parse_raw_header('tboheaders.txt'))
	# print(resp.text)
	resultList = []
	for item in mx.make_soup(resp.text).select(".result_p"):
	respdict = {
            'code': item.find('code').text.replace("\n", ""),
            'timings': item.select_one('.duration_flight').text.replace("\n", "").replace("  ", ""),
            'pubPrice': float("".join(re.findall(r'(\d)+?', item.select_one('span.price').text)))/100,
            'offerPrice': float("".join(re.findall(r'(\d)+?', item.select_one('span.price').find_next_sibling().text)))/100,
            }
	# for k,v in respdict:
	# 	respdict[k]=respdict[k].r

	postProcessing = [
            respdict.update(
                {'markup': respdict['pubPrice']-respdict['offerPrice']}),
            ]

	resultList.append(respdict)

	resultList.sort(key=lambda x: x['pubPrice'])
	return mx.jdumps(resultList)


if __name__ == '__main__':
	r = auto_encoder(TBODATA.flightsearch)
	r = get_tbo_routes()
	print(r)
