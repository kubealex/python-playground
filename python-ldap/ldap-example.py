import ldap
import argparse
import json

parser = argparse.ArgumentParser("LDAP Connection example")
parser.add_argument("ldap_server", type=str, help="LDAP Server connection string", default="ldap://idm.rh-lab.labs", nargs="?")
parser.add_argument("ldap_bind_dn", type=str, help="LDAP Server Bind DN for searches", default="uid=admin,cn=users,cn=accounts,dc=rh-lab,dc=labs", nargs="*")
parser.add_argument("ldap_bind_pwd", type=str, help="LDAP Server Bind DN password for searches", default="admin123", nargs="*")
parser.add_argument("ldap_search_base_dn", type=str, help="Base DN for the LDAP search", default="cn=users,cn=accounts,dc=rh-lab,dc=labs", nargs="*")
args = parser.parse_args()
ldap_scope = ldap.SCOPE_SUBTREE

try:
    _ldap = ldap.initialize(args.ldap_server,bytes_mode=False, bytes_strictness="silent")
    _ldap.simple_bind_s(args.ldap_bind_dn, args.ldap_bind_pwd)
    _ldap_search = _ldap.search(base=args.ldap_search_base_dn, scope=ldap_scope)
    type, user = _ldap.result(_ldap_search)
    print(user)
except ldap.LDAPError as ldap_err: 
    print(ldap_err)
