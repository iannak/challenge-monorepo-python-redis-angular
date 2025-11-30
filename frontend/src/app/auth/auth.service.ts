import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { tap } from 'rxjs/operators';
import { environment } from '../../environments/environment';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private api = environment.apiUrl;

  constructor(private http: HttpClient) {}

  login(email: string, password: string) {
    return this.http.post<any>(`${this.api}/auth/login`, { email, password })
      .pipe(tap(res => {
        if (res && typeof window !== 'undefined' && window.localStorage) {
          if (res.access_token) {
            window.localStorage.setItem('access_token', res.access_token);
          } else if (res.token) {
            window.localStorage.setItem('access_token', res.token);
          } else {
            console.warn('No access_token or token found in response');
          }
        }
      }));
  }

  register(email: string, password: string) {
    return this.http.post<any>(`${this.api}/auth/register`, { email, password });
  }

  logout() {
    if (typeof window !== 'undefined' && window.localStorage) {
      window.localStorage.removeItem('access_token');
    }
  }

  getToken(): string | null {
    if (typeof window !== 'undefined' && window.localStorage) {
      return window.localStorage.getItem('access_token');
    }
    return null;
  }

  isLoggedIn(): boolean {
    const token = this.getToken();
    return !!token;
  }
}
