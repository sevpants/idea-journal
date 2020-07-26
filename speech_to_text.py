import config


config = config.get_config()


api_url = config['google-cloud']['idea-journal']['function-url']

print(api_url)