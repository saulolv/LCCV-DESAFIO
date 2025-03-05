import { Component, Inject, OnInit, Optional } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { ProjetoService } from '../../core/services/projeto.service';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatRadioModule } from '@angular/material/radio';
import { MatInputModule } from '@angular/material/input';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatNativeDateModule } from '@angular/material/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';

import { ActivatedRoute, Router } from '@angular/router';


@Component({
  selector: 'app-project-form',
  imports: [
    MatFormFieldModule, 
    MatCheckboxModule, 
    ReactiveFormsModule, 
    MatRadioModule,
    MatInputModule,
    MatDatepickerModule,
    MatNativeDateModule,
    MatRadioModule,
    MatButtonModule,
    MatIconModule,
    MatCardModule
  ],
  templateUrl: './project-form.component.html',
  styleUrl: './project-form.component.scss'
})
export class ProjectFormComponent implements OnInit{
  projectForm!: FormGroup;
  isEditMode = false;
  projectId: number | null = null;

  constructor(
    private projetoService: ProjetoService,
    private fb: FormBuilder,
    private route: ActivatedRoute,
    private router: Router
  ) {
    this.initForm();
    };



  ngOnInit() {
    this.route.params.subscribe(params => {
      if (params['id']) {
        this.isEditMode = true;
        this.projectId = +params['id'];
        this.loadProjectData(this.projectId);
      }
    });
  }

  private initForm() {
    this.projectForm = this.fb.group({
      projeto: ['', Validators.required],
      inicio: ['', Validators.required],
      fim: ['', Validators.required],
      ativo: [true],
      areaTecnologica: ['', Validators.required],
      coordenador: ['', Validators.required],
      financiador: ['', Validators.required],
    });
  }

  loadProjectData(id: number) {
    this.projetoService.getProjetoById(id).subscribe(project => {
      this.projectForm.patchValue({
        id: project.id_projeto,
        projeto: project.projeto,
        inicio: project.inicio_vigencia,
        fim: project.fim_vigencia,
        ativo: project.ativo,
        coordenador: project.coordenador,
        areaTecnologica: project.area_tecnologica,
        financiador: project.financiador,
      });
    });
  }

  salvarProjeto() {
    if (this.projectForm.valid) {
      
      const formValues = this.projectForm.value;

      const projetoData = {
        projeto: formValues.projeto,
        inicio_vigencia: formValues.inicio,
        fim_vigencia: formValues.fim,
        ativo: formValues.ativo,
        coordenador: formValues.coordenador,
        area_tecnologica: formValues.areaTecnologica,
        financiador: formValues.financiador,
      };
      
      console.log('Projeto data:', projetoData);
      if (this.isEditMode && this.projectId) {
        this.projetoService.editarProjeto(this.projectId, projetoData)
          .subscribe(() => this.router.navigate(['/projetos']));
      } else {
        this.projetoService.cadastrarProjeto(projetoData)
          .subscribe(() => {
            this.router.navigate(['/projetos']);
          });
      }
    }
  }

  cancelOrSave() {
    this.router.navigate(['/projetos']);
  }
}
