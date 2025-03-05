import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { MatTableDataSource, MatTableModule } from '@angular/material/table';
import { MatDialog, MatDialogModule } from '@angular/material/dialog';
import { Project } from '../../core/models/project.model';
import { ProjetoService } from '../../core/services/projeto.service';
import { ProjectDetailsComponent } from '../project-details/project-details.component';
import { MatCardModule } from '@angular/material/card';
import { MatPaginator, MatPaginatorModule } from '@angular/material/paginator';
import { ProjectFormComponent } from '../project-form/project-form.component';
import { MatIconModule } from '@angular/material/icon';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { CommonModule, DatePipe } from '@angular/common';
import { Router } from '@angular/router';
import { ProjetoToggleDialogComponent } from '../project-toggle-dialog/project-toggle-dialog.component';

@Component({
  selector: 'app-project-list',
  templateUrl: './project-list.component.html',
  styleUrls: ['./project-list.component.scss'],
  standalone: true,
  imports: [
    MatCardModule, 
    MatIconModule, 
    MatPaginatorModule, 
    MatFormFieldModule, 
    MatTableModule, 
    MatDialogModule,
    MatInputModule,
    MatButtonModule,
    CommonModule
  ],
  providers: [DatePipe]

})
export class ProjetoListComponent implements OnInit, AfterViewInit {
  displayedColumns: string[] = ['projeto', 'ativo', 'vigencia', 'acoes'];
  dataSource: MatTableDataSource<Project> = new MatTableDataSource<Project>([]);

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  constructor(
    private projetoService: ProjetoService,
    private dialog: MatDialog,
    private datePipe: DatePipe,
    private router: Router
  ) {}


  ngOnInit() {
    this.carregarProjetos();
  }

  ngAfterViewInit() {
    if (this.paginator) {
      this.dataSource.paginator = this.paginator;
    }
  }

  carregarProjetos() {
    this.projetoService.getProjetos().subscribe({
      next: (projetos) => {
        const formattedProjetos = projetos.map(projeto => ({
          ...projeto,
          inicio_vigencia: this.formatDate(projeto.inicio_vigencia),
          fim_vigencia: this.formatDate(projeto.fim_vigencia)
        }));
        
        this.dataSource.data = formattedProjetos;
                console.log('Projetos carregados', this.dataSource.data);
      },
      error: (error) => {
        console.error('Erro ao carregar projetos', error);
      }
    });
  }

  formatDate(date: string | Date | null): string {
    if (!date) return '';
    return this.datePipe.transform(date, 'dd/MM/yyyy') || '';
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();
  }

  openCadastroDialog() {
    // const dialogRef = this.dialog.open(ProjectFormComponent, {
    //   width: '600px',
    //   data: null
    // });

    // dialogRef.afterClosed().subscribe(result => {
    //   if (result) {
    //     this.carregarProjetos();
    //   }
    // });
    this.router.navigate(['/projetos/novo']);
  }

  visualizarProjeto(projeto: Project) {
    const dialogRef = this.dialog.open(ProjectDetailsComponent, {
      width: '600px',
      data: projeto
    });
  }

  editarProjeto(projeto: Project) {
    // const dialogRef = this.dialog.open(ProjectFormComponent, {
    //   width: '600px',
    //   data: projeto
    // });

    // dialogRef.afterClosed().subscribe(result => {
    //   if (result) {
    //     this.carregarProjetos();
    //   }
    // });
    this.router.navigate(['/projetos/editar', projeto.id_projeto])
    .then(success => console.log('Navigation result:', success))
    .catch(error => console.error('Navigation error:', error));
  }

  toggleProjeto(projeto: Project) {
    try {
      const dialogRef = this.dialog.open(ProjetoToggleDialogComponent, {
        width: '500px',
        data: { 
          nomeProjeto: projeto.projeto, 
          tipoAcao: projeto.ativo ? 'inativar' : 'ativar' 
        }
      });
    
      dialogRef.afterClosed().subscribe(result => {
        if (result) {
          const toggleMethod = projeto.ativo 
            ? this.projetoService.inativarProjeto(projeto.id_projeto)
            : this.projetoService.ativarProjeto(projeto.id_projeto);
          
          toggleMethod.subscribe({
            next: () => {
              // Update local state after successful toggle
              projeto.ativo = !projeto.ativo;
              // Or reload all projects
              this.carregarProjetos();
            },
            error: (error) => {
              console.error('Error toggling project status:', error);
              // Show error message to user
            }
          });
        }
      });
    } catch (error) {
      console.error('Error opening dialog:', error);
    }
  }
}