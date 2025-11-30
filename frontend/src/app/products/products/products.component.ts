import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ProductService } from '../product.service';
import { Product } from '../../core/models/product.model';
import { AuthService } from '../../auth/auth.service';
import { ProductFormComponent } from '../product-form/product-form.component';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatTableModule } from '@angular/material/table';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  imports: [
    CommonModule,
    FormsModule,
    ProductFormComponent,
    MatCardModule,
    MatIconModule,
    MatButtonModule,
    MatToolbarModule,
    MatTableModule
  ]
})
export class ProductsComponent implements OnInit {
  products: Product[] = [];
  editing: Product | null = null;
  error = '';

  constructor(private svc: ProductService, private auth: AuthService, private router: Router) {}

  ngOnInit() { this.load(); }

  load() {
    this.svc.list().subscribe({
      next: data => {
        this.products = data;
      },
      error: err => {
        this.error = 'Could not load products';
      }
    });
  }

  edit(p: Product) { this.editing = { ...p }; }

  save(product: Partial<Product>) {
    const prod: Product = {
      id: product.id ?? 0,
      name: product.name ?? '',
      price: product.price ?? 0,
      created_at: product.created_at,
      updated_at: product.updated_at
    };
    if (prod.id) {
      this.svc.update(prod.id, prod).subscribe(() => this.load());
    } else {
      this.svc.create(prod).subscribe(() => this.load());
    }
    this.editing = null;
  }

  remove(id?: number) {
    if (typeof id === 'number') {
      this.svc.delete(id).subscribe(() => this.load());
    }
  }

  logout() {
    this.auth.logout();
    this.router.navigate(['/auth/login']);
  }
}
