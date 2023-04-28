# Crime predictor and Alerter
TEAM RAVEN'S EYE PRESENTS -
  CRIME ALERT!!! 

> A WEBSITE THAT PREDICTS THE 'CHANCE' OF SUFFERING WITH A CRIMINAL ACT AND PROVIDES ADVISORY BASED  ON REAL  EXTENSIVE CRIME DATABASE OF MIZORAM WHICH IS CONSTANTLY UPDATED BY THE POLICE MAKING IT AN ALL TIME HELPING AID FOR THOSE CONCERNED ABOUT THIER LOVED ONES! 

> Problem statement targetted -  Predictive Policing which involves issuing advisory (how likely a crime can happen) to people who visit a certain place/city/country during a certain time.

### HOW TO USE ? 🤔
    #1. ADVISORY (USER POV)
The homepage of our website opens up with a small form to input the location and time and based on  REAL  EXTENSIVE CRIME DATABASE , after submission of the form it will show how safe it is to visit that location at that time ! It's that easy!

    #2. DATABASE HANDLING (ADMIN POV)

The mizoram police would be able to administer through the password protected website 's admin page where detailed data about any  criminal act could be fed in the database, increasing the accuracy of the prediction.

Note- Currently we have just entered a sample database to check the working of the website . However, once handed to The mizoram police, the database can easily be updated making it functional in real time!

    WORKING PRINCIPLE
Packages you need to install before running website are given in requirements.txt.
After installation, go to predictor folder, and open command line, and enter `python manage.py runserver`. It will run website on localhost:8000.

As said before, our website works on a real criminal act based database updated by the mizoram police providing both facilities- 
1. Checking the advisory as a user. 
2. Updating the database as an admin.
Our website checks the frequency of  criminal acts in a 2 hour wide window around the required time in the required location, it predicts the chance of occurrence of a crime .


To access the admin page, use username as `anshu` and password as `1234`
To create new admin user, use `python3 manage.py createsuperuser` and enter required data which is asked.

Use the following test cases
1. Block- Aibawk , hour- 20 ---> result should be safe 
2. Block - Aibawk, hour- 3 ---> result should be high risk
3. Block - Aibawk, hour- 5 ---> result should be moderate
4. Block Aibawk, hour -6  ---> result should be moderate
5. Block - Darlawn , hour- 6 ---> result should be safe

Here, all the data inserted in the database, most of the crimes are registered in the time window 3-4 am.

[Visit Website](https://hackvecture-nit-mizoram.anshumanrai2.repl.co/predict/)

Contributions:
Priyanshu Das - Frontend, Backend 
Rudransh Srivastav -Backend 
Anshuman Rai- Backend, frontend
Rohit Kumar - Backend.

It was a nice experience.
