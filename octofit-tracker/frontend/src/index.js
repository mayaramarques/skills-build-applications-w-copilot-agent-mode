import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// Garantir que a variável de ambiente REACT_APP_CODESPACE_NAME está definida
if (!process.env.REACT_APP_CODESPACE_NAME) {
  console.warn('A variável de ambiente REACT_APP_CODESPACE_NAME não está definida. As URLs da API podem não funcionar corretamente.');
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
