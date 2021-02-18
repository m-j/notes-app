# notes-app
This is simple python REST API (with JSON) app.

## Endpoints

### GET /notes
Lists all notes from database

Response:
```
[
    {
        "id": 1,
        "content": "testowa notka",
        "createDate": "2021-02-19T00:21:12"
    },
    {
        "id": 2,
        "content": "new note aasda",
        "createDate": "2021-02-19T00:33:34.369307"
    },
    {
        "id": 3,
        "content": "new note aasda xxxx",
        "createDate": "2021-02-19T00:33:47.001308"
    }
]
```

### POST /notes

Creates new note

Request:

```
{
    "content" : "new note aasda xxxx"
}
```

## Configuration

Configuration is stored in config.json file which is red from working directory.

## Migrations

This app does not have proper sophisticated migrations mechanisms however it will automatically 
create tables in database upon connection. This is good enough for this exercise.  

# Your task

Create ansible playbook which:
* pulls this repo
* installs required dependencies: python >= 3.8.5, packages listed in requirements.txt,
postgresql 13
* configures this app to work with installed database and expose API endpoint on port 80
* installs this app as a service (systemd)
* assures that firewall is enabled and all TCP ports other than 80 and SSH are closed

Please make sure that playbook is idempotent.

Please remember to sanity-test app using curl or postman after deployment.

Playbook can be run against local virtual machine (like vagrant box) no need to 
deploy anything to a cloud.