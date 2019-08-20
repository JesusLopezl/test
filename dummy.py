import conexion
import random

status = ['open', 'pending', 'solved']
priority = ['low', 'normal', 'high', 'urgent']
via = ['chat', 'email', 'voice']
type_ = ['task', 'problem', 'incident', 'question']
description = 'menssage'
subject = 'test'
id_users = []

#generate one ticket
def generator(users,num):
    id_users = conexion.getIdUsers(users)
    data = {'ticket':
        {       
            'subject': subject, 
            'description': description,
            'requester_id': random.choice(id_users),
            'priority': random.choice(priority),
            'status': random.choice(status),
            'type': random.choice(type_),
            'assignee_id': random.choice(id_users),
            'via':{
                'channel': random.choice(via)
            }
        }
    }
    return data

#generate some tickets
def generateTickets(users):
    id_users = conexion.get_id_users(users)
    result = []
    for i in range(3):
            result.append({
            'subject': subject, 
            'description': description,
            'requester_id': random.choice(id_users),
            'priority': random.choice(priority),
            'status': random.choice(status),
            'type': random.choice(type_),
            'assignee_id': random.choice(id_users),
            'via':{
                'channel': random.choice(via)
            }
            
            })
    print(result)
    return result