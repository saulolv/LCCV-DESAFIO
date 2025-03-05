import { RouterOutlet } from "@angular/router";
import { MatToolbarModule } from '@angular/material/toolbar';
import { Component } from "@angular/core";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, MatToolbarModule],
  template: `
    <mat-toolbar color="primary">
      <span>Sistema de Projetos</span>
    </mat-toolbar>
    <div style="padding: 1rem">
      <router-outlet></router-outlet>
    </div>
  `
})
export class AppComponent {}