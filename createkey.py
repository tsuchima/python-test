from mastodon import Mastodon

#URLの部分はインスタンスURLです ご自身のインスタンスのURLに変えて下さい
# 変数nameはクライアント名を入力して下さい。（自由記述）

url = "https://friends.nico/"
name = input('クライアント名\n> ') 

#Mastodonのアプリ登録を行ないます。

Mastodon.create_app(name,
    api_base_url = url,
    to_file = "app_key.txt"
)
print('api_key作成完了!')  

#メールアドレスの入力
#パスワードの入力

mail = input('メールアドレス\n> ') 
passwd = input('パスワード\n> ') 

#生成されたapp.keyをしてしてログインします。

mastodon = Mastodon(
    client_id="app_key.txt",
    api_base_url = url)

mastodon.log_in(
    mail,
    passwd,
    to_file = "user_key.txt")
print('user_key作成完了!') 

