To run this toy example follow these steps

1. python model.py

This creates and saves a regression model as a pickle file which can be loaded later.

2. python server.py

This starts the server at port 5050 at address 127.0.0.1

3. python request.py

This sends a request to the server address. It is sending the number of years experience, and the regression model created earlier predicts a salaray based on this request, and prints on the terminal
