# Interest API

This is a simple API that scrapes Bank Of Israel's site for the current national interest rate. (Using BeatifulSoup)
On the app's launch it will scrape the data from Bank Of Israel into a sqlite db.
The db enrty will have the current date, the interest rate and the next date of decision.(The interest rate is decided upon 8 times per year)
Every time a request is made, the API will first check to see if the current date has past (or is equal to) the "Next Update Date" if so, the backend will update the db with new data and return it, otherwise the API will return the current interest rate and the next update date based on the latest entry in the db.

## Installaion 

### Build Your Own Container
```code
git clone https://github.com/Inframous/interestApiBoi.git
sudo docker build -t "interestapi" .
sudo docker run -d -p 80:80 --restart always --name interestapi interestapi
```
Point your browser at `http://<api_url>/api/interest/boi` to receive Bank Of Israel's interest rate, or use `http://<api_url>/api/interest/prime` for Israel "Prime Interest"

### Docker Hub (x86 only)
Pull the image from Docker.io and run it.
```code
sudo docker pull inframous/interestapi:latest
sudo docker run -d -p 80:80 --restart always --name interestapi interestapi
```
Point your browser at `http://<api_url>/api/interest/boi` to receive Bank Of Israel's interest rate, or use `http://<api_url>/api/interest/prime` for Israel "Prime Interest"
