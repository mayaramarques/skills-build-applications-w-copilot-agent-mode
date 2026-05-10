// src/utils/api.js
export function getApiBaseUrl() {
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  if (codespace) {
    return `https://${codespace}-8000.app.github.dev/api/`;
  }
  return 'http://localhost:8000/api/';
}
