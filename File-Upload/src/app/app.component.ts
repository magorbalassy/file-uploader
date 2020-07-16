import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
})
export class AppComponent {
    fList: FileList ;
    filelist: Array<string> = [];

    constructor(private http: HttpClient) { }

    fileChange(files: FileList) {
      this.fList = files;
      for (let i = 0; i < files.length; i++) {
        this.filelist[i] = this.fList[i]['webkitRelativePath'];
      }
    }

    upload() {
      console.log('upload click');
      let formData = new FormData();
      for (var i = 0; i < this.fList.length; i++) {
          formData.append("files[]", this.fList[i], this.fList[i]['webkitRelativePath']);
      }
      this.http.post('https://localhost:5000/upload', formData)
          .subscribe((response) => {
              console.log('response received is ', response);
          })
    }

}