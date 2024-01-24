from urllib.parse import urlparse, parse_qs
URL='https://someurl.com/with/query_string?i=main&mode=front&sid=12ab&enc=+Hello'
parsed_url = urlparse(URL)
print(parse_qs(parsed_url.query))
print(parsed_url)