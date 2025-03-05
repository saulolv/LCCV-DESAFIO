import { RouterModule, Routes } from '@angular/router';
import { NgModule } from '@angular/core';
import { ProjectFormComponent } from './components/project-form/project-form.component';
import { ProjetoListComponent } from './components/project-list/project-list.component';

export const routes: Routes = [
  { path: '', redirectTo: '/projetos', pathMatch: 'full' },
  { path: 'projetos', component: ProjetoListComponent },
  { path: 'projetos/novo', component: ProjectFormComponent },
  { path: 'projetos/editar/:id', component: ProjectFormComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
