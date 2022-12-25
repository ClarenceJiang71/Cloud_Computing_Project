import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Shop } from './shop';
import { ShopRsp } from "./shop";
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ShopService {

  shop: Shop[];
  shopServiceUrl: string;

  constructor(private http: HttpClient) {
    this.shop = undefined;
  }

  getShopServiceUrl(): string {
    const theUrl = window.location.href;
    let result: string;

    // This is some seriously bad code.
    // If you do this on a job interview, you did not learn this in my class.
    if (theUrl.includes('amazonaws')) {
      /* This can change over time */
      result = 'http://34.203.227.98:5011/api/shop/';
    }
    else {
      result = 'http://34.203.227.98:5011/api/shop/';
    }
    return result;
  }
  /** GET heroes from the server */
  getOrder(shopID): Observable<Shop> {
    let theUrl: string;

    theUrl = this.getShopServiceUrl() + shopID;
    return this.http.get<Shop>(theUrl);
  }
  deleteShops(shopID): Observable<Shop> {
    let theUrl: string;
    theUrl = this.getShopServiceUrl() + shopID;
    return  this.http.delete<Shop>(theUrl);
  }
  addShops(theShop): Observable<any> {
    let theUrl: string;
    theUrl = this.getShopServiceUrl();
    return  this.http.post<any>(theUrl, theShop, {observe: 'response'});
  }
  updateShops(theShop): Observable<any> {
    let theUrl: string;
    theUrl = this.getShopServiceUrl();
    return  this.http.put<any>(theUrl, theShop, {observe: 'response'});
  }
}
