const chatMessages = document.getElementById("chatMessages");
const chatInput = document.getElementById("chatInput");
const sendBtn = document.getElementById("sendBtn");

const contextSite = document.getElementById("contextSite");
const contextPage = document.getElementById("contextPage");

const backendStatus = document.getElementById("backendStatus");


async function loadCurrentTab() {

    const [tab] = await chrome.tabs.query({
        active: true,
        currentWindow: true
    });

    try {

        const url = new URL(tab.url);

        contextSite.textContent = url.hostname;

    } catch {

        contextSite.textContent = "Unknown";

    }

    contextPage.textContent = tab.title;

}


async function checkBackend() {

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/health"
        );

        if (response.ok) {

            backendStatus.textContent = "Connected";

        } else {

            backendStatus.textContent = "Offline";

        }

    } catch {

        backendStatus.textContent = "Offline";

    }

}


function addMessage(text, sender) {

    const message = document.createElement("div");

    message.className = `msg ${sender}`;

    message.innerHTML = `
        <div class="bubble">
            ${text}
        </div>
    `;

    chatMessages.appendChild(message);

    chatMessages.scrollTop =
        chatMessages.scrollHeight;

}


async function sendMessage(text) {

    if (!text.trim())
        return;

    addMessage(text, "user");

    chatInput.value = "";

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/chat/",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    message: text
                })
            }
        );

        const data = await response.json();

        addMessage(
            data.reply,
            "agent"
        );

    } catch {

        addMessage(
            "Backend is offline.",
            "agent"
        );

    }

}


sendBtn.addEventListener(
    "click",
    () => sendMessage(chatInput.value)
);


chatInput.addEventListener(
    "keydown",
    (e) => {

        if (e.key === "Enter" && !e.shiftKey) {

            e.preventDefault();

            sendMessage(chatInput.value);

        }

    }
);


loadCurrentTab();
checkBackend();