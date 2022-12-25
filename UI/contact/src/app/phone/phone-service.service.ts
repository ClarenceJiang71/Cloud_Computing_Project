import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import {phone} from "./phone";
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class phoneService {

  phones: phone[] | undefined;
  // phoneServiceUrl: string;

  constructor(private http: HttpClient) {
    // console.log('The URL = ' + window.location.href);
    this.phones = undefined;
  }

  getStudentServiceUrl(): string {
    const theUrl = window.location.href;
    let result: string;

    // This is some seriously bad code.
    // If you do this on a job interview, you did not learn this in my class.

    result = 'http://127.0.0.1:5011/api/contacts/phone/';

    return result;
  }


  /** GET phone from the server */
  getCustomers(accountId: bigint | undefined): Observable<phone> {
    let theUrl: string;

    theUrl = this.getStudentServiceUrl() + accountId;
    return this.http.get<phone>(theUrl);
  }
}
