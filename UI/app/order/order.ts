export class Order {
  shopID: string;
  productID: string;
  date: string;
  num: string;
  orderID: string;
}

export class OrderRsp {
  data: Order
}
