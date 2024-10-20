from DrissionPage import ChromiumPage, ChromiumOptions
from main import scrape_collection_tokens, scrape_collection_general_details

collection_name = 'pixels-farms'

all_collection_tokens = scrape_collection_tokens(collection=collection_name)
collection_general_info = scrape_collection_general_details(collection=collection_name)



