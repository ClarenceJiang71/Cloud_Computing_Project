import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import {Homepage} from "./homepage";
import {HomepageRsp} from "./homepage";
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HomepageService {

  order: Homepage[];
  productServiceUrl: string;

  constructor(private http: HttpClient) {
    this.order = undefined;
  }

  getOrderServiceUrl(): string {
    const theUrl = window.location.href;
    let result: string;

    // This is some seriously bad code.
    // If you do this on a job interview, you did not learn this in my class.
    if (theUrl.includes('amazonaws')) {
      /* This can change over time */
      result = 'http://34.203.227.98:5011/api/order/';
    }
    else {
      result = 'http://34.203.227.98:5011/api/order/';
    }
    return result;
  }
  /** GET heroes from the server */
  getOrders(orderID): Observable<Homepage> {
    let theUrl: string;

    theUrl = this.getOrderServiceUrl() + orderID;
    return this.http.get<Homepage>(theUrl);
  }
  deleteOrders(orderID): Observable<Homepage> {
    let theUrl: string;
    theUrl = this.getOrderServiceUrl() + orderID;
    return  this.http.delete<Homepage>(theUrl);
  }
  addOrders(theOrder): Observable<any> {
    let theUrl: string;
    theUrl = this.getOrderServiceUrl();
    return  this.http.post<any>(theUrl, theOrder, {observe: 'response'});
  }
  updateOrders(theOrder): Observable<any> {
    let theUrl: string;
    theUrl = this.getOrderServiceUrl();
    return  this.http.put<any>(theUrl, theOrder, {observe: 'response'});
  }
}
