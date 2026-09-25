CONCURRENT_LIMIT = 5
DEFAULT_TIMEOUT = 5

def get_target_urls():
    print("🌐 Enter the URLs you want to test (type 'done' or press Enter when finished):")
    urls = []
    
    while True:
        url = input("Enter URL > ").strip()
        if url.lower() == 'done' or url == "":
            break
        
        if not (url.startswith("http://") or url.startswith("https://")):
            url = "https://" + url
            
        urls.append(url)
        
    return urls