#!/usr/bin/python
import os, yaml

def fInput():
	f = open('~/.config/diskplayer/diskplayer.yaml')
	ds = yaml.safe_load(f)
	f.close

	username = input('Your Spotify username or email address')
	password = input('Spotify password')
	device_name = ds[spotify][device_name]
	return fOutput(username,password,device_name)
	
def fOutput(u,p,d):
	print('Writing to file..)')
	config = open('/etc/spotifyd.conf', 'a')
	g = '[global]'
	username = 'username = ' + u
	password = 'password = ' + p
	print('....')
	device_name = 'device_name = ' + d
	config.write(g)
	config.write(username)
	config.write(password)
	print('............')
	config.write(device_name)
	config.close
	print('.................DONE')
	return
	
def main():
	print('This will configure your Spotifyd.conf')
	fInput()
	print('Done! Check "/etc/spotifyd.conf" to be sure!')
	
	
main()
	
	
	
	
##nested dict print(myDict['moo']['d'])
	
	#pip install pyyaml
# spotify:
  # callback_url: http://localhost:8080/callback
  # device_name: YOUR_SPOTIFY_DEVICE_NAME
  # client_id: YOUR_SPOTIFY_CLIENT_ID 
  # client_secret: YOUR_SPOTIFY_CLIENT_SECRET 
# recorder:
  # folder_path: /tmp
  # filename: diskplayer.contents
  # server_port: 3000
# token:
   # path: ./token.json
