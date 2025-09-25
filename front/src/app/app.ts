import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { PostComponent } from './post-component/post-component';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, PostComponent],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('front');
}
