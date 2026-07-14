// ============================================================
// popup.js
// Powers the chat-style popup: shows which tab you're on,
// lets you send messages, and appends replies to the thread.
// ============================================================

// Grab all the elements we'll need once, at the top,
// so we're not calling document.getElementById() repeatedly.
const chatMessages = document.getElementById('chatMessages');
const chatInput = document.getElementById('chatInput');
const sendBtn = document.getElementById('sendBtn');
const contextSite = document.getElementById('contextSite');
const contextPage = document.getElementById('contextPage');
const backendStatus = document.getElementById('backendStatus');

// ------------------------------------------------------------
// 1. LIVE TAB CONTEXT
// Ask Chrome which tab is currently active, then show its
// domain + title in the little pill under the header.
// ------------------------------------------------------------
function loadCurrentTab() {
    // chrome.tabs is only available inside an extension context,
    // so we guard against it being missing (e.g. testing in a
    // normal browser tab instead of as a loaded extension).
    if (typeof chrome === 'undefined' || !chrome.tabs) {
        contextSite.textContent = 'demo.mode';
        contextPage.textContent = '— chrome.tabs unavailable';
        return;
    }

    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        const tab = tabs[0];
        if (!tab || !tab.url) {
            contextSite.textContent = 'Unknown';
            contextPage.textContent = '— no active tab';
            return;
        }

        try {
            const url = new URL(tab.url);
            contextSite.textContent = url.hostname;
        } catch (err) {
            contextSite.textContent = 'Unknown site';
        }

        contextPage.textContent = '— ' + (tab.title || 'Untitled page');
    });
}

// ------------------------------------------------------------
// 2. RENDERING MESSAGES
// One function that builds either a "user" or "agent" bubble,
// so we don't repeat the same HTML-building code twice.
// ------------------------------------------------------------
function addMessage(text, sender) {
    // sender is either 'user' or 'agent'
    const msg = document.createElement('div');
    msg.className = `msg ${sender}`;

    const mark = document.createElement('div');
    mark.className = 'msg-mark';

    const bubble = document.createElement('div');
    bubble.className = 'bubble';
    bubble.textContent = text; // textContent (not innerHTML) keeps this safe from HTML injection

    msg.appendChild(mark);
    msg.appendChild(bubble);
    chatMessages.appendChild(msg);

    // Auto-scroll to the newest message
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// ------------------------------------------------------------
// 3. SENDING A MESSAGE
// This is where you'll eventually call your real backend.
// For now it echoes back a placeholder reply so the UI is
// fully testable before the AI logic is wired up.
// ------------------------------------------------------------
function sendMessage(text) {
    const trimmed = text.trim();
    if (!trimmed) return;

    addMessage(trimmed, 'user');
    chatInput.value = '';
    autoResizeInput();

    // TODO: replace this with a real call to your backend, e.g.
    // fetch('http://localhost:8000/chat', { method: 'POST', body: JSON.stringify({ message: trimmed }) })
    //   .then(res => res.json())
    //   .then(data => addMessage(data.reply, 'agent'));
    setTimeout(() => {
        addMessage(`Got it — I'll "${trimmed}". (This is a placeholder reply until the backend is connected.)`, 'agent');
    }, 500);
}

// ------------------------------------------------------------
// 4. EVENT LISTENERS
// ------------------------------------------------------------

// Send on button click
sendBtn.addEventListener('click', () => sendMessage(chatInput.value));

// Send on Enter, but allow Shift+Enter for a new line
chatInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage(chatInput.value);
    }
});

// Grow the textarea as the user types, instead of scrolling inside it
function autoResizeInput() {
    chatInput.style.height = 'auto';
    chatInput.style.height = Math.min(chatInput.scrollHeight, 90) + 'px';
}
chatInput.addEventListener('input', autoResizeInput);

// Quick action chips just fill the input and send immediately
document.querySelectorAll('.chip-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
        sendMessage(btn.dataset.prompt);
    });
});

// ------------------------------------------------------------
// 5. INITIAL SETUP
// ------------------------------------------------------------
loadCurrentTab();
backendStatus.textContent = 'Connected'; // swap to 'Disconnected' if your backend ping fails