#This method serves to separate the user's full name
def separateNames(full_name):
    result = full_name.split()
    return result

#This method is used to organize the type of filtering
def organizeInquiry(id,priority,status):
    query={}

    if id != 'all' and priority != 'all' and status !='all':
        id_user = int(id)
        query = {'assignee_id':id_user,'priority':priority,'status':status}
        return query

    elif id != 'all' and priority != 'all' and status =='all':
        id_user = int(id)
        query = {'assignee_id':id_user,'priority':priority}
        return query
    
    elif id != 'all' and priority == 'all' and status !='all':
        id_user = int(id)
        query = {'assignee_id':id_user,'status':status}
        return query

    elif id == 'all' and priority != 'all' and status !='all':
        query = {'priority':priority,'status':status}
        return query

    elif id != 'all' and priority == 'all' and status =='all':
        id_user = int(id)
        query = {'assignee_id':id_user}
        return query
    
    elif id == 'all' and priority == 'all' and status !='all':
        query = {'status':status}
        return query
    
    elif id == 'all' and priority != 'all' and status =='all':
        query = {'priority':priority}
        return query



