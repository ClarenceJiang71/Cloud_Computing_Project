import { Component, OnInit } from '@angular/core';
import {AddressService} from "./address.service";
import {Address} from "./address";

@Component({
  selector: 'app-address',
  templateUrl: './address.component.html',
  styleUrls: ['./address.component.css']
})
export class AddressComponent implements OnInit {
  id: string;
  addId: string;
  addAccountId: string;
  addStreet: string ;
  addAptNo: string;
  addCity: string;
  addState: string;
  addZip: string;
  updateId: string;
  updateAccountId: string;
  updateStreet: string ;
  updateAptNo: string;
  updateCity: string;
  updateState: string;
  updateZip: string;
  toggleAddress: boolean;
  toggleAdd: boolean;
  toggleUpdate: boolean;
  addressService: AddressService;
  addressInfo: Address[];
  notice:string;

  constructor(addressService: AddressService) {
    this.id = undefined;
    this.updateId= undefined;
    this.notice=undefined;
    this.toggleAddress = false;
    this.toggleAdd = false;
    this.toggleUpdate = false;
    this.addressService = addressService;
    this.addressInfo = undefined;
  }

  ngOnInit(): void {
  }

  toggleCard(cardId): void {
      this.toggleAddress = !this.toggleAddress;
  }

  setAddressInfo(theAddress: Address): void {
    this.addressInfo = [theAddress];
  }
  onLookup(): void {
    if(this.id.length>0) {
      this.toggleUpdate=false;
      this.addressInfo=[];
      this.addressService.getAddress(this.id)
        .subscribe((data) => {
          this.setAddressInfo(data);
        });
    }
    else {
      this.addressInfo=[];
    }
  }
  onShowAdd(): void {
    this.toggleAdd = true;
  }
  onAdd(): void {
    let theAddress= new Address();
    theAddress.id=this.addId;
    theAddress.accountId=this.addAccountId;
    theAddress.street=this.addStreet;
    theAddress.aptNo=this.addAptNo;
    theAddress.city=this.addCity;
    theAddress.state = this.addState;
    theAddress.zip = this.addZip;
    this.addressService.addAddress(theAddress)
      .subscribe((response:any) => {
        if (response.status === 200){
          this.toggleAdd=false;
          this.notice='Add success!';
        }
        else{
          this.notice='Add fail!';
        }
      });
  }
   onShowUpdate(addressID): void {
    this.toggleUpdate = true;
    this.updateId = addressID;
  }
  onUpdate(): void {
    let theAddress= new Address();
    theAddress.id=this.updateId;
    theAddress.accountId=this.updateAccountId;
    theAddress.street=this.updateStreet;
    theAddress.aptNo=this.updateAptNo;
    theAddress.city=this.updateCity;
    theAddress.state = this.updateState;
    theAddress.zip = this.updateZip;
    this.addressService.updateAddress(theAddress)
      .subscribe((response:any) => {
        console.log(response.status);
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
  onDelete(id): void {
    this.addressService.deleteAddress(id) .subscribe((response:any) => {
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
