import { TestBed } from '@angular/core/testing';

import { phoneService} from './phone-service.service';

describe('PhoneServiceService', () => {
  let service: phoneService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(phoneService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
