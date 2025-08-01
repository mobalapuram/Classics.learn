import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import React from 'react'
import './static/index.css'
import './static/projects.css'
import App from './App.tsx'
import { BrowserRouter } from 'react-router-dom'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
)


