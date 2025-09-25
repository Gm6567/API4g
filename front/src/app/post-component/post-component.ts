import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {FormsModule } from '@angular/forms'
import {CommonModule, JsonPipe} from '@angular/common'

@Component({
  selector: 'app-post-component',
  standalone: true,
  imports: [FormsModule, CommonModule, JsonPipe],
  templateUrl: './post-component.html',
  styleUrls: ['./post-component.css']
})
export class PostComponent {
  inputValue: string = '';
  apiResponse: any;

  constructor(private http: HttpClient) {}

// transform response before displaying it
transform_response(response: any): string {

  const data = Object.values(response)[0] as Record<string, any>;
  if ("error" in data) {
    return "L'adresse n'est pas assez précise ou il manque le code postale"
  }
  const techs = ['2G', '3G', '4G'];
  const results: string[] = [];

  for (const tech of techs) {
    const ok = Object.values(data).some(
      (operator: any) => operator?.[tech] === true
    );
    results.push(`${tech}: ${ok ? 'OK' : 'KO'}`);
  }

  return results.join(', ');
}
  callApi() {
    this.http.post('http://localhost:8000/api', { id: this.inputValue })
      .subscribe({
        next: response => 
          this.apiResponse = this.transform_response(response),
        error: error => {
          this.apiResponse = { error: 'Erreur API' };
          console.error('Erreur API :', error);
        }
      });
  }
}
