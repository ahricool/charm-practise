spreadsheet_id = "1CrJNrVq6SpsigvWUg5fKha5l4SEmIjW8mwg3XOCqE8s"
from googleapiclient import discovery
from google.oauth2 import service_account
import os

key_path = os.path.abspath(os.path.dirname(__file__)) + '/c2.json'

# create credentials by oauth2client (version > 4.0.0)
# credentials = ServiceAccountCredentials.from_json_keyfile_name(key_path, scopes=scope)

# # create credentials by google.oauth2

GOOGLE_CREDENTIALS_FOR_FEATURED_STORY = {
    "type": "service_account",
    "project_id": "upcoming-games-monitor",
    "private_key_id": "092030a18d9d47a39dd27d9937795e5f9fc577df",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDdDnYwaEUNllaO\nGurJbq7bB6AMq+O28ypVXk0YnoAZ57CqB1yDgIZLMgvOardR3LFHOUijCHnNLbeI\n4B4EY2lNXYiGcQxj9EiI44jWqzsPEP5aOTAEQrlVwHrIdqEBYD+MAVUxPY4xUZwy\nVC+LhssQcfTVxqk5+ph2kCfAxl6syHdF6AETwq0ki0oPgeCt1wXn4xhmIOxswbFK\nGGb6Ce3X2rLLIqbS3oIwT+QK/r8uxcyU7OSs1MgDey15ZuN+9nS6IvcG8d47ZRuw\nydOWeDd7xmw5o/RgsIjRWI+KLWEi6b7i/X9vdoGXFB0Q03Qm8TOshNWG4fPwLlp5\nbjYbsYUxAgMBAAECggEAMSNN0mTbNLH+e4gwOKaJ59ZCFY8AB2L2PhPAP4C8KQX/\nl0wbnH+tWnm9dhzysxfDsHljVBpGOP24lox7H66ZccEg4AGxJ2bd2M/7UvytHCRC\n5ftgWRIb8Jvgrz7ve0bR2WVScqekPAJQHj/ocbN84CL0sbB/XYv+6BwTOh7eXLmp\nQkg/btYcCligoQfiar6Jc5RXOchxUD5Qv9a9eaw0QHofkwmi+Uy+P0iqj6uUTRqo\nlX9LAb5BTjapVBt59oZXqeqN6bGt2Yj56lWf+s4Ooio7LJXEEJTxJqe98r60n2kv\nrHy2P7GdCZJeLvOKxEW0qQyMxgVmJNKud7c/SiS9gQKBgQDycSgS6Kook30tBvid\nhRvObiux/ZjI+GfdFWw00STfBuO3w6IWLxstTILNHLAPtoG77bk4JRbSyeB39inY\n1ikVoc3gmi/V28nvjkgwkTFbHt7iJFzZqebDX7LPrXTm1ElKmi20CfwOloMUGsZt\nr7rw4UZ6tbXp98mD6rl77yYCVQKBgQDpayVmhdB9P5N5Od8Y8DNXNbal2ATrxZ0m\neo0IrkcUf3So+rAd34Pv4ZInO4UFWnsSwlYbkmdyQ7oRH58zrJezcJQ2Qyceh2lY\ngCRj5EZF76gvAbhm8ETACeHWc8O8RfL99IakzKsB6xFkCP/HxPIP7NJJDv1u3oMl\nYcKFkmVrbQKBgAfXsTwrWpXFb58tQo2V6Lhcx/0R/wdBQdrc/osW2OJ+Do+7PFsL\nWw20E+cernNTrA6wOfWe/YYEEcbPp7rj8qBIg6hoVHPOkFG3gI5RpA8WiI84Lei8\nnkJjrh0Zt1ZgN566LhBM4mJ2a/cShqi1ro5sOyNtDV1sLpCd3zIrIkehAoGAWrNR\n0ybIPwMHUSHVuSENMiQjFwp7zwn46MzSJL9jy2lDca4H5XPHFt12J1yPcecYz89I\nGmqnW9VJZgH9oNy+DfH/BZ7OgqRnoQYaHd7EF8Tqe2mVuBpA/MZaRTSyqGQd6eSs\ntTj6ckJffZmpmnzC+sExbUYv4HcCSvJT3gdm9XkCgYAiegkMcc0CyIfaRthFY6YF\n1FjygrqtbWk/1bvd+zmC4P6ZFVxg/gPMSsxuxbQlqGoTiUCKtIEqo11cAsEBikd/\nBoSf7MUbKm0oOiQcSjjViFgGpzJ44+fyzOY+f7LpsyxYbhPYPpMjRU49v2YZnIqH\nCBJwNOdifLSNdI23go7iYQ==\n-----END PRIVATE KEY-----\n",
    "client_email": "read-upcoming-games-info@upcoming-games-monitor.iam.gserviceaccount.com",
    "client_id": "101947338534252121999",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/read-upcoming-games-info%40upcoming-games-monitor.iam.gserviceaccount.com"
}

