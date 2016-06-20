
import xmlrpclib


class Connection:
    def __init__(self,url,db,username,password):
        self.url=url
        self.db=db
        self.username=username
        self.password=password
        self.uid=None
        self.models=None
        self.hasModel=False

    def getUid(self):
        if not self.uid:
            common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
            self.uid = common.authenticate(self.db, self.username, self.password, {})
        return self.uid

    def getModels(self):
        if not self.hasModel:
            self.models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(self.url))
            self.hasModel=True
        return self.models




c=Connection('http://localhost:8069','w',"w","w")
#print(c.getUid())
#print(c.getModels())
#models=c.getModels()

class Facture:
    nom="account.invoice"
    requiredFields = ["reference_type", 'partner_id', "reference_type", "account_id", "currency_id", "journal_id",
                      "company_id"]
    pass
class LigneFacture:
    nom="account.invoice.line"
    requiredFields=["account_id","price_unit","quantity"]
    pass



#res=models.execute_kw(db, uid, password,     'account.invoice', 'check_access_rights',    ['write'], {'raise_exception': False})

#res=models.execute_kw(db, uid, password,    'account.invoice', 'search',    [ [] ] )
#print res


def trouveRequiredFields(c,classe):
    r = c.getModels().execute_kw(c.db, c.getUid(), c.password, classe.nom, 'fields_get', [], {})
    liste=[]
    for rr, vv in r.iteritems():
        if vv["required"]:
            liste.append(rr)
            print(rr)
    return liste

trouveRequiredFields(c,LigneFacture)

def lisLaDonnee(c,classe,id):
    record=c.getModels().execute_kw(c.db,c.getUid(),c.password,classe.nom,"read",[id])
    print("hi",record)
    toCreate = {}
    for k, v in record.iteritems():
        if k in classe.requiredFields:
   #         print(k,v)
            if type(v) is list and len(v) == 2:
                v = v[0]
            print k, v
            toCreate[k] = v
    return toCreate

def ecrisLaDonnee(db,uid,password,models,classe):
    pass

toCreate=lisLaDonnee(c,Facture,1)
print(toCreate)

for i in range(10):
    id = c.getModels().execute_kw(c.db, c.getUid(), c.password, 'account.invoice', 'create', [toCreate])