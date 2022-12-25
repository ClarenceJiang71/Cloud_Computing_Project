import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';


import { ReactiveFormsModule } from '@angular/forms';
import { NavtestComponent } from './navtest/navtest.component';
import {NgbNavModule} from "@ng-bootstrap/ng-bootstrap";
import { HomepageComponent } from './homepage/homepage.component';
import { CustomerComponent } from './customer/customer.component';
import { ShopComponent } from './shop/shop.component';
import { ProductComponent } from './product/product.component';
import { OrderComponent } from './order/order.component';
import { AddressComponent } from './address/address.component';


@NgModule({
  declarations: [
    AppComponent,
    HomepageComponent,
    NavtestComponent,
    HomepageComponent,
    CustomerComponent,
    ShopComponent,
    ProductComponent,
    OrderComponent,
    AddressComponent
  ],
    imports: [
        BrowserModule,
        HttpClientModule,
        FormsModule,
        ReactiveFormsModule,
        NgbNavModule
    ],
  providers: [
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }


