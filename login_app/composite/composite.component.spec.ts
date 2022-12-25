import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CompositeComponent } from './composite.component';

describe('CustomerComponent', () => {
  let component: CompositeComponent;
  let fixture: ComponentFixture<CompositeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CompositeComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CompositeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
