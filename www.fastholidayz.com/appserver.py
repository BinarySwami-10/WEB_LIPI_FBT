from flask import *  
from  easemytrip_api import main_api

app = Flask(__name__)

@app.route('/api/v1/flightSearch') 
def get_flights():
   resp=main_api.get_flights()
   return jsonify(resp)


   

if __name__ == '__main__':  
   app.run(debug = True)  

