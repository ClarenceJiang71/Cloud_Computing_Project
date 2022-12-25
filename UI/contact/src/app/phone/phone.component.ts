import { Component, OnInit } from '@angular/core';
import {phone} from "./phone";
import {phoneService} from "./phone-service.service";

@Component({
  selector: 'app-phone',
  templateUrl: './phone.component.html',
  styleUrls: ['./phone.component.css']
})
export class PhoneComponent implements OnInit {

  accountId: bigint | undefined;
  phoneService: phoneService;
  phonesInfo: phone[] | undefined;

  // constructor() { }

   constructor(phoneService: phoneService) {
      this.accountId = undefined;
      this.phoneService = phoneService;
      this.phonesInfo = undefined;
  }

  ngOnInit(): void {
  }

  setPhoneInfo(thePhone: phone): void {
    console.log("Phone = \n" + JSON.stringify(thePhone, null, 2));
    this.phonesInfo = [thePhone];
  }

  onSomethingInput(e: Event) : void {
    // console.log("Input = ", (<HTMLInputElement> e.target).value);
    this.accountId = BigInt((<HTMLInputElement> e.target).value);

    this.phoneService.getCustomers(this.accountId)
      .subscribe((data) => this.setPhoneInfo(data));
  }

   onLookup(): void {
    this.phoneService.getCustomers(this.accountId)
      .subscribe((data) => this.setPhoneInfo(data));
  }
}
