# Hangman

Hangman is a word guessing game where after correct guess the letter shows up in correct place. You starting game with 10 lifes. If you guessed the word until 0 lifes left you win otherwise you lose!

# Getting started

First of all you should have python and docker installed on you machine. This project projected to work fully on docker containers. After git cloning there is possibility to play it on local machine but still docker mongo db container still needed. 

#   Installation

1. Pull git repository.
2. Install all requirements because there are external libraries. Command: pip install -r requirements.txt 
3. Activate your virtual enviroment.
4. Set up Mongo Db container with command: docker run -d -p 27017:27017 --name hangman_db mongo:latest
(Here in main.py you should modify db connection to host to 0.0.0.0 at the end of the code and in login_service. After these modifications in could be launched on our local mashine.)
                *** Important ***
If you are planning to create app's image you should modify Mongo Db object according to Mongo's Db in Docker IP. To get it's IP command - docker inspect container_name and change ip accordingly. 

5. As mentioned that all parts is docerized. Now we should build our image from Dockerfile. Command: docker build . -t hangman_app:v1 -f docker/Dockerfile
6. After we have image we need to run our image. Worth to know, that there is a file_logger which loggs info into file, we need to get those loggings. Thats we we use -v tag, mounting source repositoryt to dockers containers. In this case we get all new created file including log file.
docker run -v ./src:/app/  -it 6bdb494f9532

# Credits
Thanks to our mentors and helpers when I have stuck they reached out hand of help. Also I am thankful for them that they shared with us they knowladge and wisdom!
@vychiokas
@