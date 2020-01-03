class API:
    def __init__(self, http):
        self.http = http
    
    async def get_all_cosmetics(self):
        return await self.http.benbot_request(url="http://benbotfn.tk:8080/api/cosmetics")