import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-calculo',
  standalone: false,
  templateUrl: './calculo.component.html',
  styleUrl: './calculo.component.css'
})
export class CalculoComponent {
  num1: number = 0;
  num2: number = 0;
  num3: number = 0;

  requisicoes: any[] = [];

  constructor(private http: HttpClient) {}

  enviar() {
    const payload = {
      num1: this.num1,
      num2: this.num2,
      num3: this.num3
    };

    this.http.post<any>('http://127.0.0.1:8000/processar/', payload)
      .subscribe(res => {
        const requisicao = {
          id: res.id,
          num1: payload.num1,
          num2: payload.num2,
          num3: payload.num3,
          status: res.status,
          media: null,
          mediana: null
        };

        this.requisicoes.push(requisicao);

        // Verifica status real após 2 segundos
        setTimeout(() => {
          this.http.get<any>(`http://127.0.0.1:8000/status/${res.id}/`)
            .subscribe(data => {
              const index = this.requisicoes.findIndex(r => r.id === data.id);
              if (index > -1) {
                this.requisicoes[index] = data;
              }
            });
        }, 2000);
      });
  }
}
