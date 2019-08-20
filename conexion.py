import pymongo
from bson import ObjectId
from datetime import datetime
import validation

#verify if the user already exists in the database
def verifyExistenceUser(users,id_user):
        existing_document = users.find_one({'integration_id': id_user})
        if not existing_document:
                return False
        else:
                return True

#check if there are new changes in the user
def verifyChangesUser(users,id_user,id_update):
        document = users.find_one({'integration_id': id_user},{'updated_at':1,'_id':0})
        if document == id_update:
                return False
        else :
                return True

#verify if the ticket already exists in the database
def verifyExistenceInteraction(interactions,id_interaction):
        existing_document = interactions.find_one({'interaction_id': id_interaction})
        if not existing_document:
                return False
        else:
                return True

#check if there are new changes in the ticket
def verifyChangesInteraction(interactions,id_interaction,id_update):
        document = interactions.find_one({'interaction_id': id_interaction},{'updated_at':1,'_id':0})
        if document == id_update:
                return False
        else :
                return True

#add a new user to the database
def addUser(users,name, last_name, email, id, created_at, updated_at):
        users_id = users.insert({
        'name': name,
        'last_name':last_name,
        'email': email,
        'integration_id': id,
        'created_at': created_at,
        'updated_at': updated_at,
        'created_at':created_at,
        'updated_at':updated_at
        #'created_at': datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%SZ'),
        #'updated_at': datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%SZ')
        })
        new_users = users.find_one({'integration_id':id})
   
        return new_users

#get users
def getUsers(users):
        result = []
        for field in users.find():
                result.append({
                'name': field['name'], 
                'last_name': field['last_name'],
                'email': field['email'],
                'integration_id':field['integration_id'],
                'created_at':field['created_at'],
                'updated_at':field['updated_at']
        })
        return result 

#update a user
def updateUser(users,name, last_name, email, id, updated_at):
        users.find_one_and_update({'integration_id':id}, {"$set": {
        'name': name,
        'last_name':last_name,
        'email': email,
        'updated_at': updated_at
        }}, upsert=False) 

#add news tickets to the database
def addTickets(interactions,requester_id, id, description, priority, status, via, assignee_id, created_at, updated_at):
        interactions.insert({
        'requester_id': requester_id,
        'interaction_id':id,
        'description':description,
        'priority':priority,
        'status':status,
        'via':via,
        'assignee_id':assignee_id,
        'created_at':created_at,
        'updated_at':updated_at        
        })

#get tickets
def getTickets(interactions,users):
        result = []
        for field in interactions.find():
                result.append({
                'requester_id':getNameUsers(users,field['requester_id']),
                'interaction_id': field['interaction_id'], 
                'description': field['description'],
                'priority': field['priority'],
                'status':field['status'],
                'via':field['via'],
                'assignee_id': getNameUsers(users,field['assignee_id'])
                })
        return result 

#update ticket
def updateInteraction(interactions,id,priority,status,assignee_id,updated_at):
        interactions.find_one_and_update({'interaction_id':id}, {"$set": {
        'priority': priority,
        'status':status,
        'assignee_id': assignee_id,
        'updated_at': updated_at
        }}, upsert=False) 

#get users to select
def getDataUsers(users):
        result =[]
        for field in users.find():
                result.append({
                'name': field['name'], 
                'last_name': field['last_name'],
                'integration_id':field['integration_id']
                })
        return result

#get the names of the users
def getNameUsers(users,id):
        document = users.find_one({'integration_id':id},{'name': 1, 'last_name':1,'_id': 0 } )
        result = document['name']+' ' +document['last_name']
        return result

#get the id of the users
def getIdUsers(users):
        result =[]
        for field in users.find():
                result.append( 
                        field['integration_id']
                )
        return result


#filter by users id
def getFilterIdUsers(interactions,users,id):
        id_user = int(id)
        result = []
        for field in interactions.find({'assignee_id':id_user}):
                result.append({
                'requester_id': getNameUsers(users,field['requester_id']),
                'interaction_id': field['interaction_id'], 
                'description': field['description'],
                'priority': field['priority'],
                'status':field['status'],
                'via':field['via'],
                'assignee_id': getNameUsers(users,field['assignee_id'])
                #'created_at':field['created_at'],
                #'updated_at':field['updated_at']
        })
        return result 

#filter by interactions id
def getFilterIdInteraction(interactions,users,id):
        id_interaction = ''
        query = {}
        if id != '':
                id_interaction = int(id)
                query = {'interaction_id':id_interaction}
        else:
                query = {}
        result = []
        for field in interactions.find(query):
                result.append({
                'requester_id': getNameUsers(users,field['requester_id']),
                'interaction_id': field['interaction_id'], 
                'description': field['description'],
                'priority': field['priority'],
                'status':field['status'],
                'via':field['via'],
                'assignee_id': getNameUsers(users,field['assignee_id'])
                #'created_at':field['created_at'],
                #'updated_at':field['updated_at']
        })
        return result 

#general filter
def getFilter(interactions,users,id,priority,status):
        query = validation.organizeInquiry(id,priority,status)
        print(query)

        result = []
        for field in interactions.find(query):
                result.append({
                'requester_id': getNameUsers(users,field['requester_id']),
                'interaction_id': field['interaction_id'], 
                'description': field['description'],
                'priority': field['priority'],
                'status':field['status'],
                'via':field['via'],
                'assignee_id': getNameUsers(users,field['assignee_id'])
                #'created_at':field['created_at'],
                #'updated_at':field['updated_at']
        })
        return result 

