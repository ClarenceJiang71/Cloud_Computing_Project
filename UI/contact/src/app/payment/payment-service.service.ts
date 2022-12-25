import { Injectable } from '@angular/core';
import {payment} from "./payment";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class paymentService {
  payments: payment[] | undefined;

  constructor(private http: HttpClient){
    this.payments = undefined;
  }

  getStudentServiceUrl(): string {
    const theUrl = window.location.href;
    let result: string;

    // This is some seriously bad code.
    // If you do this on a job interview, you did not learn this in my class.

    result = 'http://127.0.0.1:5011/api/contacts/payment/';

    return result;
  }

  getCustomers(accountId: bigint | undefined): Observable<payment> {
    let theUrl: string;

    theUrl = this.getStudentServiceUrl() + accountId;
    return this.http.get<payment>(theUrl);
  }
}
