import { Injectable } from '@angular/core';
import {address} from "./address";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class AddressService {
  address: address[] | undefined;

  constructor(private http: HttpClient){
    this.address = undefined;
  }

  getStudentServiceUrl(): string {
    const theUrl = window.location.href;
    let result: string;

    // This is some seriously bad code.
    // If you do this on a job interview, you did not learn this in my class.

    result = 'http://127.0.0.1:5011/api/contacts/address/';

    return result;
  }

   getCustomers(accountId: bigint | undefined): Observable<address> {
    let theUrl: string;

    theUrl = this.getStudentServiceUrl() + accountId;
    return this.http.get<address>(theUrl);
  }
}
