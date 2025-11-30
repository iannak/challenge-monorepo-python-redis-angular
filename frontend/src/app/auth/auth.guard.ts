import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { AuthService } from './auth.service';

@Injectable({ providedIn: 'root' })
export class AuthGuard implements CanActivate {
  constructor(private auth: AuthService, private router: Router) {}

  canActivate(): boolean {
    const loggedIn = this.auth.isLoggedIn();
    console.log('AuthGuard.canActivate loggedIn:', loggedIn);
    if (loggedIn) return true;
    this.router.navigate(['/auth/login']);
    return false;
  }
}
