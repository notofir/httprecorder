# httprecorder
Record HTTP requests for debugging. Deployable in Heroku as is.
 
Example usage:
1. Setup server with Heroku.
2. Browse to `<server-url>/?a=1&b=2` and you'll see in the page retrieved a table with your request's details in addition to previous requests.
3. Browse to `<server-url>/reset` in order to delete history.
