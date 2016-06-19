url = 'http://localhost:8069'
db = 'w'
username = 'w'
password = 'w'
requiredFields=["reference_type",'partner_id',"reference_type","account_id","currency_id","journal_id","company_id"]
import xmlrpclib
#info = xmlrpclib.ServerProxy('https://demo.odoo.com/start').start()

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())
uid = common.authenticate(db, username, password, {})
print(uid)
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
print(common.__dict__)
print(models.__dict__)
res=models.execute_kw(db, uid, password,
    'account.invoice', 'check_access_rights',
    ['write'], {'raise_exception': False})
print res
res=models.execute_kw(db, uid, password,
    'account.invoice', 'search',
    [ []])
print res

record = models.execute_kw(db, uid, password,
    'account.invoice', 'read', [1])
toCreate={}
for k,v in record.iteritems():
    if k in requiredFields:
        if len(v)==2:
            v=v[0]
        print k,v
        toCreate[k]=v
r=models.execute_kw(
    db, uid, password, 'account.invoice', 'fields_get',
    [], {})
#for rr,vv in r.iteritems():
 #   print rr,vv
print(toCreate)
id = models.execute_kw(db, uid, password, 'account.invoice', 'create', [toCreate])