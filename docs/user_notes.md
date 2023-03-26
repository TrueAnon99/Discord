# User Notes
Modify user's notes for your account

## PUT /users/@me/notes/{user-id}
Where {user-id} is the ID of the user whose notes you wish to modify

### Payloads:
Object with the following properties  
| name  | type   | description        |
|-------|--------|--------------------|
| notes | string | Notes for the user |

## Response code
204 if all is successful
