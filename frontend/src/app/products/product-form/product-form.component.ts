import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { Product } from '../../core/models/product.model';

@Component({
  selector: 'app-product-form',
  templateUrl: './product-form.component.html',
  imports: [
    CommonModule,
    FormsModule,
    MatCardModule,
    MatIconModule,
    MatButtonModule,
    MatFormFieldModule,
    MatInputModule
  ]
})
export class ProductFormComponent {
  @Input() product: Partial<Product> = {};
  @Output() save = new EventEmitter<Partial<Product>>();

  priceMasked: string = '';

  ngOnInit() {
    if (typeof this.product.price === 'number') {
      this.priceMasked = this.product.price.toFixed(2).replace('.', ',');
    } else if (typeof this.product.price === 'string') {
      this.priceMasked = this.product.price;
    }
  }

  onPriceInput(value: string) {
    // Remove tudo que não é número ou vírgula
    let cleaned = value.replace(/[^\d,]/g, '');
    // Se já tem vírgula, limita a 2 casas decimais
    if (cleaned.includes(',')) {
      const [int, dec] = cleaned.split(',');
      cleaned = int + ',' + (dec.substring(0,2));
    }
    // Se não tem vírgula, adiciona automaticamente ao digitar
    if (!cleaned.includes(',') && cleaned.length > 2) {
      cleaned = cleaned.slice(0, cleaned.length - 2) + ',' + cleaned.slice(-2);
    }
    this.priceMasked = cleaned;
    // Atualiza o valor real no objeto product
    this.product.price = parseFloat(cleaned.replace(',', '.'));
  }

  submit() {
    // Garante que price é float
    if (typeof this.product.price === 'string' && this.product.price) {
      this.product.price = parseFloat((this.product.price as string).replace(',', '.'));
    }
    this.save.emit(this.product);
  }
}
