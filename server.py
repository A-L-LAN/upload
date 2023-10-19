# server.py 

from flask import Flask, request, send_file
import gridfs
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

app = Flask(_name_)

# Connect to MongoDB Atlas cluster 
uri = "mongodb+srv://<allankipruto4th>:<allan28>@cluster0.rqefq2o.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.images
fs = gridfs.GridFS(db)

@app.route('/upload', methods=['POST']) 
def upload_image():
  if request.files:
    image = request.files['image']
    image_id = fs.put(image)
    print('Image uploaded with ID:', image_id)
    
    return image_id

@app.route('/image/<image_id>')
def get_image(image_id):
  file = fs.get(image_id)
  return send_file(file, mimetype='image/jpeg')
  
if _name_ == '_main_':
  app.run(debug=True)
