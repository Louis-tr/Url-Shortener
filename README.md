# Url-Shortener

An Url-Shortener built with aiohttp and mongodb.

# Api
You can use the `/shorten` endpoint to shorten an url. Just make a post request and provide the "url" key with the original url. You will get back the new url in json format.

## Dependencies

- [Python 3.6 or higher](https://www.python.org/)    
`pip install -U -r requirements.txt`

## Hosting

### Windows
These are steps to host this website yourself.

- Install [Python](https://www.python.org/downloads/) 3.6 or higher (including pip)
  - Be sure to select "customize installation" and select "Add Python to evironment variables"

- Clone this repository or download it as a zip and extract it

- Open the cmd, navigate in the directory of the website and run the following command:
  - `python -m pip install -r requirements.txt`

- Run the web.py file with the `python web.py` command.

### Linux & Mac
Should be easy to adapt from the windows guide.
