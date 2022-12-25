import { Component, OnInit } from '@angular/core';
import {NgForm} from '@angular/forms';
import {CompositeService} from "./composite.service";
import {Composite} from "./composite";

@Component({
  selector: 'app-composite',
  templateUrl: './composite.component.html',
  styleUrls: ['./composite.component.css']
})
export class CompositeComponent implements OnInit {
  emailID: string;
  toggleComposite: boolean;
  compositeService: CompositeService;
  compositesInfo: Composite[];

  constructor(compositeService: CompositeService) {
    this.emailID = undefined;
    this.toggleComposite = false;
    this.compositeService = compositeService;
    this.compositesInfo = undefined;
  }

  ngOnInit(): void {
  }

  toggleCard(cardId): void {
      this.toggleComposite = !this.toggleComposite;
  }

  setCustomerInfo(theCustomer: Composite): void {
    this.compositesInfo = [theCustomer];
  }




  onLookup(): void {
    // this.customerService.getCustomers(this.emailID)
    //   .subscribe((data) => this.setCostomerInfo(data));
    if(this.emailID.length > 0) {
      this.compositesInfo = [];
      this.compositeService.getCustomers(this.emailID)
        .subscribe((data) => {
          this.setCustomerInfo(data);
        });
    }
    else {
      this.compositesInfo = [];
    }
  }


}
