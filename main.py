
from flask import Flask, request, render_template,url_for,redirect
import requests
from bs4 import BeautifulSoup
import json
def get_all_particpate(username,contestname,contest_number):
  p = 1
  url =  "https://leetcode.com/contest/api/ranking/" + contestname + "-"+contest_number + "/?pagination=" + str(p) + "&region=india"
  response = requests.get(url)
  if response.status_code == 200:
    total_no_of_pages = int(response.json()['user_num'])//25 + 1
    for p in range(1,total_no_of_pages+1):
      url =  "https://leetcode.com/contest/api/ranking/" + contestname + "-"+contest_number + "/?pagination=" + str(p) + "&region=india"
      response = requests.get(url)
      if response.status_code == 200:
        user_pat = response.json()["total_rank"]
        for i in user_pat:
          if username.strip() == i['username']:
             return ({'username' : i['username'],'rank' : i['rank']+1,'score':i['score']})
    return {'username':username,'rank':"-",'score':'-'}
app = Flask(__name__)
@app.route('/get_participate', methods=['GET'])
def get_participate():
    username = request.args.get('username')
    contestname = request.args.get('contestname')
    contest_number = request.args.get('contestnumber')
    a = get_all_particpate(username,contestname,contest_number)
    return render_template('home.html', output= a)
@app.route('/')
def hello_world():
	return render_template('home.html', output="")
if __name__ == '__main__':
	app.run()