# i-NUIST-auto-login
A simple Python script to login i-NUIST automatically
# How to use
1. Use the developer's tools in chrome (or sth else) to get the post header and post data which your browser sends to the server when you click "login" on the webpage.
2. Fill in **#YOUR ACCOUNT**, **#YOUR PASSWORD** and **#DOMAIN** in the script (if you don't know the domain in specific, find it in the post data).
3. Fill in **#YOUR COOKIE** and **#YOUR USER AGENT** in the script. YOUR COOKIE can be found in the header, just copy it; use the browser's user agent).
## ps
You may use **PyInstaller** to make an executive file (eg. *.exe).
I believe you can now make a similar iOS shortcut by yourself! :D
## note
Due to the way Windows handles open networks, the script may fail to function even if you are connected. 
