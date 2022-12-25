import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {email} from "./email";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class emailService {
  emails: email[] | undefined;

  constructor(private http: HttpClient){
    this.emails = undefined;
  }

  getStudentServiceUrl(): string {
    const theUrl = window.location.href;
    let result: string;

    // This is some seriously bad code.
    // If you do this on a job interview, you did not learn this in my class.

    result = 'http://127.0.0.1:5011/api/contacts/email/';

    return result;
  }

  /** GET phone from the server */
  getCustomers(accountId: bigint | undefined): Observable<email> {
    let theUrl: string;

    theUrl = this.getStudentServiceUrl() + accountId;
    return this.http.get<email>(theUrl);
  }



}
