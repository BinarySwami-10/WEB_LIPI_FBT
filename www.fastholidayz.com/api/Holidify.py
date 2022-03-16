from mxproxy import mx
import requests
import urllib

getparams = {
    "placeCode": "",
    "pageNum": 0,
    "latitude": 25.45,
    "longitude": 81.85,
    "userId": "",
    "userHash": "",
    "holidifyListFilter": {"categoryTags": "", "activityTags": "", "popularityTags": "", "numberOfDays": "2", "region": "NORTH-EAST", "holidifySortObject": {"sortCriterion": "RELEVANCE"}, "visaCategory": "", "budgetCategory": "", }
}
getparams = urllib.parse.urlencode(getparams)

url = 'https://www.holidify.com/web/ajaxWeb/getExploreContentV2.hdfy'
page = requests.get(url, params=getparams).text
print(page)
