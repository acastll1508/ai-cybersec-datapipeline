import ipaddress

def process_auth(match):

    data = match.groupdict()

    status = "failed" if "Failed" in data["event"] else "success"

    ip_obj = ipaddress.ip_address(data["ip"])
    
    # Add 4 couples "key:value" in order to be turn into new columns in return dataframe.
    data["status"] = status        
    data["ip_int"] = int(ip_obj)
    data["is_private"] = ip_obj.is_private 
    data["ip_version"] = ip_obj.version
    

    return data