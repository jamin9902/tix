from tm_api_tools import client

apikeys = ['2oPiS5JzXX2Eh0D9ANZ3VUoF7TncvmOS']

tm_client = client.ApiClient(apikeys[0])

def get_event_info(event):
    unavailableMessage = 'Not Available'

    eventID = event.id 
    eventName = event.name
    eventDate = event.local_start_date
    eventTime = event.local_start_time
    eventURL = event.url
    venue = unavailableMessage
    city = unavailableMessage
    stateCode = unavailableMessage
    countryCode = unavailableMessage

    venues = event.venues

    if venues:
        venue = venues[0].name
        city = venues[0].city
        countryCode = venues[0].country_code
        if countryCode == "US":
            stateCode = venues[0].state_code

    return (eventID, eventName, venue, city, stateCode, countryCode, eventDate, eventTime, eventURL)


#Testing
def main():
    page = tm_client.events.find(
        start_date_time='2023-06-01T20:00:00Z',
        end_date_time='2023-06-03T20:00:00Z'
    ).limit()

    for event in page:
        event_tuple = get_event_info(event)
        for i in event_tuple:
            print(i)
        print('\n')
    
if __name__ == '__main__':
    main()