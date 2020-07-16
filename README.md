# App Index

This very minimalistic application lets you create a nice page displaying multiple applications and serve it.
Built in functionality enables you to filter out applications by pressing "space" typing the text on which you want to filter the apps and pressing "enter".


## Usage
To add new applications simply edit applications.json 
e.g.
```
[
 {
    "category": "Documentation",
    "applications": [
      {
        "name": "Wiki",
        "description": "Confluence Wiki",
        "link": "https://wiki",
        "image": "img/wiki.jpg"
      }
    ]
  }
]
```
and add an image named "wiki.jpg" into a directory named "img" in the root directory of the repo.

## Building
Simply run `docker build -t app_index:1.0.0 .`

## Running
After building run `docker-compose up -d` to start serving the app on port 8080.