# c2={
#   "type": "service_account",
#   "project_id": "companytest-283609",
#   "private_key_id": "5d6fc9aea63f3382d6b289fcc5fff4746868b8af",
#   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCxKP1jsyi6AvQf\nyizWGbMg/C+E4eom0ZS0SRBKDx69vGfil4r+mvmhhjUgIvCqguuWwHNrDZeSSTaS\nYq1C6obbiOWqHNWpDtUQyLYxYBHgFHfaauepD0aLxB8yzwlBg/CzSnqi3NHKra4/\nEg8byeQGcyi0SVpyUoVbP1Byqhx/H/6IKjRj3hji+/jXLeM89lIKglAcMx8FNcvg\n8c3my8I0bg3gJ2y3A4+0qKFKNMwqOUfJoluoGA3M+/72nGZa1QZGVVEs86SI2VDv\n2Z5kg7qsyfTtbzzRzXx8yVjjWZ8v1fGy6S6itHsoeLn1bxjniLxhAKJgM50YUy24\nQ/xjyrZdAgMBAAECggEAB5MomRmLzWmbQDwNRGRElU2jHIE/rpmPIabuxDPhonGK\nrD9tiSsILxYFcdJ8oYByi/do7UlfUzkVKmzUsAPwxd8/GVHH+EVdlSz3zqRRxK0r\nXhKXGtKVN3GodywvXvaXapsYePE3I9Le8exsP/Rsbwgqfow/tUao/rig0HOh6fTa\nbMBx2h2WlxSI7jIgDfyMxQULKG2dgcoISn36tyxNtm8AHtQJIkJe0a2tLdWALC6E\nk4haX9WDN16BFyrWZ9Fi+2AwAUc0rP+ucyyJGYE69amTHtp98SGy6/75BgPvJ6rH\nx1ZAfl6nnulkNFagZ+bGMutrYg0LzxOFpt2Jre1ykwKBgQDuTi3WDH5PRZrWycOJ\nokx5iBr7iDJyCuJExlx2u7q/Sm0pUe/DgqTYxEzJxsjnO6cZDxtj7onWqCjcL0t2\nPG3sb9ZUma3aMfJZLCaMmEeGP9QaNiDi2fE2kxU1CatqzNOhr7xd7W5Qa94J2F7i\nn9EHSPz2DGUR/2Gf0QbwTjb9KwKBgQC+UIhdb/w/5IFdu9PoCT4chNtefjgixv6q\nB+BADlUo2gL5TzY/lUj6wJ/qnxYjmhvGPbVXHaX+ixCETXtWKqIbH5UDx8yjihNf\nWNexuzZkPv0uzWOgRaOI86f1C7PqBwR+r4Dw3sR4VtSZJX+48yZBqSAiSc9BriGW\ndJzY2dUmlwKBgDW3r8NhW5OY+BdUsdwzlpOKp7JteBmW9HxWTn+BP85hA4xd6PMk\nXu5yCXEuexkMrFUMv7reCXo2u8cubg8//fNfHmxBnBvkSGHrfuEQbocHmlMyQmWA\nhUwtCYnEHTzc4RPAXnC51bURK6MCgBkLt32x6Tu5fYr6C1KQNsUyjFizAoGAagiw\nkW6tWmPT+AeIX0WXB4i2OIWWfTnl9ZIBzW6u393nvkP186MXUC42ayBL03Yvd1o2\nSN1J+PI+N5h72VxTiU0lVz/gslVhycPUGUA3Y878fTEOCuQB43Ht6Eem7AMQ7AyY\niJt1V575QIJ2EPPYIsk6ECCTiwKb0BoUsXVcnu0CgYASfCsiquUMfZdNW+ySWDVd\nhJZjkiocWIR73s5oj3mEv4/yhTbGT/Txu+BMQ20ymdnNAhv5/aMY2IcSCFmHRliE\n/0svyfl9Db3+29vxluQcDC7upgqpweGTRQ8lw67eGlMSYGdVrdnj8+g04ADP4XSm\ndCdG0Flnw/X57Yfsic0rog==\n-----END PRIVATE KEY-----\n",
#   "client_email": "aatest@companytest-283609.iam.gserviceaccount.com",
#   "client_id": "109932596000694441434",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/aatest%40companytest-283609.iam.gserviceaccount.com"
# }

