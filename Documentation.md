# Task3
Develop a RESTful API for Authentication

Base URL
https://your-app-name.herokuapp.com/api/

Endpoints:
1. User Registration
Endpoint: /register/
Method: POST
Request Body:
email: User's email
password: User's password
Response:
Status Code: 201 Created
Body: User ID and email

2. User Authentication
Endpoint: /login/
Method: POST
Request Body:
email: User's email
password: User's password
Response:
Status Code: 200 OK
Body: Access token and refresh token

3. Access Token Refresh
Endpoint: /refresh/
Method: POST
Request Body:
refresh_token: User's refresh token
Response:
Status Code: 200 OK
Body: New access token and refresh token

4. Logout
Endpoint: /logout/
Method: POST
Request Body:
refresh_token: User's refresh token
Response:
Status Code: 200 OK
Body: Success message

5. Retrieve Personal Information
Endpoint: /me/
Method: GET
Headers:
Authorization: Bearer token
Response:
Status Code: 200 OK
Body: User ID, username, and email

6. Update Personal Information
Endpoint: /me/
Method: PUT
Headers:
Authorization: Bearer token
Request Body:
username: New username
Response:
Status Code: 200 OK
Body: Updated user information

Code Repository
The complete code for this project is available in the master branch of the GitHub repository
