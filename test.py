# code taken from
# https://developers.google.com/sheets/api/quickstart/python
# run using cmd: python test.py

from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

# The ID of the spreadsheet can be found in the url:
# https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=sheetId
SPREADSHEET_ID = '1lNvvAS-VqpD3ia7HIbkb5ZhGQKIrkHBoM0_fX1myZ3A'
# range of data to look at
RANGE = 'A1:D4'

def main():
    # ----- CODE FROM GOOGLE, DONT TOUCH -----
    # Shows basic usage of the Sheets API. Prints values from a sample spreadsheet.
    # The file token.json stores the user's access and refresh tokens,
    # and is created automatically when the authorization flow completes for the first time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE).execute()
    values = result.get('values', [])

    sheet.values().(spreadsheetId=SPREADSHEET_ID, range=RANGE)


    # ----- FUN STUFF STARTS HERE (my code) -----

    if not values:
        print('No data found.')
    else:
        for row in values:
            # prints the data data (it says row but its actually ABCD)
            print('%s, %s, %s, %s' % (row[0], row[1], row[2], row[3]))

if __name__ == '__main__':
    main()