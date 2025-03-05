import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogModule, MatDialogRef } from '@angular/material/dialog';
import { Project } from '../../core/models/project.model';
import { DatePipe } from '@angular/common';

@Component({
  selector: 'app-project-details',
  imports: [MatDialogModule],
  templateUrl: './project-details.component.html',
  styleUrl: './project-details.component.scss',
  providers: [DatePipe]
})
export class ProjectDetailsComponent {
  constructor(
    @Inject(MAT_DIALOG_DATA) public data: Project,
    private dialogRef: MatDialogRef<ProjectDetailsComponent>,
    private datePipe: DatePipe
  ) {}

  closeDialog(): void {
    this.dialogRef.close();
  }

  formatDate(date: string | Date | null): string {
    if (!date) return '';
    return this.datePipe.transform(date, 'dd/MM/yyyy') || '';
  }
}
