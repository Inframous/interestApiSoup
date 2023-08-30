from bs4 import BeautifulSoup
import subprocess


def get_interest_from_net():
    url = "https://www.boi.org.il/"
    response = subprocess.run(["curl", url], capture_output=True, text=True)
    html_content = response.stdout
    soup = BeautifulSoup(html_content, "html.parser")

    boi_interest = soup.find_all("div", {"class": "interestAndInflationValue order-1"})[0].text.replace("%",'').strip()
    next_date = soup.find_all("div", {"class": "interestAndInflationComment order-3"})[0].text.split(":")[1].strip()
    
    data = {
        "BoiInterest": boi_interest,
        "NextDecisionDate": next_date
    }
    
    return data
