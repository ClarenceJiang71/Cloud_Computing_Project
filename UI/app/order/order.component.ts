import { Component, OnInit } from '@angular/core';
import {OrderService} from "./order.service";
import {Order} from "./order";


@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.css']
})
export class OrderComponent implements OnInit {

  orderID: string;
  addOrderID: string;
  addShopID: string;
  addProductID: string;
  addDate: string;
  addNum: string;
  updateOrderID: string;
  updateShopID: string;
  updateProductID: string;
  updateDate: string;
  updateNum: string;
  toggleOrder: boolean;
  toggleAdd: boolean;
  toggleUpdate: boolean;
  orderService: OrderService;
  ordersInfo: Order[];
  notice:string;

  constructor(orderService: OrderService) {
    this.orderID = undefined;
    this.updateOrderID = undefined;
    this.notice=undefined;
    this.toggleOrder = false;
    this.toggleAdd = false;
    this.toggleUpdate = false;
    this.orderService = orderService;
    this.ordersInfo = undefined;
  }

  ngOnInit(): void {
  }

  toggleCard(cardId): void {
      this.toggleOrder = !this.toggleOrder;
  }

  setOrderInfo(theOrder: Order): void {
    this.ordersInfo = [theOrder];
  }




  onLookup(): void {
    if(this.orderID.length>0) {
      this.toggleUpdate=false;
      this.ordersInfo=[];
      this.orderService.getOrders(this.orderID)
        .subscribe((data) => {
          this.setOrderInfo(data);
        });
    }
    else {
      this.ordersInfo=[];
    }
  }
  onShowAdd(): void {
    this.toggleAdd = true;
  }
  onAdd(): void {
    let theOrder= new Order();
    theOrder.orderID=this.addOrderID;
    theOrder.shopID=this.addShopID;
    theOrder.productID=this.addProductID;
    theOrder.date=this.addDate;
    theOrder.num=this.addNum;
    this.orderService.addOrders(theOrder)
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

  onShowUpdate(orderID): void {
    this.toggleUpdate = true;
    this.updateOrderID = orderID;
  }
  onUpdate(): void {
    let theOrder= new Order();
    theOrder.orderID=this.updateOrderID;
    theOrder.shopID=this.updateShopID;
    theOrder.productID=this.updateProductID;
    theOrder.date=this.updateDate;
    theOrder.num=this.updateNum;
    this.orderService.updateOrders(theOrder)
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
  onDelete(orderID): void {
    this.orderService.deleteOrders(orderID) .subscribe((response:any) => {
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
