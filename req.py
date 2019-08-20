import requests
import validation
import conexion
import json
import dummy

user = 'londozzz33@gmail.com'
token = '7xVEmoeJBrhf6QPJ5QPTrR69se0taimGjWwxkW4q'

def test():
    url1 = 'https://test15003.zendesk.com/api/v2/tickets.json?per_page=2'
    while url1:
        response = requests.get(url1, auth=(user+"/token", token))
        data = response.json()
        for article in data['tickets']:
            print(article['status'])
        print('---------------------------')
        url1 = data['next_page']    
    return data


def importUsers(users):
    url1 = 'https://test15003.zendesk.com/api/v2/users.json?per_page=5'
    while url1:
        response = requests.get(url1, auth=(user+"/token", token))
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')
            exit()
        data = response.json()
        group_list = data['users']
        result = []
        for group in group_list:
            tem = validation.separateNames(group['name'])
            if conexion.verifyExistenceUser(users,group['id']):
                if conexion.verifyChangesUser(users,group['id'],group['updated_at']):
                    conexion.updateUser(users,tem[0],tem[1],group['email'],group['id'],group['updated_at'])
            else:
                conexion.addUser(users,tem[0],tem[1],group['email'],group['id'],group['created_at'],group['updated_at']) 
        url1 = data['next_page']    
    return result


def createTickets(users,num):
    url2 = 'https://test15003.zendesk.com/api/v2/tickets.json'
    
    for i in range(int(num)): 
        data = dummy.generator(users,0)    
        payload = json.dumps(data)
        headers = {'content-type': 'application/json'}    
        response = requests.post(url2, data=payload, auth=(user+"/token", token), headers=headers)

    
    if response.status_code != 201:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()

    
    print('Successfully created the ticket.')
    return data

def importInteractions(interactions):
    url2 = 'https://test15003.zendesk.com/api/v2/tickets.json?per_page=5'

    while url2:
        response = requests.get(url2, auth=(user+"/token", token))
        data = response.json()
        group_list = data['tickets']
        result = []
        for group in group_list:
            if conexion.verifyExistenceInteraction(interactions,group['id']):
                if conexion.verifyChangesInteraction(interactions,group['id'],group['updated_at']):
                    conexion.updateInteraction(interactions,group['id'],group['priority'],group['status'],group['assignee_id'],group['updated_at'])
            else:
                conexion.addTickets(interactions,group['requester_id'],group['id'],group['description'],group['priority'],group['status'],group['via']['channel'],group['assignee_id'],group['created_at'],group['updated_at'])
        url2 = data['next_page'] 
    return data






