import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Project } from '../models/project.model';

@Injectable({ providedIn: 'root' })
export class ProjetoService {
  private baseUrl = 'https://sume.lccv.ufal.br/homologacao/api/selecao_5_2025/projetos';

  constructor(private http: HttpClient) {}

  /**
   * GET /projetos/listar/
   * Retrieves the list of all projetos.
   */
  getProjetos(): Observable<Project[]> {
    return this.http.get<Project[]>(`${this.baseUrl}/listar/`).pipe(
      catchError(this.handleError)
    );
  }

  /**
   * GET /projetos/form/
   * Retrieves any data needed to populate the "cadastrar" form (e.g. dropdowns).
   */
  getProjetoFormData(): Observable<any> {
    return this.http.get<any>(`${this.baseUrl}/form/`).pipe(
      catchError(this.handleError)
    );
  }

  /**
   * GET /projetos/{id}/visualizar/
   * Retrieves a single projeto by ID.
   */
  getProjetoById(id: number): Observable<Project> {
    return this.http.get<Project>(`${this.baseUrl}/${id}/visualizar/`).pipe(
      catchError(this.handleError)
    );
  }

  /**
   * POST /projetos/cadastrar/
   * Creates a new projeto.
   */
  cadastrarProjeto(projeto: Partial<Project>): Observable<Project> {
    return this.http.post<Project>(`${this.baseUrl}/cadastrar/`, projeto).pipe(
      catchError(this.handleError)
    );
  }

  /**
   * PATCH /projetos/{id}/editar/
   * Edits an existing projeto.
   */
  editarProjeto(id: number, changes: Partial<Project>): Observable<Project> {
    return this.http.patch<Project>(`${this.baseUrl}/${id}/editar/`, changes).pipe(
      catchError(this.handleError)
    );
  }

  /**
   * POST /projetos/{id}/ativar/
   * Activates a projeto (sets "ativo" to true).
   */
  ativarProjeto(id: number): Observable<any> {
    return this.http.post(`${this.baseUrl}/${id}/ativar/`, {}).pipe(
      catchError(this.handleError)
    );
  }

  /**
   * POST /projetos/{id}/inativar/
   * Inactivates a projeto (sets "ativo" to false).
   */
  inativarProjeto(id: number): Observable<any> {
    return this.http.post(`${this.baseUrl}/${id}/inativar/`, {}).pipe(
      catchError(this.handleError)
    );
  }

  private handleError(error: HttpErrorResponse) {
    console.error('API error:', error);
    return throwError(() => error);
  }
}
