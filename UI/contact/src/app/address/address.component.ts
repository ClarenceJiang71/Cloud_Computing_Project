import { Component, OnInit } from '@angular/core';
import {address} from "./address";
import {AddressService} from "./address.service";
import {email} from "../email/email";


@Component({
  selector: 'app-address',
  templateUrl: './address.component.html',
  styleUrls: ['./address.component.css']
})
export class AddressComponent implements OnInit {

  accountId: bigint | undefined;
  addressService: AddressService;
  addressInfo: address[] | undefined;

  constructor(addressService: AddressService) {
    this.accountId = undefined;
    this.addressService = addressService;
    this.addressInfo = undefined;

  }

  ngOnInit(): void {
  }

  setAddressInfo(theAddress: address): void {
    console.log("Phone = \n" + JSON.stringify(theAddress, null, 2));
    this.addressInfo = [theAddress];
  }

  onLookup(): void {
    this.addressService.getCustomers(this.accountId)
      .subscribe((data) => this.setAddressInfo(data));
  }
}
