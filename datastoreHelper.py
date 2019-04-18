import uuid
def log_me_in(username, password):
    from google.cloud import datastore

    datastore_client = datastore.Client("lookbus")
    query = datastore_client.query(kind='users')

    users = list(query.fetch())

    for user in users:
        if user["username"] == username and user["password"] == password:
            return True

    return False

def get_me_list():
    from google.cloud import datastore

    datastore_client = datastore.Client("lookbus")
    query = datastore_client.query(kind='users')

    users = list(query.fetch())

    res = []

    for user in users:
        temp = {}
        temp = user['id'], user['username'], user['password']
        res.append(temp)
    
    return res

def delete_me(id):
    from google.cloud import datastore

    datastore_client = datastore.Client("lookbus")

    key = datastore_client.key('users', id)
    datastore_client.delete(key)


def run_quickstart(username, password):
    from google.cloud import datastore

    datastore_client = datastore.Client("lookbus")

    kind = 'users'
    name = str(uuid.uuid4())
    task_key = datastore_client.key(kind, name)

    task = datastore.Entity(key=task_key)
    task['id'] = name
    task['username'] = username
    task['password'] = password

    datastore_client.put(task)

    print('Saved {}: {}'.format(task.key.name, task['username']))
