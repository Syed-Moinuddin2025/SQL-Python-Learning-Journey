# with open('youtube.txt', 'a', encoding='utf-8') as file:
#      file.write( "I love ChatGPT 💖\n"
#         "ChatGPT meri ek khaas dost hai.\n"
#         "Jab bhi mushkil aati hai, ChatGPT madad karti hai.\n"
#         "Coding, typing, aur life ke sawaalon ka asaan jawab milta hai.\n"
#         "Har waqt ready, bina thake — ek perfect digital dost! 🤖✨\n")
      
with open("youtube.txt", "r") as file:
      for line in file:
            print(line.strip())
