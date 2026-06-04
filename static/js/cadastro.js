/* ============================================================
   EduHub — cadastro.js
   ============================================================ */

// ── Trocar abas ──────────────────────────────────
function switchTab(tipo) {
  ['admin','aluno','prof'].forEach(t => {
    document.getElementById('tab-' + t).className   = 'tab';
    document.getElementById('panel-' + t).className = 'form-panel';
  });
  document.getElementById('tab-' + tipo).className   = 'tab active-' + tipo;
  document.getElementById('panel-' + tipo).className = 'form-panel active';
}

// ── Preview foto (círculo redondo) ───────────────
function previewFoto(input, circleId) {
  const circle = document.getElementById(circleId);
  if (!input.files || !input.files[0]) return;
  const reader = new FileReader();
  reader.onload = e => {
    circle.innerHTML = '';
    const img = document.createElement('img');
    img.src = e.target.result;
    circle.appendChild(img);
    circle.classList.add('has-foto');
  };
  reader.readAsDataURL(input.files[0]);
}

// ── Gerar e-mail + senha automaticamente ─────────
const dominios = { admin: 'administrador.com', aluno: 'aluno.com', prof: 'educador.com' };

function gerarEmail(tipo) {
  const nome = document.getElementById(tipo + '-nome').value.trim();
  if (!nome) return;

  const slug  = nome.toLowerCase()
                    .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
                    .replace(/\s+/g, '.').replace(/[^a-z.]/g, '');
  const email = slug + '@' + dominios[tipo];
  const senha = gerarSenha();

  document.getElementById('cred-' + tipo + '-email').textContent = email;
  document.getElementById('cred-' + tipo + '-senha').textContent = senha;
  document.getElementById(tipo + '-email-hidden').value = email;
  document.getElementById(tipo + '-senha-hidden').value = senha;

  const cred = document.getElementById('cred-' + tipo);
  cred.classList.add('show');
}

function gerarSenha() {
  const chars = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghjkmnpqrstuvwxyz23456789@#!';
  return Array.from({length: 10}, () => chars[Math.floor(Math.random() * chars.length)]).join('');
}

// ── Copiar para área de transferência ────────────
function copiar(elementId) {
  const texto = document.getElementById(elementId).textContent;
  navigator.clipboard.writeText(texto).then(() => {
    const btn = document.querySelector(`[onclick="copiar('${elementId}')"]`);
    const orig = btn.textContent;
    btn.textContent = '✓ Copiado';
    setTimeout(() => btn.textContent = orig, 1500);
  });
}