const form = document.getElementById('loginForm');
const status = document.getElementById('status');
const submitBtn = form.querySelector('button.submit');

function showStatus(message, isSuccess) {
  status.textContent = message;
  status.classList.add('visible');
  status.classList.toggle('success', Boolean(isSuccess));
}

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const email = document.getElementById('email').value.trim();
  const password = document.getElementById('password').value;
  const remember = document.getElementById('remember').checked;

  if (!email || !password) {
    showStatus('Enter your email and password to continue.', false);
    return;
  }

  submitBtn.disabled = true;
  submitBtn.textContent = 'Signing in…';

  try {
    const response = await fetch('/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password, remember }),
    });

    const data = await response.json();

    if (!response.ok) {
      showStatus(data.error || 'Something went wrong. Try again.', false);
      return;
    }

    showStatus(data.message || 'Signed in. Redirecting…', true);

    // Confirm the session actually stuck, then move on.
    setTimeout(() => {
      window.location.href = '/';
    }, 900);
  } catch (err) {
    showStatus('Could not reach the server. Check your connection.', false);
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = 'Sign in';
  }
});
