import Channel

ch = Channel.Channel("hi")
print(ch.get_name())


ch.login("client_secret.json", "credentials.storage")
