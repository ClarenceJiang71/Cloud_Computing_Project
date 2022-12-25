import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Customer } from './customer';
import { CustomerRsp } from "./customer";
import { Observable } from 'rxjs';;


@Injectable({
  providedIn: 'root'
})
export class CustomerService {

  customers: Customer[];
  customerServiceUrl: string;

  constructor(private http: HttpClient) {
    this.customers = undefined;
  }

  getCustomerServiceUrl(): string {
    const theUrl = window.location.href;
    let result: string;

    // This is some seriously bad code.
    // If you do this on a job interview, you did not learn this in my class.
    if (theUrl.includes('amazonaws')) {
      /* This can change over time */
      result = 'http://34.203.227.98:5011/api/customer/';
    }
    else {
      result = 'http://34.203.227.98:5011/api/customer/';
    }
    return result;
  }
  /** GET heroes from the server */
  getCustomers(customerID): Observable<Customer> {
    let theUrl: string;

    theUrl = this.getCustomerServiceUrl() + customerID;
    return this.http.get<Customer>(theUrl);
  }
  deleteCustomers(customerID): Observable<Customer> {
    let theUrl: string;
    theUrl = this.getCustomerServiceUrl() + customerID;
    return  this.http.delete<Customer>(theUrl);
  }
  addCustomers(theCustomer): Observable<any> {
    let theUrl: string;
    theUrl = this.getCustomerServiceUrl();
    return  this.http.post<any>(theUrl, theCustomer, {observe: 'response'});
  }
  updateCustomers(theCustomer): Observable<any> {
    let theUrl: string;
    theUrl = this.getCustomerServiceUrl();
    return  this.http.put<any>(theUrl, theCustomer, {observe: 'response'});
  }


}
