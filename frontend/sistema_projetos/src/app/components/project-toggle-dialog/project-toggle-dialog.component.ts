import { Component, Inject } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MAT_DIALOG_DATA, MatDialogModule, MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-project-toggle-dialog',
  imports: [MatDialogModule, MatButtonModule],
  templateUrl: './project-toggle-dialog.component.html',
  styleUrl: './project-toggle-dialog.component.scss'
})
export class ProjetoToggleDialogComponent {
  titulo: string;
  acao: string;
  tipoAcao: 'ativar' | 'inativar';
  nomeProjeto: string;

  constructor(
    public dialogRef: MatDialogRef<ProjetoToggleDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: { 
      nomeProjeto: string, 
      tipoAcao: 'ativar' | 'inativar' 
    }
  ) {
    this.nomeProjeto = data.nomeProjeto;
    this.tipoAcao = data.tipoAcao;
    this.titulo = this.tipoAcao === 'ativar' 
      ? 'Ativar Projeto' 
      : 'Inativar Projeto';
    this.acao = this.tipoAcao;
  }
}