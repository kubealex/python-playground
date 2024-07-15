import ldap
import argparse
import json

### Main/Config

parser = argparse.ArgumentParser("ldaptool")
parser.add_argument("--ldap_server", type=str, help="LDAP Server connection string", default="ldap://idm.rh-lab.labs", nargs="?")
parser.add_argument("--ldap_bind_dn", type=str, help="LDAP Server Bind DN for searches", default="uid=admin,cn=users,cn=accounts,dc=rh-lab,dc=labs", nargs="?")
parser.add_argument("--ldap_bind_pwd", type=str, help="LDAP Server Bind DN password for searches", default="admin123", nargs="?")
parser.add_argument("--ldap_search_base_dn", type=str, help="Base DN for the LDAP search", default="dc=rh-lab,dc=labs", nargs="?")

### Search command

subparser = parser.add_subparsers(title="subcommands", help="Available commands", dest="command")
parser_search = subparser.add_parser("search")
parser_search.add_argument("user", type=str, help="Specify user to search")

### Test connection command

parser_test = subparser.add_parser("test")

args = parser.parse_args()

ldap_scope = ldap.SCOPE_SUBTREE
# search_filter='(&(objectClass=groupOfNames)(member=%s))' % args.ldap_bind_dn

try:
    _ldap = ldap.initialize(args.ldap_server,bytes_mode=False, bytes_strictness="silent")
    _ldap.simple_bind_s(args.ldap_bind_dn, args.ldap_bind_pwd)

    if (hasattr(args, "user")):
        search_filter="uid=%s" % args.user
        _ldap_search = _ldap.search(base=args.ldap_search_base_dn, scope=ldap_scope, filterstr=search_filter)
        type, user = _ldap.result(_ldap_search)
        print(user)

    if (args.command == "test"):
        print("Successfully connected to", args.ldap_server, "with user", args.ldap_bind_dn)

except ldap.LDAPError as ldap_err: 
    print(ldap_err)