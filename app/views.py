from flask import render_template
import redis
import simplejson
from config import REDIS_CONFIG
from app import app

@app.route('/beta')
def index():
	redis_store = redis.Redis(REDIS_CONFIG['host'])
	instagram_recent_media = {'data': redis_store.get(REDIS_CONFIG['instagram_recent_media_key'])}
	#recent_media_data = simplejson.loads(instagram_recent_media)
	return render_template('index.html', instagram_recent_media=instagram_recent_media)
