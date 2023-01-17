# flaskats

First version/tag was a flask project with Airtable API.

Second challenge/version works with Recruitee API and Hello Sign for contract signing.
In addition, we incorporate a DB for users and offers, so it's necessary to register users for administration purposes.

--------------------------------------------
To register an user, follow the next steps:
--------------------------------------------
Enter to the command line and execute  

    flask --app flaskats shell

then  

    from flaskats import db, bcrypt
    from flaskats.models.user import User

    hash_password = bcrypt.generate_password_hash("password").decode('utf-8')
    user = User(username = "Name", email = "email", password=hash_password)
    db.session.add(user)
    db.session.commit()

Now, you can login into an admin account.

--------------------------------------------

To obtain active offers:
--------------------------------------------
Enter to the command line and execute
    curl -X GET 'https://api.recruitee.com/c/{company_id}/offers?scope=active&view_mode=brief' -H 'Authorization: Bearer {api_token}' > offers.json

--------------------------------------------

To obtain info about a candidate:
--------------------------------------------
Enter to the command line and execute
    curl -X GET 'https://api.recruitee.com/c/{company_id}/candidates/46369420' -H 'Authorization: Bearer {api_token}' >candidate.json



--------------------------------------------
Improvements for next versions
--------------------------------------------

- Notifier responsabilities: Separate in a better way the functionality of check_candidates function, throw implementing other clases or services that help to accomplish this task.

- Testing: Improve the test coverage (latest value 68%)

- APIs: Consider response errors and delayed responses from APIs

- Offer Deletion: Add a double confirmation for deletion
