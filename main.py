from atproto import Client

client = Client()
client.login('sacstatefediverse.bsky.social', 'HtOalLpbaLzBObgAWgs3BYGOk5avRK')

post = client.send_post('Test')