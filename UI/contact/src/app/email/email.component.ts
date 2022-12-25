import { Component, OnInit } from '@angular/core';
import {email} from "./email";
import {emailService} from "./email-service.service";

@Component({
  selector: 'app-email',
  templateUrl: './email.component.html',
  styleUrls: ['./email.component.css']
})
export class EmailComponent implements OnInit {

  accountId: bigint | undefined;
  emailService: emailService;
  emailsInfo: email[] | undefined;

  constructor(emailService: emailService) {
    this.accountId = undefined;
    this.emailService = emailService;
    this.emailsInfo = undefined;

  }

  ngOnInit(): void {
  }

  setEmailInfo(theEmail: email): void {
    console.log("Phone = \n" + JSON.stringify(theEmail, null, 2));
    this.emailsInfo = [theEmail];
  }

  onLookup(): void {
    this.emailService.getCustomers(this.accountId)
      .subscribe((data) => this.setEmailInfo(data));
  }
}
