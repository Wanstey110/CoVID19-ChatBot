import requests
filenames = ["Chat.txt", "ChatBot.py", "cUpdates.py",
             "growthRate.py"]
for i in filenames:
    response = requests.get(
        f"https://raw.github.com/Wanstey110/CoVID19-ChatBot/Wanstey110-patch-1/{i}")
    with open(i, "w") as file:
        file.write(response.text)
import ChatBot
ChatBot.main()