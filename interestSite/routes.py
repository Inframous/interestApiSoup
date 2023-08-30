from interestSite import app 
from interestApiSoup import interestApi
from interestSite import helpers
from datetime import datetime


@app.route('/api/interest/boi')
def get_interest_boi():
    data = helpers.get_latest_entry()
    if helpers.validate_data(data["NextDecisionDate"]) == False:
        print("Updating data...")
        
        print("Data updated.")

    boi_interest = data['BoiInterest']
    next_date = data['NextDecisionDate']
    api_data = {
        "BoiInterest": boi_interest + "%",
        "NextDecisionDate": next_date
    }
    return api_data


@app.route('/api/interest/prime')
def get_interest_prime():
    data = helpers.get_latest_entry()
    if helpers.validate_data(data["NextDecisionDate"]) == False:
        print("Updating data...")
        
        print("Data updated.")
        
    boi_interest = data['BoiInterest']
    next_date = data['NextDecisionDate']
    api_data = {
        "BoiInterest": str(float(boi_interest) + 1.5)+ "%",
        "NextDecisionDate": next_date
    }
    return api_data

def update_db():
    fresh_data = interestApi.get_interest_from_net()
    data = fresh_data
    helpers.add_new_item(data["BoiInterest"], data["NextDecisionDate"])

with app.app_context():
    if helpers.is_table_empty() == True:
        print("Updating DB for the first time ..")
        update_db()
        print("Update Successfull - DONE")