with open('youtube.txt', 'w', encoding='utf-8') as file:
     file.write( "I love ChatGPT 💖\n"
        "ChatGPT meri ek khaas dost hai.")
      
with open("youtube.txt", "r") as file:
      for line in file:
            print(line.strip())