new_cred = {
    "type": "service_account",
    "project_id": "aa-connect-prod-metrics",
    "private_key_id": "3521751ef169756d7d0b3d6d119b7ab553717c99",
    "private_key": '-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDE/wxmgjonYpJg\ne9riUXKpUM15AdmVdmCThsuQJrSV4XmbbmYXCSiQO8Cctk7cTjDwNFyeTEz0ESA7\nuR8uBufZLk6p3Vjh7moT2ogY+VWzP60cFE2ClCdZOjt4ROFqWG1mgholGhpZ+PPC\nGQfTHNQW+eS0BmvTyB/NGO9849D20kKFGvazPVDutcHLCVMpDwrPQJmMgwLB7xGG\nUqbmtrCQopUaI6/xpoBWXqMzuFE2kmd+38w7LbfgTfdfKWBwCs/mzwU1A9kavpfW\n9NlnCHwyexLM1VlALUGyaHEzRkHgVPQ/wailh/vfaMMzKc4Kq0OdeB1Q1QnaYNdq\n1ls0rSZdAgMBAAECggEAJIJoV+82u+nm2v7ZWCxkJcEV86FGJA8mYvEOdQ7XVRfO\no+HYBdjqraCFWAXpo6bSJxJtP+FAOdOat7bdcnhRK80LQywEtwqqmjdcFdTP70KT\n4KpamyK+EClcsDOD22O8Es117v5hd99NveFJs/SZ0hBKNJskDMIAMtC2Qd0u8y89\nC5eK3IotLneJEFw0oY+/7Y+PkDtaR87y+uZ4NXQgjgRuZOKeD9wCl49KRehKFfkb\nxJ0Ip6NBSZGzcFT99XFQHv1ZCs3YbCAtNMeYHtZ++terwh2Eb5bVLgg/z6gW4Ewo\nKEVbc4ZPnSJhiPf7/bj3zr18aOidIY74E/ig1sASgQKBgQD25K+DcFOjF4hNoGzx\nH7vnBt8pbujPsfRaoCwmt2sN2n3ZqPP5v/LgsGv8Y+iLv+Uj63iKQw/NLYkAUsFy\nVpPI4CFBSt6WwOgJ22BlwWUuTmCtfmp5FeyinRpc5/q//g9aT3ROcnOdIY8IdnYg\ntFN+BFAs/l1/ZZP5EkZZQ/GErQKBgQDMQzSOcudzZt1fF30Kstv7VGJXdcTOX+tP\ny0STPWjuq2pnXBaRbQ18aq6ecKicUOHAOv1syIbxzhBw9OAFJf/+i/ryvooxEYge\n2F1Wd61iAyggDVjoEQ9T0gohcrX6A5gAncZ3Tyi01NMOFsCj5qhA3LOHI92NXHm0\n7ly7QvSucQKBgQCwvG+vxX75puTZvNd/nFnkPZUOkehylU74eORiKralyhyA7WMJ\nC5EPqvsCR3q2X33mQq+dOfhbxhbmdlcoRDWyfE8R8Eh63ki8lZ/h95k4lr66M16A\no2Mr3Q58J0vmmDXhTjNR3LhKaTV8t2BEdRG3idri+otvoQVWLPDTAcIoWQKBgHfz\nh2uXwp+caqerDX0458JCHbYqrLZc0bz8K3sj9vkhpMyp4X7pQaAsrfrRQdL6FHhk\nq+o0IDrjvff3dY7Qb/K1lVrz1gdWuk8S1E0w3prOK8QW0n0Fd7DLibN2v7LgZWUH\nQkNSMx9uU7rUVbBqhagBc1QLFdIr2jUMPVyixzmhAoGBAIwH7osTxrb8rtCOK6GR\nvaB5Nqn7bSLrclCfNhoTHdpue/tF4H2eY0oqMXWv+CWx39OcZwTClJM93j8+kGED\nkGJbZE8qeEAEclelibzrSHgMddACtIQagAPs9XO+VE5+M9HSL2IyNjuJM9AgYmoi\n5xUcOE44/sDcyBu8LGVs9774\n-----END PRIVATE KEY-----\n',
    "client_email": 'aa-conn-prod-metrics@aa-connect-prod-metrics.iam.gserviceaccount.com',
    "client_id": "114258887326697771348",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/aa-conn-prod-metrics%40aa-connect-prod-metrics.iam.gserviceaccount.com"
}


# from googleapiclient import discovery
# from google.oauth2 import service_account
# from django.conf import settings
# cred=settings.ASCEND_CMT_GOOGLE_API_CREDENTIAL
# spreadsheet_id = "1QY9W9C0htVXYPq4UhXAgCh3ropxWJ6eXNuBcbGVdEDA"
credentials = service_account.Credentials.from_service_account_info(new_cred) \
    .with_scopes(["https://www.googleapis.com/auth/spreadsheets"])

# Using API keys
service = discovery.build('sheets', 'v4', credentials=credentials)

result = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id, range="Sheet1!A:G").execute()
rows = result.get('values', [])
print(rows)

values = [
    ["we", "all", "toge"],
    [ "we", "sd", "2323"]
]
body = {
    'values': values
}
result = service.spreadsheets().values().append(
    spreadsheetId=spreadsheet_id, range="Sheet1",
    valueInputOption="RAW", body=body).execute()
print('{0} cells appended.'.format(result.get('updates')))
