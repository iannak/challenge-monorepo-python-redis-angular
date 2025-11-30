import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { Router } from '@angular/router';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatIconModule
  ]
})
export class RegisterComponent {
  email = '';
  password = '';
  error = '';
  success = '';

  constructor(private auth: AuthService, private router: Router) {}

  submit() {
    this.auth.register(this.email, this.password).subscribe({
      next: () => {
        this.success = 'Usuário cadastrado com sucesso!';
        this.error = '';
        setTimeout(() => this.router.navigate(['/auth/login']), 1500);
      },
      error: err => {
        this.error = err?.error?.error || 'Erro ao cadastrar';
        this.success = '';
      }
    });
  }
}
