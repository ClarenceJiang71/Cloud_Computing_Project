import { Component, OnInit } from '@angular/core';
import {payment} from "./payment";
import {paymentService} from "./payment-service.service";

@Component({
  selector: 'app-payment',
  templateUrl: './payment.component.html',
  styleUrls: ['./payment.component.css']
})
export class PaymentComponent implements OnInit {

  accountId: bigint | undefined;
  paymentService: paymentService;
  paymentsInfo: payment[] | undefined;

   constructor(paymentService: paymentService) {
    this.accountId = undefined;
    this.paymentService = paymentService;
    this.paymentsInfo = undefined;

  }

  ngOnInit(): void {
  }

  setPaymentInfo(thePayment: payment): void {
    console.log("Phone = \n" + JSON.stringify(thePayment, null, 2));
    this.paymentsInfo = [thePayment];
  }

  onLookup(): void {
    this.paymentService.getCustomers(this.accountId)
      .subscribe((data) => this.setPaymentInfo(data));
  }

}
