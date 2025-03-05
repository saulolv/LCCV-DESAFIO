import { TestBed } from '@angular/core/testing';

import { AreaTecnologicaService } from './area-tecnologica.service';

describe('AreaTecnologicaService', () => {
  let service: AreaTecnologicaService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AreaTecnologicaService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
