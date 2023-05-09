from time import sleep
import json
from selenium_stealth import stealth
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import undetected_chromedriver as uc



# Configure headless undetected chrome driver to webscrape Ticketmaster
capabilities = DesiredCapabilities.CHROME
capabilities["goog:loggingPrefs"] = {"performance": "ALL"}

ticketmaster_uc = uc.Chrome(use_subprocess=True, 
                            headless=True, 
                            desired_capabilities=capabilities)

stealth(ticketmaster_uc,
        languages=['en-US', 'en'],
        vendor='Google Inc.',
        platform='Win32',
        webgl_vendor="Intel Inc.",
        renderer='Intel Iris OpenGL Engine',
        fix_hairline=True,
        )



# Access ticket availibility and pricing data for event at url
def get_ticket_data(driver, url):

    '''Note: eventually we will want a try/except 
       to make sure our driver works and url is valid'''
    
    # Get network response logs
    driver.get(url)
    sleep(5)
    logs = driver.get_log('performance')

    # Filter for response containing section-wise ticket availibility
    availability_keyword = 'by=inventorytypes+offertypes+accessibility+offers+section+priceLevelSecnames+ticketTypes&q=available&available=true'
    availability_response = find_network_response(driver, logs, availability_keyword)
    print(availability_response['facets'])
    print(len(availability_response['facets']))

    # Filter for response containing ticket pricing
    pricing_keyword = 'by=offers&show=listpricerange&q=available&available=true'
    pricing_response = find_network_response(driver, logs, pricing_keyword)
    print(len(pricing_response['facets']))

    sleep(5)



# Filter through network response logs for keyword 
def find_network_response(driver, logs, keyword):

    '''Want to also think about where to do error checking here'''

    for log in logs:
        log = json.loads(log["message"])["message"]
        if ("Network.responseReceived" in log["method"] and "params" in log.keys()):
            try:
                response = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': log["params"]["requestId"]})
                body = json.loads(response['body'])
                if keyword in body['_links']['self'][0]['href']:
                    return body
            except:
                pass

    return {}


# Testing
ticketmaster_url = 'https://www.ticketmaster.com/bruce-springsteen-and-the-e-street-foxborough-massachusetts-08-24-2023/event/01005E4DD61A4439'

def main():
    get_ticket_data(ticketmaster_uc, ticketmaster_url)

if __name__ == '__main__':
    main()
