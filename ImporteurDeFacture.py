
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

class Client:
    nom="res.partner"
    requiredFields=["notify_email","property_account_payable_id","property_account_receivable_id","name","display_name"]
    def __init__(self,id):
        self.id=id


class Facture:
    nom="account.invoice"
    requiredFields = ["reference_type", 'partner_id', "reference_type", "account_id", "currency_id", "journal_id",
                      "company_id"]
    def __init__(self):
        self.company_id=1
        self.currency_id=1
        self.partner_id=44
        self.reference_type= "none"
        self.journal_id=1
        self.account_id=277
        self.lignes=[]
        self.clients=[]

class LigneFacture:
    nom="account.invoice.line"
    requiredFields=["account_id","price_unit","quantity","name","invoice_line_tax_ids"]

    def __init__(self):

        pass



#res=models.execute_kw(db, uid, password,     'account.invoice', 'check_access_rights',    ['write'], {'raise_exception': False})

res=c.getModels().execute_kw(c.db, c.getUid(), c.password,    'account.invoice', 'search',    [ [] ] )
print res


def trouveRequiredFields(c,classe):
    r = c.getModels().execute_kw(c.db, c.getUid(), c.password, classe.nom, 'fields_get', [], {})
    liste=[]
    for rr, vv in r.iteritems():
  #      print(rr,vv)
        if vv["required"]:
            liste.append(rr)
            print(rr)
    return liste

#
trouveRequiredFields(c,Client)

def lisLaDonnee(c,classe,id):
    record=c.getModels().execute_kw(c.db,c.getUid(),c.password,classe.nom,"read",[id])
    print("hi",record)
    toCreate = {}
    for k, v in record.iteritems():
        if "name" in k:
            print(k,v)
        if k in classe.requiredFields:
   #         print(k,v)
            if type(v) is list and len(v) == 2:
                v = v[0]
            print k, v
            toCreate[k] = v
    return toCreate

def ecrisLaDonnee(db,uid,password,models,classe):
    pass

toCreate=lisLaDonnee(c,Client,44)

toCreate=lisLaDonnee(c,LigneFacture,4)
print(toCreate)

toCreate=lisLaDonnee(c,Facture,1301)
print(toCreate)

def creerFacture(c,facture):
    pass

#for i in range(10):
 #   id = c.getModels().execute_kw(c.db, c.getUid(), c.password, 'account.invoice', 'create', [toCreate])