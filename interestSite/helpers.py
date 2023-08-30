from datetime import datetime
from interestSite.models import DataItem, db


def get_latest_entry():
    latest_entry = DataItem.query.order_by(DataItem.id.desc()).first()
    if latest_entry:
        data = {
            'id': latest_entry.id,
            'Date': latest_entry.current_date,
            'BoiInterest': latest_entry.boi_interest,
            'NextDecisionDate': latest_entry.next_date
        }
        return data
    else:
        return {'message': 'No data entries found'}


def validate_data(next_date):
    date_format = "%d/%m/%Y"
    date_in_db = datetime.strptime(next_date, date_format)
    current_date = datetime.now()
    print("Validating data..")
    if current_date >= date_in_db:
        print("Validation FAILED - Data is out of date.")
        return False
    else:
        print("SUCCESS - Data is up to date.")
        return True


def add_new_item(boi_interest, next_date):
    print("Wirting new data to the db...")
    now = datetime.now().strftime("%d/%m/%Y")
    new_item = DataItem(current_date=now, boi_interest=boi_interest, next_date=next_date)
    db.session.add(new_item)
    db.session.commit()
    print("Successfully wrote data to db.")

def is_table_empty():
    row_count = DataItem.query.count()
    if row_count == 0:
        return True
    else:
        return False


    