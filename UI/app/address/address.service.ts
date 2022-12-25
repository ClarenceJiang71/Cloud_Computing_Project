import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import {Address} from './address';
import {AddressRSP} from "./address";
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AddressService {
  address: Address[];
  addressServiceUrl: string;

  constructor(private http: HttpClient) {
    this.address = undefined;
  }

   getAddressServiceUrl(): string {
    const theUrl = window.location.href;
    let result: string;

    // This is some seriously bad code.
    // If you do this on a job interview, you did not learn this in my class.
    if (theUrl.includes('amazonaws')) {
      /* This can change over time */
      result = 'http://34.203.227.98:5011/api/address/';
    }
    else {
      result = 'http://34.203.227.98:5011/api/address/';
    }
    return result;
  }
  getAddress(id): Observable<Address> {
    let theUrl: string;

    theUrl = this.getAddressServiceUrl() + id;
    return this.http.get<Address>(theUrl);
  }
  deleteAddress(id): Observable<Address> {
    let theUrl: string;
    theUrl = this.getAddressServiceUrl() + id;
    return this.http.delete<Address>(theUrl);
  }
  addAddress(theAddress): Observable<any> {
    let theUrl: string;
    theUrl = this.getAddressServiceUrl();
    return  this.http.post<any>(theUrl, theAddress, {observe: 'response'});
  }
  updateAddress(theAddress): Observable<any> {
    let theUrl: string;
    theUrl = this.getAddressServiceUrl();
    return  this.http.put<any>(theUrl, theAddress, {observe: 'response'});
  }


}
