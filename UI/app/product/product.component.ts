import { Component, OnInit } from '@angular/core';
import {ProductService} from "./product.service";
import {Product} from "./product";

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent implements OnInit {

  productID: string;
  addProductID: string;
  addProductName: string;
  addPrice: string;
  updateProductID: string;
  updateProductName: string;
  updatePrice: string;
  toggleProduct: boolean;
  toggleAdd: boolean;
  toggleUpdate: boolean;
  productService: ProductService;
  productsInfo: Product[];
  notice:string;

  constructor(productService: ProductService) {
    this.productID = undefined;
    this.updateProductID = undefined;
    this.notice=undefined;
    this.toggleProduct = false;
    this.toggleAdd = false;
    this.toggleUpdate = false;
    this.productService = productService;
    this.productsInfo = undefined;
  }

  ngOnInit(): void {
  }

  toggleCard(cardId): void {
      this.toggleProduct = !this.toggleProduct;
  }

  setProductInfo(theProduct: Product): void {
    this.productsInfo = [theProduct];
  }




  onLookup(): void {
    if(this.productID.length>0) {
      this.toggleUpdate=false;
      this.productsInfo=[];
      this.productService.getProducts(this.productID)
        .subscribe((data) => {
          this.setProductInfo(data);
        });
    }
    else {
      this.productsInfo=[];
    }
  }
  onShowAdd(): void {
    this.toggleAdd = true;
  }
  onAdd(): void {
    let theProduct= new Product();
    theProduct.productID=this.addProductID;
    theProduct.product_name=this.addProductName;
    theProduct.price=this.addPrice;
    this.productService.addProducts(theProduct)
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

  onShowUpdate(productID): void {
    this.toggleUpdate = true;
    this.updateProductID = productID;
  }
  onUpdate(): void {
    let theProduct= new Product();
    theProduct.productID=this.updateProductID;
    theProduct.product_name=this.updateProductName;
    theProduct.price=this.updatePrice;
    this.productService.updateProducts(theProduct)
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
  onDelete(productID): void {
    this.productService.deleteProducts(productID) .subscribe((response:any) => {
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
