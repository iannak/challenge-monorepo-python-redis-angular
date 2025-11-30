import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { Observable } from 'rxjs';
import { Product } from '../core/models/product.model';
import { AuthService } from '../auth/auth.service';

@Injectable({ providedIn: 'root' })
export class ProductService {
  private api = environment.apiUrl;

  constructor(private http: HttpClient, private auth: AuthService) {}

  private getAuthHeaders() {
    const token = this.auth.getToken();
    return token ? { headers: new HttpHeaders({ Authorization: `Bearer ${token}` }) } : {};
  }

  list(): Observable<Product[]> {
    return this.http.get<Product[]>(`${this.api}/products`, this.getAuthHeaders());
  }

  create(product: Partial<Product>) {
    return this.http.post(`${this.api}/products`, product, this.getAuthHeaders());
  }

  update(id: number, product: Partial<Product>) {
    return this.http.put(`${this.api}/products/${id}`, product, this.getAuthHeaders());
  }

  delete(id: number) {
    return this.http.delete(`${this.api}/products/${id}`, this.getAuthHeaders());
  }
}
