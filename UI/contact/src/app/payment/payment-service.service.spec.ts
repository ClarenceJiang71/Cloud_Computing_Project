import { TestBed } from '@angular/core/testing';

import { paymentService } from './payment-service.service';

describe('PaymentServiceService', () => {
  let service: paymentService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(paymentService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
