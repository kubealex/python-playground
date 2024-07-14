import ldap
import argparse
import json

parser = argparse.ArgumentParser("LDAP Connection example")
parser.add_argument('ldap_server', type=str, help="LDAP Server connection string", default="ldap://idm.rh-lab.labs", nargs="*")
args = parser.parse_args()

print(args.ldap_server)

_ldap = ldap.initialize(args.ldap_server,bytes_mode=False, bytes_strictness='silent')
ldap_user="uid=admin,cn=users,cn=accounts,dc=rh-lab,dc=labs"
ldap_pass="admin123"
ldap_base="cn=users,cn=accounts,dc=rh-lab,dc=labs"
ldap_scope = ldap.SCOPE_SUBTREE

try:
    _ldap.simple_bind_s(ldap_user,ldap_pass)
    _ldap_search = _ldap.search(base=ldap_base, scope=ldap_scope)
    type, user = _ldap.result(_ldap_search)
    print(user)
except ldap.LDAPError as ldap_err: 
    print(ldap_err)
