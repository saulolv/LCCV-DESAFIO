import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProjectToggleDialogComponent } from './project-toggle-dialog.component';

describe('ProjectToggleDialogComponent', () => {
  let component: ProjectToggleDialogComponent;
  let fixture: ComponentFixture<ProjectToggleDialogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ProjectToggleDialogComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ProjectToggleDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
