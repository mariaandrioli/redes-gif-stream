# coding=utf-8
from giphy_client.rest import ApiException
import giphy_client, random

def gifUrl():
	# create an instance of the API class
	api_instance = giphy_client.DefaultApi()
	api_key = 'iJKajUqoVS09YBIEgUFcEUdj4ceh0XX0' # str | Giphy API Key.
	limit = 1 # int | The maximum number of records to return. (optional) (default to 25)
	rating = 'g' # str | Filters results by specified rating. (optional)
	fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)

	try: 
		# Trending GIFs Endpoint
		gifType = ['gif', 'sticker']
		choice = random.choice(gifType) # decide se é gif ou sticker

		if choice == 'gif':
			url = api_instance.gifs_random_get(api_key, rating=rating, fmt=fmt).data.fixed_height_downsampled_url # para gifs normais
		else:
			url = api_instance.stickers_random_get(api_key, rating=rating, fmt=fmt).data.fixed_height_downsampled_url # para stickers
		# print(api_response)
		return(url, choice)

	except ApiException as e:
		print("Exception when calling DefaultApi->gifs_trending_get: %s\n" % e)

