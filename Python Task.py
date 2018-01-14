import pyrebase

config = {
      "apiKey": "apiKey",
      "authDomain": "python-task.firebaseapp.com",
      "databaseURL": "https://python-task.firebaseio.com/",
      "storageBucket": "python-task.appspot.com",
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()


TV = {'Heros': 'The Flash','Power': 'Speed'}
db.child('Superheroes').push(TV)


Team = {"Player": "Kyrie Irving", "Team": "Caviliers"}
db.child("NBA Team").push(Team)


retrieve = db.child("NBA Team").get()
print (retrieve.val())





