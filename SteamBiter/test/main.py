import steam
from steam.steamid import SteamID
from steam import webapi
from steam.webapi import WebAPIInterface
import steam_market


# # print(SteamID(steam.steamid.from_url("https://steamcommunity.com/id/zukablyaat")))
# my_id = SteamID(steam.steamid.from_url("https://steamcommunity.com/id/zukablyaat"))
api = steam.webapi.WebAPI(key="3DE99EE3A26CBD36596B35704788627D")
print(api.call('ISteamUser.ResolveVanityURL', vanityurl="valve", url_type=2))
doc = api.doc()

doc_ISteamUser = doc[doc.find("ISteamUser"):doc.find("ISteamUserAuth")]
doc_GET_splited = doc.split("GET")

# print(doc)
# All get
# for GET_splited in doc_GET_splited:
#     print(GET_splited[0:GET_splited.find("(")])
    # print(GET_splited[GET_splited.find("Get"):GET_splited.find("(")])


# print(doc[doc.find("GetItemID")-50:doc.find("GetWorldStatus")])
# print(doc_ISteamUser)



lines_splited_doc = doc.split("--")
while True:
    try:
        lines_splited_doc.remove('')
    except:
        break

interfaces_dict = {}
i = 0
while(i < len(lines_splited_doc) - 1):
    interface_name = lines_splited_doc[i]
    interface_name = interface_name[interface_name.find("I"):-1]
    interfaces_dict[interface_name] = lines_splited_doc[i+1]
    i+=2

print(lines_splited_doc)

for key in interfaces_dict:
    print(key)











#print(api.call('ISteamUser.GetFriendList'))
# user_api = steam.webapi.get("ISteamUser", "ResolveVanityURL")
# print(user_api)
# my_id = SteamID(steam.steamid.from_url("https://steamcommunity.com/market/listings/753/322170-Dovahkiin"))
# print(my_id)


#steam_market.get_csgo_item("Snakebite Case")