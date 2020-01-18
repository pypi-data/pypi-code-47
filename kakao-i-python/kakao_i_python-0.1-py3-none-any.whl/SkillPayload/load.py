# {
#  "userRequest": {
#     "timezone": "Asia/Seoul",
#     "params": {},
#     "block": {
#       "id": "<블록 id>",
#       "name": "<블록 이름>"
#     },
#     "utterance": "<사용자 발화>",
#     "lang": "kr",
#     "user": {
#       "id": "<사용자 botUserKey>",
#       "type": "botUserKey",
#       "properties": {
#         "plusfriendUserKey": "<카카오톡 채널 사용자 id>"
#       }
#     }
#   },
#   "contexts": [],
#   "bot": {
#     "id": "<봇 id>",
#     "name": "<봇 이름>"
#   },
#   "action": {
#     "name": "<스킬 이름>",
#     "clientExtra": null,
#     "params": {},
#     "id": "<스킬 id>",
#     "detailParams": {}
#   }
# }
import json
class payload:
    def __init__(self, userRequest):
        self.data = userRequest["userRequest"]

    def gettimezone(self):
        return json.loads(self.data["timezone"])

    def getblockinfo(self):
        return json.loads(self.data["block"])

    def gettext(self):
        return json.loads(self.data["utterance"])

    def getlang(self):
        return json.loads(self.data["lang"])

    def getbotinfo(self):
        return json.loads(self.data["bot"])
    
    def getaction(self):
        return json.loads(self.data["action"])

    def getuserid(self):
        return json.loads(self.data["user"]["id"])

    def getuserproperties(self):
        return json.loads(self.data["user"]["properties"])