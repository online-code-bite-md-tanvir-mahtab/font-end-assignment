from flask import Flask, render_template, redirect, request, json, jsonify




app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/bookticket', methods=['POST','GET'])
def book():
    # this condition will check wheather i am sending any data from the filled form
    # and send them as a post request or not 
    if request.method == "POST":
        # this three line will do is first read the data from the file
        # then it will be loaded as json formated and will hold the specific data and store in the json_data variable
        with open('data/LHR_CDG_ADT1_TYPE_1.txt', mode='r') as file:
            json_data = json.load(file)['flightOffer']
            # now this code will connect the python to back end to the html code and pass the json data in the flightdata parameter.
            return render_template('bookticket.html', flightdata= json_data)
    else:
        # this code will only going to pass empty data.
        return render_template('bookticket.html', flightdata= [])
    

if __name__ == '__main__':
    app.run(debug=True)