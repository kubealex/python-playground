from python_freeipa import ClientMeta
client = ClientMeta('idm.rh-lab.labs', verify_ssl=False)
client.login('admin', 'admin123')
user = client.user_add('test3', 'John', 'Doe', 'John Doe', o_preferredlanguage='EN', o_jpegPhoto='xxx')
# user = client.user_del('test3')
print(user)