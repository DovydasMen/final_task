# Hangman

Hangman is a word guessing game. After correct letter guessed it shows up in a correct place. You start a game with 10 lifes and after each wrong guess you lose 1 life. Game continues untill you guess all the letters before running out of lifes and win the game. If you run out of lifes while guessing letters, you lose the game. 

# Getting started

First of all, you should have Python 3.11.3 and Docker installed on your machine. This project was projected to work fully on Docker containers. There is possibility to play it on local machine after Git cloning aswell but Docker Mongo db container still neededs to be. 

#   Installation
1. Pull source code from Git repository.
2. Install all requirements because of external libraries. Command: pip install -r requirements.txt 
3. Activate your virtual environment.
4. Set up Mongo Db container with command: Docker run -d -p 27017:27017 --name hangman_db mongo:latest
(Here in main.py you could modify db connection. Host to 0.0.0.0 at the end of the code, in login_service and login_service_after_registration. After these modifications were made it could be launched on our local mashine.)
                *** Important ***
If you are planning to create app's Docker image you should modify Mongo db object according to Mongo's db container IP. To get it's IP command - docker inspect container_name and change IP accordingly. 

5. As mentioned before all parts are docerized. Now you should build our image from Dockerfile. Command: docker build . -t hangman_app:v1 -f docker/Dockerfile
6. After image is created you need to run it. Worth to know, that there is a file_logger which loggs info into file, you need to get those loggings. Thats why you need use -v tag, mounting source repositoryt to dockers containers. In this case you get all new created file including log file.
docker run -v ./src:/app/  -it <image_id>

# Credits
Big thanks to all mentors and classmates for all the help when I was stuck. I am also thankfull to our mentors for sharing knowledge and wisdom with us!
@vychiokas
@mindaugeliseth