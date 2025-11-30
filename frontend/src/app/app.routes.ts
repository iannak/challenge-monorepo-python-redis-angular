import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './auth/login/login.component';
import { RegisterComponent } from './auth/register/register.component';
import { ProductsComponent } from './products/products/products.component';
import { AuthGuard } from './auth/auth.guard';

export const routes: Routes = [
	{ path: 'auth/login', component: LoginComponent },
	{ path: 'auth/register', component: RegisterComponent },
	{ path: 'products', component: ProductsComponent, canActivate: [AuthGuard] },
	{ path: '', redirectTo: 'products', pathMatch: 'full' },
	{ path: '**', redirectTo: 'products' }
];

@NgModule({
	imports: [RouterModule.forRoot(routes)],
	exports: [RouterModule]
})
export class AppRoutingModule {}
