import { TestBed } from '@angular/core/testing';

import { FinaciadorService } from './finaciador.service';

describe('FinaciadorService', () => {
  let service: FinaciadorService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FinaciadorService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
