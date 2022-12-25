import { Component, OnInit } from '@angular/core';
import {NgForm} from '@angular/forms';
import {CustomerService} from "./customer.service";
import {Customer} from "./customer";

@Component({
  selector: 'app-customer',
  templateUrl: './customer.component.html',
  styleUrls: ['./customer.component.css']
})
export class CustomerComponent implements OnInit {
  emailID: string;
  addEmailId: string;
  addUserName: string;
  addFirstName: string;
  addLastName: string;
  addPhone: string;
  updateEmailID: string;
  updateUserName: string;
  updateFirstName: string;
  updateLastName: string;
  updatePhone: string;
  toggleCustomer: boolean;
  toggleAdd: boolean;
  toggleUpdate: boolean;
  customerService: CustomerService;
  customersInfo: Customer[];
  notice: string;

  constructor(customerService: CustomerService) {
    this.emailID = undefined;
    this.updateEmailID = undefined;
    this.notice = undefined;
    this.toggleCustomer = false;
    this.toggleAdd = false;
    this.toggleUpdate = false;
    this.customerService = customerService;
    this.customersInfo = undefined;
  }

  ngOnInit(): void {
  }

  toggleCard(cardId): void {
      this.toggleCustomer = !this.toggleCustomer;
  }

  setCustomerInfo(theCustomer: Customer): void {
    this.customersInfo = [theCustomer];
  }




  onLookup(): void {
    // this.customerService.getCustomers(this.emailID)
    //   .subscribe((data) => this.setCostomerInfo(data));
    if(this.emailID.length>0) {
      this.toggleUpdate=false;
      this.customersInfo = [];
      this.customerService.getCustomers(this.emailID)
        .subscribe((data) => {
          this.setCustomerInfo(data);
        });
    }
    else {
      this.customersInfo=[];
    }
  }

  onShowAdd(): void {
    this.toggleAdd = true;
  }

  onAdd(): void {
    let theCustomer = new Customer();
    theCustomer.emailID = this.addEmailId;
    theCustomer.username = this.addUserName;
    theCustomer.firstname = this.addFirstName;
    theCustomer.lastname = this.addLastName;
    theCustomer.phone = this.addPhone;
    this.customerService.addCustomers(theCustomer)
      .subscribe((response:any) => {
        if(response.status===200){
          this.toggleAdd=false;
          this.notice='Add success!';
        }
        else{
          this.notice='Add fail!';
        }
      });
  }

  onShowUpdate(customerID): void {
    this.toggleUpdate = true;
    this.updateEmailID = customerID;
  }

  onUpdate(): void {
    let theCustomer = new Customer();
    theCustomer.emailID = this.updateEmailID;
    theCustomer.username = this.updateUserName;
    theCustomer.firstname = this.updateFirstName;
    theCustomer.lastname = this.updateLastName;
    theCustomer.phone = this.updatePhone;
    this.customerService.updateCustomers(theCustomer)
      .subscribe((response:any) => {
        if(response.status===200){
          this.toggleUpdate=false;
          this.notice='Update success!';
          this.onLookup();
        }
        else{
          this.notice='Update fail!';
        }
      });
  }
  onDelete(customerID): void {
    this.customerService.deleteCustomers(customerID) .subscribe((response:any) => {
        console.log(response.status);
        if(response.status===200){
          this.onLookup();
          this.notice='Delete success!';
        }
        else{
          this.notice='Delete fail!';
        }
      });

  }

}
