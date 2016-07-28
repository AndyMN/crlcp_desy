import requests
from auth_vars import USERNAME, PASSWORD, WRONG_PASSWORD, WRONG_USERNAME

url = "https://prometheus.desy.de:443/Users/" + USERNAME + "/"

file_to_open = "notice1"

file_to_upload_name = "CMSCalorimeter.png"
file_to_upload_dir = "/home/andy/"

"""
print "OPEN FILE NOTICE"
r = requests.get(url + file_to_open, auth=(WRONG_USERNAME, PASSWORD))
print r.headers
r = requests.get(url + file_to_open, auth=(USERNAME, PASSWORD))
print r.headers


print "DELETE DIR OR FILE"
r = requests.delete(url + file_to_open, auth=(USERNAME, PASSWORD))
print r.status_code, r.reason


print "DOWNLOAD FILE"
r = requests.get(url + "notice", stream=True, auth=(USERNAME, PASSWORD))
with open(file_to_upload_dir + "notice", 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:  # filter out keep-alive new chunks
            f.write(chunk)
print r.status_code, r.reason


print "UPLOAD FILE CMSCALORIMETER"
with open(file_to_upload_dir + file_to_upload_name, 'rb') as data:
    r = requests.put(url + file_to_upload_name, data=data, auth=(USERNAME, PASSWORD))
print r.status_code, r.reason
"""



r = requests.get(url + "public-file", auth=(USERNAME, PASSWORD))
print r.status_code, r.reason
print r.headers

r = requests.get(url + "private-file", auth=(USERNAME, PASSWORD))
print r.status_code, r.reason
print r.headers
