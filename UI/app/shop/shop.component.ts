import { Component, OnInit } from '@angular/core';
import {ShopService} from "./shop.service";
import {Shop} from "./shop";

@Component({
  selector: 'app-shop',
  templateUrl: './shop.component.html',
  styleUrls: ['./shop.component.css']
})
export class ShopComponent implements OnInit {
  shopID: string;
  addShopID: string;
  addName: string;
  addPhone: string;
  addEmail: string;
  addAddress: string;
  updateShopID: string;
  updateName: string;
  updatePhone: string;
  updateEmail: string;
  updateAddress: string;
  toggleShop: boolean;
  toggleAdd: boolean;
  toggleUpdate: boolean;
  shopService: ShopService;
  shopsInfo: Shop[];
  notice:string;

  constructor(shopService: ShopService) {
    this.shopID = undefined;
    this.updateShopID = undefined;
    this.notice=undefined;
    this.toggleShop = false;
    this.toggleAdd = false;
    this.toggleUpdate = false;
    this.shopService = shopService;
    this.shopsInfo = undefined;
  }

  ngOnInit(): void {
  }

  toggleCard(cardId): void {
      this.toggleShop = !this.toggleShop;
  }

  setShopInfo(theShop: Shop): void {
    this.shopsInfo = [theShop];
  }




  onLookup(): void {
    if(this.shopID.length>0) {
      this.toggleUpdate=false;
      this.shopsInfo=[];
      this.shopService.getOrder(this.shopID)
        .subscribe((data) => {
          this.setShopInfo(data);
        });
    }
    else {
      this.shopsInfo=[];
    }
  }
  onShowAdd(): void {
    this.toggleAdd = true;
  }
  onAdd(): void {
    let theShop= new Shop();
    theShop.shopID=this.addShopID;
    theShop.name=this.addName;
    theShop.address=this.addAddress;
    theShop.email=this.addEmail;
    theShop.phone=this.addPhone;
    this.shopService.addShops(theShop)
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

  onShowUpdate(shopID): void {
    this.toggleUpdate = true;
    this.updateShopID = shopID;
  }
  onUpdate(): void {
    let theShop= new Shop();
    theShop.shopID=this.updateShopID;
    theShop.name=this.updateName;
    theShop.address=this.updateAddress;
    theShop.email=this.updateEmail;
    theShop.phone=this.updatePhone;
    this.shopService.updateShops(theShop)
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
  onDelete(shopID): void {
    this.shopService.deleteShops(shopID) .subscribe((response:any) => {
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
