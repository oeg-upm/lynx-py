import requestsimport jsonimport osimport requests.exceptionsclass TokenGenarator:                    client_id=''    client_secret=''            def __init__(self,ids,pas):        self.client_id=ids        self.client_secret=pas                                def setKeys(self,ClientID, ClientSecret):        self.client_id= ClientID        self.client_secret = ClientSecret                        def getToken(self,clientId=None, clientSecret=None):                if clientId== None:           clientId=self.client_id           clientSecret=self.client_secret                        print("Generating token for:"+clientId)        url_authen='https://auth.lynx-project.eu/auth/realms/Lynx/protocol/openid-connect/token'                grant_type = "client_credentials"        data = {            "grant_type": grant_type,            "client_id": clientId,            "client_secret": clientSecret            #"scope": scope        }                auth_response = requests.post(url_authen, data=data)                # Read token from auth response                auth_response_json = auth_response.json()        auth_token = auth_response_json["access_token"]            return auth_token                        def getTokenFromFile(self,Path):        f = open("credentials/client_id.txt",encoding="utf8")        self.client_id=f.read().strip()            f = open("credentials/client_secret.txt",encoding="utf8")        self.client_secret=f.read().strip()                return self.getToken()