import requests

ref = None


class Payment:
    def __init__(self,key,email,amounts):
        self.key = key
        self.email = email
        self.amounts = amounts
        
    def pay(self):
        url = "https://api.paystack.co/transaction/initialize"
        data = {
            'email': self.email,
            'amount' : self.amounts * 100
        }
        
        headers = {
            "Authorization": 'Bearer ' + self.key,
            "Content-Type" : 'application/json'
        }
        
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            data = response.json() 
            ref = data['data']['reference']
            auth_link = data['data']['authorization_url']
            result = {
                'reference_id': ref,
                'auth_url': auth_link
                }
            return data
            
        else:
            return ('Error:', response.status_code)
        
    def status(self):
        global ref
        while True:
            url = f"https://api.paystack.co/transaction/verify/{ref}"
            headers = {
                "Authorization": "Bearer " + self.key
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                gateway_response = data['data']['gateway_response']
                if gateway_response == "Successful":
                    return "successful"
                elif gateway_response == "The transaction was not completed":
                    continue
                else:
                    return "failed"
            
           
           


    
    
        


            
