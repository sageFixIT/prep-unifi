import socket
import pymongo

hostname = socket.gethostname()
fqdn = hostname + ".younifi.cloud"
client = pymongo.MongoClient("mongodb://127.0.0.1:27117/ace")
mdb = client.ace
super_mgmt = mdb.setting.find_one({"key":"super_mgmt"})
super_mgmt.pop("_id", None)
super_mgmt["override_inform_host"] = True
print(super_mgmt)
mdb.setting.insert_one(super_mgmt)


mdb.setting.delete_one({"key":"super_identity"})

mdb.setting.insert_one({
    "key" : "super_identity",
    "name" : "UniFi Network",
    "hostname" : fqdn
})
