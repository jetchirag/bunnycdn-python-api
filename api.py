# Python wrapper for BunnyCDN 
# Auther: @jetchirag

import requests 
import json

class BunnyCDN:
    
    def __init__(self, AccessKey):

        self._AccessKey = AccessKey
        self._URL = "https://bunnycdn.com/api"
        
    def GetHeaders(self):
        header = {
            'Content-Type' : 'application/json',
            'accesskey' : self._AccessKey
        }
        return header
    
    def _VerifyResponse(self, r):
        if r.status_code != 200:
            response = {
                "status": "error",
                "status_code": r.status_code,
                "result": None,
            }
            return json.dumps(response)
        else:
            response = {
                "status": "success",
                "status_code": r.status_code,
                "result": r.text,
            }
            return json.dumps(response)
            
    
    def _CallAPI(self, APIURL, APIMETHOD, header, APIDATA={}):
        if APIMETHOD == "GET":
            r = requests.get(APIURL, headers=header, params=APIDATA)
        elif APIMETHOD == "POST":
            r = requests.post(APIURL, headers=header, json=APIDATA)
        elif APIMETHOD == "DELETE":
            r = requests.delete(APIURL, headers=header, params=APIDATA)
        return r
        
    def ListZones(self):
        APIURL = self._URL + '/pullzone';
        header = self.GetHeaders()
        r = self._CallAPI(APIURL, "GET", header)
        return self._VerifyResponse(r)
        
    def CreateZone(self, name, OriginUrl):
        APIURL = self._URL + '/pullzone';
        header = self.GetHeaders()
        
        APIDATA = {
            'Name' : name,
            'OriginUrl' : OriginUrl
        }
        
        r = self._CallAPI(APIURL, "POST", header, APIDATA)
        return self._VerifyResponse(r)
    
    def GetZone(self, ZoneID):
        APIURL = self._URL + '/pullzone/' + ZoneID
        header = self.GetHeaders()
        r = self._CallAPI(APIURL, "GET", header)
        return self._VerifyResponse(r)
    
    def UpdateZone(self, ZoneID, APIDATA):
        APIURL = self._URL + '/pullzone/' + ZoneID
        header = self.GetHeaders()
        
        r = self._CallAPI(APIURL, "POST", header, APIDATA)
        return self._VerifyResponse(r)
    
    def DeleteZone(self, ZoneID):
        APIURL = self._URL + '/pullzone/' + ZoneID
        header = self.GetHeaders()
        
        r = self._CallAPI(APIURL, "DELETE", header)
        return self._VerifyResponse(r)
    
    def PurgeCache(self, ZoneID):
        APIURL = self._URL + '/pullzone/' + ZoneID + '/purgeCache'
        header = self.GetHeaders()
        
        r = self._CallAPI(APIURL, "POST", header, {})
        return self._VerifyResponse(r)
    
    def addHostname(self, ZoneID, Hostname):
        APIURL = self._URL + '/pullzone/addHostname'
        header = self.GetHeaders()
        
        APIDATA = {
            "PullZoneId" : ZoneID,
            "Hostname" : Hostname
        }
        
        r = self._CallAPI(APIURL, "POST", header, APIDATA)
        return self._VerifyResponse(r)
    
    def addHostname(self, ZoneID, Hostname):
        APIURL = self._URL + '/pullzone/addHostname'
        header = self.GetHeaders()
        
        APIDATA = {
            "PullZoneId" : ZoneID,
            "Hostname" : Hostname
        }
        
        r = self._CallAPI(APIURL, "POST", header, APIDATA)
        return self._VerifyResponse(r)
    
    def deleteHostname(self, ZoneID, Hostname):
        APIURL = self._URL + '/pullzone/deleteHostname'
        header = self.GetHeaders()
        
        APIDATA = {
            "id" : ZoneID,
            "hostname" : Hostname
        }
        
        r = self._CallAPI(APIURL, "DELETE", header, APIDATA)
        return self._VerifyResponse(r)
        
    # TODO:  def setForceSSL():
    
    def loadFreeCertificate(self, hostname):
        APIURL = self._URL + '/pullzone/loadFreeCertificate'
        header = self.GetHeaders()
        
        APIDATA = {
            "hostname": hostname
        }
        r = self._CallAPI(APIURL, "GET", header, APIDATA)
        return self._VerifyResponse(r)
    
    # TODO: def addCertificate():
    
    def addBlockedIp(self, ZoneID, BlockedIP):
        APIURL = self._URL + '/pullzone/addBlockedIp'
        header = self.GetHeaders()
        
        APIDATA = {
            "PullZoneId" : ZoneID,
            "BlockedIp" : BlockedIP
        }
        
        r = self._CallAPI(APIURL, "POST", header, APIDATA)
        return self._VerifyResponse(r)
    
    def removeBlockedIp(self, ZoneID, BlockedIP):
        APIURL = self._URL + '/pullzone/removeBlockedIp'
        header = self.GetHeaders()
        
        APIDATA = {
            "PullZoneId" : ZoneID,
            "BlockedIp" : BlockedIP
        }
        
        r = self._CallAPI(APIURL, "POST", header, APIDATA)
        return self._VerifyResponse(r)
    
    def purgeURL(self, URL):
        APIURL = self._URL + '/purge?url=' + URL
        header = self.GetHeaders()
        
        r = self._CallAPI(APIURL, "POST", header)
        return self._VerifyResponse(r)
        
