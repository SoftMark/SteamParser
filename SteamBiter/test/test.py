import steam
from steam.client import SteamClient
from steam.steamid import SteamID
from steam.client.cdn import CDNClient
from steam.enums.emsg import EMsg

client = SteamClient()

# print(client.auto_discovery)

client.cli_login("zukablyaat", "imheretoseesometits")

@client.on(EMsg.ClientVACBanStatus)
def print_vac_status(msg):
    print("Number of VAC Bans: %s" % msg.body.numBans)


print("Logged on as: %s" % client.user.name)
print("Community profile: %s" % client.steam_id.community_url)
print("Last logon: %s" % client.user.last_logon)
print("Last logoff: %s" % client.user.last_logoff)
print("Number of friends: %d" % len(client.friends))


# session = client.get_web_session()  # returns requests.Session
# session.get('https://store.steampowered.com')

# cdn = CDNClient(client)

# seva = client.get_user(SteamID(steam.steamid.from_url("https://steamcommunity.com/id/BelyiScsgo")))
# seva.send_message("Hello World!")


client.logout()
