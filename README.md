# File Upload using http(s)

A simple tool to upload a folder and its content to a remote server.
Inspired by online examples: the tool is a combination of several online blogs (thanks all), modified a bit for my needs.  
- https://blog.jscrambler.com/implementing-file-upload-using-node-and-angular/
- https://www.smashingmagazine.com/2017/09/uploading-directories-with-webkitdirectory/
- https://github.com/roytuts/python/tree/master/python-flask-rest-api-multiple-files-upload

## Details

The `File-Upload` folder is the Angular code, which can be compiled to `bundle.js` and used with the Flask backend.  
The REST API of the server side is almost an exact copy of the above github repo, adjusted a bit for my needs.  
The REST API has two endpoints and both the HTML+JS and Angular frontends can be used with it. The endpoints won't do anything but the upload, feel free to adjust it to your needs.  
- `/` : endpoint for the HTML + JS API
- `/upload`: Angular endpoint


