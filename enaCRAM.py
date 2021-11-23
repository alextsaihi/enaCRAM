import requests
import re

class enaCRAM:
    
    def get_metadata(self, sid):
        try:
            # Validate SID
            self.validate_sid(sid)
            # Make request
            response = requests.get("https://www.ebi.ac.uk/ena/cram/sequence/{}/metadata".format(sid))
        except Exception as e:
            raise e
        return response.json()

    def get_sequence(self, sid):
        try:
            # Validate SID
            self.validate_sid(sid)
            # Make request
            response = requests.get("https://www.ebi.ac.uk/ena/cram/sequence/{}".format(sid))
        except Exception as e:
            raise e
        return response.content

    def validate_sid(self, sid):
        # Check string type
        assert type(sid) is str, "Invalid type: MD5 Sequence ID should be of type String"
        # Check md5 format
        regex = "^[a-f0-9]{32}$"
        valid = re.search(regex, sid)
        if not valid:
            raise ValueError("Invalid MD5 hash: Enter valid MD5 hash string containing 32 characters from a-f and 0-9")
        return valid

    def get_service_info(self):
        response = requests.get("https://www.ebi.ac.uk/ena/cram/sequence/service-info")
        return response.json()
        
sequence = enaCRAM()
refseq = sequence.get_sequence("3050107579885e1608e6fe50fae3f8d0")
print(refseq)