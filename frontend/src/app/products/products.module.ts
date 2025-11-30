import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProductsComponent } from './products/products.component';
import { ProductFormComponent } from './product-form/product-form.component';

@NgModule({
  imports: [CommonModule, ProductsComponent, ProductFormComponent],
  exports: [ProductsComponent, ProductFormComponent]
})
export class ProductsModule {}
