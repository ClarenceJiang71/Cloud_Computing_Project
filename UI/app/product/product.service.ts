import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import {Product} from "./product";
import {ProductRsp} from "./product";
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  product: Product[];
  productServiceUrl: string;

  constructor(private http: HttpClient) {
    this.product = undefined;
  }

  getProductServiceUrl(): string {
    const theUrl = window.location.href;
    let result: string;

    // This is some seriously bad code.
    // If you do this on a job interview, you did not learn this in my class.
    if (theUrl.includes('amazonaws')) {
      /* This can change over time */
      result = 'http://34.203.227.98:5011/api/product/';
    }
    else {
      result = 'http://34.203.227.98:5011/api/product/';
    }
    return result;
  }
  /** GET heroes from the server */
  getProducts(productID): Observable<Product> {
    let theUrl: string;

    theUrl = this.getProductServiceUrl() + productID;
    return this.http.get<Product>(theUrl);
  }
  deleteProducts(productID): Observable<Product> {
    let theUrl: string;
    theUrl = this.getProductServiceUrl() + productID;
    return  this.http.delete<Product>(theUrl);
  }
  addProducts(theProduct): Observable<any> {
    let theUrl: string;
    theUrl = this.getProductServiceUrl();
    return  this.http.post<any>(theUrl, theProduct, {observe: 'response'});
  }
  updateProducts(theProduct): Observable<any> {
    let theUrl: string;
    theUrl = this.getProductServiceUrl();
    return  this.http.put<any>(theUrl, theProduct, {observe: 'response'});
  }
}

