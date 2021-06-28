import xmlrpc.client

ODOO_URL = 'http://localhost:8069'
ODOO_DB = 'odoo'
ODOO_USER = 'odoo'
ODOO_PASS = 'odoo'


def printMsg(data_list, title=''):
    if title:
        print(title)
    for line in data_list:
        print('-', line)
    pass


class XMLRPC_API():
    def __init__(self, url, db, user, password):
        self.url = url
        self.db = db
        self.user = user
        self.password = password

        # xmlrpc/2/common: authentication itself or fetching version information
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))

        self.uid = common.authenticate(self.db, self.user, self.password, {})
        print(self.uid)

        # xmlrpc/2/project: used call methods of model via the execute_kw RPC func
        self.models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))
        pass

    # get fields names of the model
    def get_fields(self, model_name, required=False):
        data = self.models.execute_kw(self.db,
                                      self.uid,
                                      self.password,
                                      model_name,
                                      'fields_get',
                                      [],
                                      {'attributes': ['sting', 'type', 'required', 'readonly']})
        if required:
            key_list = list(data.keys())
            for k in key_list:
                if not data[k].get('required', False):
                    data.pop(k)
                pass
        return data

    def search(self, model_name, conditions=[()]):
        return self.models.execute_kw(self.db,
                                      self.uid,
                                      self.password,
                                      model_name,
                                      'search',
                                      [conditions])

    def create(self, model_name, data_dict):
        id = self.models.execute_kw(self.db,
                                    self.uid,
                                    self.password,
                                    model_name,
                                    'create',
                                    [data_dict])
        return id

    def read(self, model_name, conditions=[()], params={}):
        return self.models.execute_kw(self.db,
                                      self.uid,
                                      self.password,
                                      model_name,
                                      'search_read',
                                      [conditions],
                                      params)

    def update(self, model_name, id_list, new_data_dict):
        self.models.execute_kw(self.db,
                               self.uid,
                               self.password,
                               model_name,
                               'write',
                               [id_list, new_data_dict])

    def delete(self, model_name, id_list):
        self.models.execute_pw(self.db,
                               self.uid,
                               self.password,
                               model_name,
                               'unlink',
                               [id_list])
        pass

    def soft_delete(self, model_name, id_list):
        self.update(model_name,
                    id_list,
                    {'active': False, })

    def call(self, model_name, method, params=[]):
        return self.models.execute_kw(self.db,
                                      self.uid,
                                      self.password,
                                      model_name,
                                      method,
                                      params)

    def call2(self, model_name, method, param1, param2):
        return self.models.execute_kw(self.db,
                                      self.uid,
                                      self.password,
                                      model_name,
                                      method,
                                      param1,
                                      param2)


def main():
    client = XMLRPC_API(url=ODOO_URL, db=ODOO_DB, user=ODOO_USER, password=ODOO_PASS)

    data_list = client.read(model_name='my.pet',
                            conditions=[('id', '>=', 1)],
                            params={'fields': ['name', 'nickname']},
                            )
    printMsg(data_list, title='Read My Pet')

    printMsg(client.call2(model_name='my.pet',
                          method='search_read',
                          param1=[['id', '>=', 1]],
                          param2={}),
             title="General call")

    id_new = client.create(model_name='my.pet',
                           data_dict={'name': 'Doberman',
                                      'nickname': 'Body'})
    print(f'Created new pet {id_new}')

    client.update(model_name='my.pet',
                  id_list=[16],
                  new_data_dict={'name': 'Bug Lazy',
                                 'nickname': 'Mỡ'})
    print('Updated my pet')

    pass


if __name__ == "__main__":
    main()
