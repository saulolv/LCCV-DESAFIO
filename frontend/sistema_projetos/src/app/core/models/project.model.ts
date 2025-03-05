import { AreaTecnologica } from "./areaTecnologica.model";
import { Financiador } from "./financiador.model";

export interface Project {
    id_projeto: number;
    projeto: string;
    ativo: boolean;
    inicio_vigencia: string | Date;
    fim_vigencia: string | Date;
    coordenador: string;

    id_area_tecnologica: number;
    id_financiador: number;
    financiador: string;
    area_tecnologica: string;
  }