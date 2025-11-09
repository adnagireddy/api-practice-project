Hi y'all don't mind me - this is me trying to build a python-based api by following this tutorial: https://www.youtube.com/watch?v=Ha3ls0EAtW8.

Update: project completed! Use insomnia to test this app. 

Testing Notes
1. Make sure to set port to 5002 
2. make sure to add to header: 
    { 'Content-Type' : 'application/json' }
3. To test if the POST route works, make sure in the json reponse, the id value increments (i.e id:1 becomes id:2 if there was alread an existing value in db)

Summary of What I Did:
1. set up a flask app 
2. create quick sql alchemy db 
3. created a CRUD application that allows user to mantain a database of travel destinations, add, modify, and delete it  
4. Tested all api routes on insomnia, configured headers and JSON request bodies. 

YAYYYYYY. ok bai. 
