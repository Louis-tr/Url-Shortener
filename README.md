# Url-Shortener

A small url "shortener". The length of the resulting urls do obviously depend on the length of your domain and the id length set in the config.

# How to shorten an url
## Api
You can use the `/shorten` endpoint to shorten an url. Just make a post request to that endpoint and provide the "url" key with the original url. You will get back the new url in plain text.

## Web
I added a basic frontend to test the application. Just paste your url into the input and click the "Shorten" button. The input will be updated to the resulting url.

## Dependencies

- [Python 3.6 or higher](https://www.python.org/)    
`pip install -U -r requirements.txt`

## Hosting

### Windows
These are steps to host this website yourself.

- Install [Python](https://www.python.org/downloads/) 3.6 or higher (including pip)
  - Be sure to select "customize installation" and select "Add Python to evironment variables"

- Clone this repository or download it as a zip and extract it

- Open the cmd, navigate in the directory of the website and run the following commands:
  - `python -m pip install -r requirements.txt`

- Run the web.py file with the `python web.py` command.

### Linux & Mac
Should be easy to adapt from the windows guide.
