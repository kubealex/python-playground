import ldap
import json
_ldap = ldap.initialize("ldap://idm.rh-lab.labs",bytes_mode=False, bytes_strictness='silent')
ldap_user="uid=admin,cn=users,cn=accounts,dc=rh-lab,dc=labs"
ldap_pass="admin123"
ldap_base="cn=users,cn=accounts,dc=rh-lab,dc=labs"
ldap_scope = ldap.SCOPE_SUBTREE

_ldap.simple_bind(ldap_user,ldap_pass)
_ldap_search = _ldap.search(base=ldap_base, scope=ldap_scope)
type, user = _ldap.result(_ldap_search)
for a, _user in user:
    print(_user.__class__)
    for _attr in _user.values():
        print(b' '.join(_attr).decode('utf-8'))
        print(_attr.__class__)